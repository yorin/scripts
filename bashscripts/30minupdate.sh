#!/bin/bash
#env stat -c %Y 30minupdate.sh
#1428164696
#604800 7days
CURFILEDATE=$(env stat -c %Y datewatch.sh)
SERVERDATE=$(env date +%s)
echo "CURFILEDATE: $CURFILEDATE"
echo "SERVERDATE: $SERVERDATE"
SUMDIFF=$((SERVERDATE - CURFILEDATE))
echo "SUMDIFF: $SUMDIFF"
