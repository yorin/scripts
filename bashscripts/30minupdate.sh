#!/bin/bash
#env stat -c %Y datewatch.sh
#1428164696
#1800 30mins
COMP="1800"
CURFILEDATE=$(env stat -c %Y .cache/test.txt)
SERVERDATE=$(env date +%s)
echo "CURFILEDATE: $CURFILEDATE"
echo "SERVERDATE: $SERVERDATE"
echo "COMP: $COMP"
SUMDIFF=$((SERVERDATE - CURFILEDATE))
echo "SUMDIFF: $SUMDIFF"
if [ "$COMP" -le "$SUMDIFF" ]
then
    echo "YAHOO"
    echo $(date) >> .cache/test.txt
else
    echo "NOPE"
fi
exit 0
