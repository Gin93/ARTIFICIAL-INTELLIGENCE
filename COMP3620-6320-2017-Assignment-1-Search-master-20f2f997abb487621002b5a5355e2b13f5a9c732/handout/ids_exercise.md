# Iterative Deepening Search
## _Another uninformed but less memory consuming algorithm_ (15 Marks)

### What We Expect You To Do

Implement the Iterative Deepening Search (IDS) algorithm inside the `solve()`
function in [`ids_search.py`](../code/ids_search.py).

Remember from the lectures that this search algorithm performs a series of
depth-limited Depth First Searches (DFS). This enables it to combine the
completeness and optimality guarantees of BrFs, with low space
requirements of DFS (O(bm)), at the extra cost of exploring the same prefix of the
search tree many times. Remember also that DFS expands always the deepest node on the frontier first,
and this can be implemented using a LIFO policy (Last In First Out).

You will get full marks if your implementation of IDS has **all** the following properties:

1. It returns a **valid** sequence of actions, (all moves are legal and the
   sequence of moves leads from the initial state to the goal)
2. It visits states in the **right** order, (see description of IDS in the
   lectures)
3. It produces an **optimal** solution, (that is the number of steps is minimal)
4. The number of nodes on the fringe is **linear** in the depth of the deepest node
5. In case no solution is found, the procedure prints on the standard output a **lower-bound** on the
   optimal solution cost. 
6. Your implementation is not substantially slower than our solution over the maps
   `anuSearch`, `aiSearch` and `mazeSearch` 

The following table shows the
   performance and results of our solution:

    | Problem    | Cost | Expanded   | Time (secs) |
    |------------|------|------------|-------------|
    | anuSearch  | 24   | NA         | TO          |
    | aiSearch   | 26   | 43,652,859 | 344.1       |
    | mazeSearch | 68   | 16469     | 0.2       |

    TO in this experiment means that the system was not able to produce a result
    within 30 minutes; *Cost* for this instance is only a **lower-bound** on the
    actual cost. The measurements were taken with the Ubuntu 16.04.1 LTS, Python
    3.5.1 on an Intel Core i7-4770 CPU @ 3.40GHz × 4. We will be testing your code
    on the same hardware.

You can test your implementation with the command

```
$ python3 red_bird.py -l <map> -p SearchAgent -a fn=ids
```

where `<map>` is one of the instances for the simple navigation problem.

### Hints

1. At each iteration, IDS **expands** first the *deepest* nodes on the frontier. 
2. In [frontiers.py](../master/code/frontiers.py) you will find a number of data
   structures readily available for you to use. 
3. The depth-first implementation can be either the recursive or iterative (see
   lectures).
4. In order to achieve our similar performances, you need a smart way to detect
   loops, which does not compromise optimality, and preserves the O(bm) space requirement
5. In order to print the lower bound, just take advantage from the fact that each *failing iteration* still tells you something

### What to Submit

You need to include in your submission the file `ids_search.py` with your implementation
of IDS. Please, remember to fill in your details in the comments at the start of the file.
