#!/bin/bash
#env stat -c %Y 30minupdate.sh
#1428164696
#604800 7days
COMP="604800"
CURFILEDATE=$(env stat -c %Y datewatch.sh)
SERVERDATE=$(env date +%s)
echo "CURFILEDATE: $CURFILEDATE"
echo "SERVERDATE: $SERVERDATE"
echo "COMP: $COMP"
SUMDIFF=$((SERVERDATE - CURFILEDATE))
echo "SUMDIFF: $SUMDIFF"
if [ "$COMP" -le "$SUMDIFF" ]
then
    echo "YAHOO"
else
    echo "NOPE"

fi
exit 0
