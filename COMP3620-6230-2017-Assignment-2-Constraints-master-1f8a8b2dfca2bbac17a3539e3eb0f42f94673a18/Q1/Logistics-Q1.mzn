int: C;					  				% Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types

array[trucks] of int: cap;	          	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers

% Insert your variables and constraints here


array [customers,trucks] of var 0..MAXCAP: deliverychilled; % chilled goods delivery matrix
array [customers,trucks] of var 0..MAXCAP: deliveryambient; % ambient goods delivery matrix

constraint forall (j in trucks)   %cannot exceed the cap
	( (sum (i in customers) (deliverychilled[i,j]) + sum (i in customers)(deliveryambient[i,j])) <= cap[j]);
constraint forall (j in customers , i in trucks) (
	if refrig[i] ==false then  deliverychilled[j,i] = 0 else true endif );
constraint forall (i in customers) 
	(sum (j in trucks)(deliverychilled[i,j]) = order[1,i] );
constraint forall (i in customers) 
	(sum (j in trucks)(deliveryambient[i,j]) = order[2,i] );
solve satisfy;

output [ "\(T), \(C)\n"] ++
[if fix(deliverychilled [i,j]) !=0 \/ fix(deliveryambient [i,j])!=0 then "\(j),\(i),\(deliverychilled [i,j]),\(deliveryambient [i,j]) \n" else "" endif |  j in trucks,i in customers ];


