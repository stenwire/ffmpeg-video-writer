#!/usr/bin/env bash

ffmpeg -framerate 1 -i ./images/num%d.jpg -c:v libx264 -r 30 ./results/output.mp4
