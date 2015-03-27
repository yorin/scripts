#!/bin/bash

#date
#env TZ=EST5EDT date
while [ 1 ] ;# loop forever
do
    echo -e '\0033\0143'
    date
    env TZ=EST5EDT date
    env TZ=CST6CDT date
    sleep 1 ;# wait a bit
done
