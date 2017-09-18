include "alldifferent.mzn";
%include "Logistics-Q3-4-3.dzn";
int: C;					  % Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types
set of int: times = 0..C+1;            	  % Enough times to visit each customer once and depot twice if needed

array[trucks] of int: cap;	     	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers
array[trucks] of int: centsPerKm;         % Cost of running trucks (in cents per km)
array[customers,customers] of int: D;  	  % Distances between customers (including the depot)


array [trucks,1..5*C] of var 0..T+C+MAXCAP: delivery; 

constraint forall (t in trucks, c in 1..C) % remember * 5
	( delivery [t,5*c-4] = t ); % the first number in each block
	
constraint forall (t in trucks, c in 1..C) % remember * 5
	( delivery [t,5*c-3] = c ); % the second number 
	
constraint forall (t in trucks, c in 1..C) % the fourth number 
	(if refrig[t] == false then delivery [t,5*c-1] = 0 else true endif);  % chilled must be stored in refrigerated

constraint forall (c in 1..C) % the fourth 
	(sum (t in trucks) ( delivery[t,5*c-1]) = order [1,c] ); % ordered chilled food must be satisfied
	
constraint forall (c in 1..C) % the fifth 
	(sum (t in trucks) ( delivery[t,5*c]) = order [2,c] ); % ordered ambient food must be satisfied
	
constraint forall (t in trucks) % the fourth and fifth
	( sum (c in 1..C) (delivery[t,5*c-1]) + sum (c in 1..C) (delivery[t,5*c]) <= cap [t]); % cannot over the cap

array [trucks] of var times: maxtimes; % for each truck, the maximial times of visit

%below four constraints to set the times 

constraint forall(t in trucks)
	(maxtimes[t] < 3);
	
constraint forall (t in trucks) 	% get the maximial visit times for each truck
	( maxtimes[t] = sum (c in 1..C) (bool2int(delivery[t,5*c-1] != 0 \/ delivery[t,5*c] !=0) ));
	
		
constraint forall (t in trucks, c in 1..C)
	(if ( delivery[t,5*c-1] != 0 \/ delivery[t,5*c] !=0) 
		then delivery[t,5*c-2] > 0  /\ delivery[t,5*c-2] <=maxtimes[t]  % set the times as  1--maxtimes  if the truck need visit that customer
		else delivery[t,5*c-2] = 0 endif);  
	
constraint forall (t in trucks)
	(forall (i,j in 1..C where (delivery[t,5*i-1] != 0 \/ delivery[t,5*i] !=0) /\  (delivery[t,5*j-1] != 0 \/ delivery[t,5*j] !=0) /\ i!=j )
	(delivery[t,i*5-2] != delivery[t,j*5-2]));

var int: tot_cost;	      	   	  % Total cost of the solution

constraint tot_cost =sum(t in trucks where maxtimes[t]>0 /\ maxtimes[t] < C+1)(
	sum (a,b in 1..C  where  (delivery[t,5*a-2]-delivery[t,5*b-2] == 1 /\ delivery[t,5*b-2] > 0 ))(centsPerKm[t] * D [a,b])+ 
	sum (c in 1..C where delivery[t,5*c-2] == 1) (  centsPerKm [t] * D[0,c])+
	sum(c in 1..C where delivery[t,5*c-2] == maxtimes[t])( centsPerKm [t] * D[c,0]) );

%solve satisfy;
solve minimize tot_cost;


output [ "\(T) \(C) \n"] ++
	["\(maxtimes) \n"]++
	["\(tot_cost) \n"]++
	[if fix( delivery[t,5*c-1]) != 0 \/ fix( delivery[t,5*c] !=0) 
		then "\(delivery[t,5*c-4]) \(delivery[t,5*c-2]) \(delivery[t,5*c-3]) \(delivery[t,5*c-1]) \(delivery[t,5*c]) \n" 
		else "" endif |  t in trucks,c in 1..C ];


