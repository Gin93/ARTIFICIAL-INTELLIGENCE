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



solve satisfy;



output [ "\(T) \(C) \n"] ++
	[if fix( delivery[t,5*c-1]) != 0 \/ fix( delivery[t,5*c] !=0) 
		then "\(delivery[t,5*c-4]) \(delivery[t,5*c-3]) \(delivery[t,5*c-2]) \(delivery[t,5*c-1]) \(delivery[t,5*c]) \n" 
		else "" endif |  t in trucks,c in 1..C ];


