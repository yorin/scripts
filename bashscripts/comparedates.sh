#!/bin/bash
#http://unix.stackexchange.com/questions/84381/how-to-compare-two-dates-in-a-shell
todate=$(date -d 2013-07-18 +"%y%m%d")
cond=$(date -d 2013-07-15 +"%y%m%d")

if [ $todate -ge $cond ]; #put the loop where you need it
then
 echo 'yes';
 sleep 3;
fi

date_a=2013-07-18
date_b=2013-07-15

if [[ "$date_a" > "$date_b" ]] ;
then
    echo "break"
fi
