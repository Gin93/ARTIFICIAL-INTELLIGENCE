include "alldifferent.mzn";
int: C;					  % Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types
set of int: times = 0..C+1;            	  % Enough times to visit each customer once and depot twice if needed

array[trucks] of int: cap;	     	  	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers


array [customers,trucks] of var 0..MAXCAP: deliverychilled; % chilled goods delivery matrix
array [customers,trucks] of var 0..MAXCAP: deliveryambient; % ambient goods delivery matrix
% Important! Above two variables are intermediate variables, they will not be outputted.
% I use these two variables in order to speed up this program in order to SOLVE THE "21-8" PROBLEM WITHIN 1 MIN (ACTUALLY WITHIN 5S)


%below fours come from Q1
constraint forall (j in trucks)   %cannot exceed the cap
	( (sum (i in customers) (deliverychilled[i,j]) + sum (i in customers)(deliveryambient[i,j])) <= cap[j]);
constraint forall (j in customers , i in trucks) (
	if refrig[i] ==false then  deliverychilled[j,i] = 0 else true endif );
constraint forall (i in customers) 
	(sum (j in trucks)(deliverychilled[i,j]) = order[1,i] );
constraint forall (i in customers) 
	(sum (j in trucks)(deliveryambient[i,j]) = order[2,i] );

array [trucks,1..5*C] of var 0..T+C+MAXCAP : delivery;  % the output matrix

constraint forall (c in 1..C, t in trucks) % the fourth 
	(delivery[t,5*c-1] = deliverychilled[c,t]); % ordered chilled food must be satisfied
	
constraint forall (c in 1..C , t in trucks) % the fifth 
	( delivery[t,5*c] = deliveryambient [c,t] ); % ordered ambient food must be satisfied
	
constraint forall (t in trucks, c in 1..C) % remember * 5
	( delivery [t,5*c-4] = t ); % the first number in each block
	
constraint forall (t in trucks, c in 1..C) % remember * 5
	( delivery [t,5*c-3] = c ); % the second number 
	
constraint forall (t in trucks, c in 1..C) % deal with the sequences
	( if delivery[t,5*c-1] = 0 /\ delivery[t,5*c] =0 
		then delivery[t,5*c-2] = 0 
		else true endif ); % if not delivery then set the sequences as 0

constraint forall (t in trucks, c in 1..C) % the third
	(if c = 1 /\ ( delivery[t,5*c-1] != 0 \/ delivery[t,5*c] !=0) 
		then delivery[t,5*c-2] = 1 
		else true endif);
		
constraint forall (t in trucks, c in 2..C) % the third
	( if ( delivery[t,5*c-1] != 0 \/ delivery[t,5*c] !=0) 
		then delivery [t,5*c-2 ] = 1 + max (i in 1..C where i < c) (delivery [t,5*i-2 ]) 
		else true endif);
		
solve satisfy;

output [ "\(T),\(C) \n"] ++
	[if fix(deliverychilled [i,j]) = 0 then "" else "" endif | i in customers,j in trucks] ++
	[if fix(deliveryambient [i,j]) = 0 then "" else "" endif | i in customers,j in trucks] ++
	%above two matrix will NEVER be outputed, but they are necessary!! the reason you will see in the report
	[if fix( delivery[t,5*c-1]) != 0 \/ fix( delivery[t,5*c] !=0) 
		then "\(delivery[t,5*c-4]),\(delivery[t,5*c-2]),\(delivery[t,5*c-3]),\(delivery[t,5*c-1]),\(delivery[t,5*c]) \n" 
		else "" endif |  t in trucks,c in 1..C ];
