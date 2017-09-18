#!/bin/sh

python3 red_bird.py -l $1 -p SearchAgent -a fn=astar,heuristic=$2
