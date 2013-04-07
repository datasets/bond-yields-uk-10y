#!/bin/bash
echo "Year,Rate" > annual.csv
cat cache/10y.csv | tail -n+2 | sed "s/^.\{7\}//" | sed "s///g" >> annual.csv
