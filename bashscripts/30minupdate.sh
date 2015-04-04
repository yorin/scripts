#!/bin/bash
#env stat -c %Y 30minupdate.sh
#1428164696
CURDATEFILE=$(env stat -c %Y datewatch.sh)
SERVERDATE=$(env date +%s)
echo "$CURDATEFILE"
echo "$SERVERDATE"
env TZ=EDT date +%s
DATA=$((1428157831 - 1428157802))
#1428164696
echo "$DATA"
