# Breadth-First Search
## _The Simplest Uninformed/Blind Search Algorithm_ (15 Marks)

### What We Expect You To Do

Implement the Breadth-First Search (BrFS) algorithm inside the `solve()`
function provided in the file [`brfs_search.py`](../code/brfs_search.py).
Remember, BrFS explands the shallowest node on the frontier, i.e. newly
generated nodes are placed on the frontier using a FIFO policy.

You will get full marks if your implementation of BrFS has **all** the following
properties:

1. It returns a **valid** sequence of actions, (all moves are legal and the
   sequence of moves leads from the initial state to the goal)
2. It visits states in the **right** order, (see ldescription of BrFS in the lectures)
2. it produces an **optimal** solution, (that is the number of steps is minimal)
3. Your implementation is not substantially slower than our solution over the maps
   `anuSearch`, `aiSearch` and `mazeSearch`

The times of our solution on the three maps mentioned above are:

| Problem    | Expanded | Time (secs) |
|------------|----------|-------------|
| anuSearch  | 28,488   | 0.2         |
| aiSearch   | 21,881   | 0.15        |
| mazeSearch | 275      | 0.011       |

The times above have been averaged over several runs. The measurements were taken
with the Windows 10 64-bit build of Python 3.5.1 on an Intel i7-4400k CPU running
at a clock speed of 3.4 GHz. We will be testing your code on the same hardware.

You can test your implementation with the command

```
$ python3 red_bird.py -l <map> -p SearchAgent -a fn=bfs
```

where `<map>` is one of the instances for the simple navigation problem.

### Hints

1. Remember that BrFS *expands* the *shallowest* nodes on the frontier.
2. In [frontiers.py](../code/frontiers.py) you will find a number of data
   structures readily available, and which may be useful for you to implement
   the appropriate frontier.
3. Be sure to avoid generating a path to the same state more than once.

### What to Submit

You need to include in your submission the file `brfs_search.py` with your
implementation of BrFS. Please, remember to fill in your details in the comments
at the start of the file.
