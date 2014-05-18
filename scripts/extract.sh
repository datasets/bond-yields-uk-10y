#!/bin/bash
echo "Year,Rate" > data/annual.csv
cat cache/10y.csv | tail -n+2 | sed "s/^.\{7\}\(....\)/\1-12-31/" | sed "s///g" >> data/annual.csv

# quarterly
echo "Date,Rate" > data/quarterly.csv
cat cache/10y-q.csv | tail -n+2 | sed "s/^\(..\) \(...\) \(....\)/\3-\2-\1/" | sed "s/Mar/03/" | sed "s/Jun/06/" | sed "s/Sep/09/" | sed "s/Dec/12/" | sed "s///g" >> data/quarterly.csv 

