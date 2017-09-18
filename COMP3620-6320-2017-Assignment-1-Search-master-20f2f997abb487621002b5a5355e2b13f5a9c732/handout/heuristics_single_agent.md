# Developing Heuristics
## _Dealing with Multiple Goals_ (20 Marks)

### What We Expect You To Do

The red-bird in this case has to collect all the yellow-birds on the map!
First, we will take a look at the performance of A* with the _null heuristic_ _h(s)=0_ (**Note:** in this case
A* becomes the Uniform Cost strategy). Then, you will start with a *very simple*
heuristic that captures the essence of the task (picking up yellow birds), but already
significantly improves the runtime of A*. Finally, you will move onto a more powerful heuristic.

Each of the two latter heuristics will need to be implemented inside the file
[heuristics.py](../code/heuristics.py)

### The Baseline Heuristic

Let's first assess how well the null heuristic handles the navigation problem
with constraints. With this command
```
$ python3 red_bird.py -l search_layouts/<map> -p SearchAgent -a fn=astar,prob=MultiplePositionSearchProblem,heuristic=null
```
you can run your implementation of A* with the _null heuristic_ over the instances
of this harder problem in the files:

- `smallMultiSearch.lay`
- `aiMultiSearch.lay`
- `anuMultiSearch.lay`
- `mazeMultiSearch.lay`

On our test machine, we get the following results with our implementation of A*:

Problem | Cost | Expanded Nodes | Time (secs)
--------|------|----------------|-----
aiMultiSearch | 55 | 6,633 | 0.04
anuMultiSearch | 99 | 13,912 | 0.09
smallMultiSearch | 60| 16,688 | 0.11
mazeMultiSearch | 215  | 534,496 | 4.9


### Counting Birds (5 Marks)

The first admissible heuristic we will consider is given by the following formula:
```
h(s) = # yellow birds still to be captured
```
Implement the above in the function `bird_counting_heuristic()` in the file
[heuristics.py](../code/heuristics.py).

You can see the effect of using this heuristic with the following command:
```
python3 red_bird.py -l search_layouts/<map> -p SearchAgent -a fn=astar,prob=MultiplePositionSearchProblem,heuristic=bch
```

Verify that your heuristic works correctly (it needs to be _0_ for *goal states*)
and also comparing with the tables below for A*:

Problem | Cost | Expanded Nodes | Time (secs)
--------|------|----------------|-----
aiMultiSearch | 55 | 6,092 | 0.038
anuMultiSearch | 99 | 13,502 | 0.082
smallMultiSearch | 60 | 12,517  | 0.08
mazeMultiSearch | 215 | 485,961 | 4.65


This heuristic is indeed **admissible** but it is still not very **informative** because it completely abstracts the navigation problem away.  The effect of this becomes stronger
on the larger problems.

### Come up with your heuristic! (15 Marks)

In this exercise you are requested to devise a much **more informative admissible** heuristic for the problem.

Implement the above in the function `every_bird_heuristic()` in the file
[heuristics.py](../code/heuristics.py).

This heuristic will be graded according to different factors:

1. Admissibility: your heuristic value must not exceed the smaller number of steps to collect all yellow birds. It has to however be more informed (give higher value) than the counting birds heuristic at least
in the initial state.
2. Informativeness: measured by the reduction of Expanded Nodes
3. Efficiency: reduction of run-time.

You can see the effect of your implementation launching the following command:
```
python3 red_bird.py -l search_layouts/<map> -p SearchAgent -a fn=astar,prob=MultiplePositionSearchProblem,heuristic=every_bird

```
The reduction of number of expanded nodes and efficiency is compared with the counting
birds heuristic presented above (our implementation). We expect to see substantial efficiency gains in the bigger instance (i.e., mazeMultiSearch).

Our current implementation achieves the following performance though you are not required to compare with it, but can use it as reference


Problem | Cost | Expanded Nodes | Time (secs)
--------|------|----------------|-----
aiMultiSearch | 55 | 210 | 0.4  
anuMultiSearch | 99| 316 | 0.4  
smallMultiSearch | 60 | 410 | 0.5  
mazeMultiSearch | 215| 696 | 0.6

Hints
1. Your heuristic should not try to solve the original problem! It has to relax
   it to make it simpler so that the heuristic be efficiently computable. There
   is a tradeoff between efficiency and informativeness.
2. There are many ways to relax the problem (see lectures for examples).
3. The class search\_problems contains a very interesting method that is called "get\_maze\_distances". You may want to have
a look into it.
4. If you are heuristic is admissible, but not consistent, it is important that your implementation of A* is able (if necessary) to re-open nodes
which are already been expanded (they are in the explored set)
