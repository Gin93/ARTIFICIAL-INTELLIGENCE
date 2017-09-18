#!/bin/sh

python3 red_bird.py -p MinimaxAgent -l $1 -a depth=${2} -b GreedyBlackBirdAgent --frame_time 0.1
