#!/bin/bash

export DISPLAY=:0

sleep 5
notify-send -r 1 "Started auto";
sleep 1
totalcount="$1"

counter=1

while [ $counter -le $totalcount ]
do
    echo "Counter: $counter"
    notify-send -r 1 "$counter/$totalcount"
    ((counter++))  # Increment counter
sleep 3.5
xdotool key End
sleep .5
xdotool key f
sleep .5
xdotool key k
sleep .5
xdotool key Enter
sleep .5
xdotool key f
sleep .5
xdotool key s
sleep .5
done

notify-send -r 1 -t 0 "Completed !"
