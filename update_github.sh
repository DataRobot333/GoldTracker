#!/bin/bash

cd /home/rad/Projects/GoldTracker || exit 1
/usr/bin/python3 collector.py || exit 1

git add data/gold_price.csv

git commit -m "update csv"

git push origin main
