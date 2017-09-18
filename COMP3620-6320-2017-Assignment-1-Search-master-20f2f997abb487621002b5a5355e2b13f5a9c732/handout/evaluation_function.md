# Evaluation Functions for Two-Player Games (15 Marks)

### What We Want You To Do

Improve upon your Minimax agent by implementing a strong *evaluation function*
for this game. The evaluation function will be invoked when the search cannot
reach a terminal state within the given **depth limit**.

You need to implement your evaluation function in such a way that you can
use it within the method `evaluation()` of the class `MinimaxAgent` in [minimax_agent.py](../code/minimax_agent.py).
Besides that, you will have to create and include a text file called 
`eval_function.results.md` whose contents are detailed below.

You will get **10** marks if your Minimax implementation, when augmented with your evaluation
function, obtains these or better scores on the following maps with the given (or
smaller) depths

Maze | Depth | Score
-----|-------|-----
testAdversarial | 12 | 89.11
smallAdversarial | 2 | 92.18
aiAdversarial | 10 | 86.87
anuAdversarial | 8 | -316
mazeAdversarial | 10 | -253
smallDenseAdversarial | 6 | 342.6  
aiDenseAdversarial | 6 | -1142.7 
anuDenseAdversarial | 6 | -1169.8 
mazeDenseAdversarial | 6 | 533 

We need you to include in the file `eval_function.results.md` a table like the one above, encoded
using MarkDown syntax (see the source of this file to see how to do that),
reporting your depths and scores.

You can do the tests with the following command

```
$ python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/<map>.lay -a depth=<d> -b GreedyBlackBirdAgent
```

where `<map>` is the map name, and `<d>` is the value for the depth.

You will get another **5** marks if your agent succeds in the above experiments within 60 seconds. This can be tested as follows:
```
$ python3 red_bird.py -p MinimaxAgent -l adv_search_layouts/<map>.lay -a depth=<d> -b GreedyBlackBirdAgent --timeout 60 -c
```

### Hints

1. The value that this function returns should reflect an estimate of
the maximum score the red agent can attain from the given state. However, you might find
this exercise difficult if you take that too literally.

2. Read carefully the section on Adversarial Search in the [Getting Started](getting_started.md)
and [Implementation Notes](implementation_notes.md) sections. All you need to think
about and implement a strong evaluation function can be found in those two documents.

3. The default implementation (see the implementation of `evaluation()` in
`MinimaxAgent` for example) just returns the score of a given state. Think
hard about the following: why did this (dummy) evaluation function work quite well
on the test map?

4. You can greatly speed up the proceedings using the command line argument '-q', this kills the graphics.

5. Make sure that your evaluation isn't too pessimistic. This can get you into trouble, since Minimax is 
built around the assumption that the MAX player is being realistic about its possibilities and possible winning
strategies may be pruned away.
