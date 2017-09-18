# A*
## _An Informed Search Algorithm_ (20 Marks)

### What We Expect You To Do

Implement the A* search algorithm inside the
`solve()` function in [`a_star_search.py`](../code/a_star_search.py).

Your A* search will use the heuristic contained in the `heuristic` argument passed
to the `solve()` function in [`a_star_search.py`](../code/a_star_search.py).
The heuristics take a state and return an estimate of the cost to reach
the goal from that state. The heuristics are defined in [heuristics.py](../code/heuristics.py)
and for the simple navigation search problem we include three heuristics:

- The null heuristic, i.e. _h(s) = 0_ for every state _s_,
- the Manhattan distance heuristic, _h(s) = |x(s) - x(G)| + |y(s) - y(G)|_ where
_x()_ and _y()_ are the coordinates of the given state _s_ or goal state _G_,
- and the Euclidean distance heuristic, _h(s) = sqrt( |x(s) - x(G)|^2 + |y(s) - y(G)|^2 )_.


You will get full marks if your implementation of A* has **all** the following properties:

1. It returns a **valid** sequence of actions, (all moves are legal and the
   sequence of moves leads from the initial state to the goal)
2. The sequence of actions has **optimal length** when using an admissible
   heuristic (such as the *Manhattan Distance* and the *Euclidean Distance*
   heuristic)
3. It visits states in the **right** order, (it expands nodes with smaller f-values first)
4. Your implementation is not substantially slower than our solution over the maps
   `anuSearch`, `aiSearch` and `mazeSearch`. 

The times and costs of optimal
   solutions with our implementation on the three maps mentioned above are:

    | Problem    | Cost | Expanded Manhattan |Time w. Manhattan (secs) | Expanded Euclidean | Time w. Euclidean (secs) |
    |------------|------|--------------------|-------------------------|--------------------|-------------------------|
    | anuSearch  | 45 | 222 | 0.0084 | 200 | 0.0076  |
    | aiSearch | 26  | 59 | 0.0024 | 89 | 0.00425  |
    | mazeSearch | 68 | 221 | 0.009 | 226 | 0.01  |

    the times above have been averaged over several runs. The measurements were
    taken with the Debian/Ubuntu 64-bit build of Python 3.5.1 on an Intel
    i7-4770 CPU running at a clock speed of 3.4 GHz. We will be testing your
    code on the same hardware.

You can test your implementation with the command

```
$ python3 red_bird.py -l <map> -p SearchAgent -a fn=astar,heuristic=manhattan
```

where `<map>` is one of the instances for the simple navigation problem.

### Hints

1. A* **expands** first the nodes on the frontier with *minimum f-value*.
2. In [frontiers.py](../code/frontiers.py) you will find a number of data structures
readily available for you to use. 
3. Be sure to avoid generating a path to the same state more
than once.

### What to Submit

You need to include in your submission the file `a_star_search.py` with your implementation
of A*. Please, remember to fill in your details in the comments at the start of the file.
