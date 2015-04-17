#!/bin/bash 

if [ "$#" == "0" ]; then
    echo "You need to supply at least one domain name!" 
    exit 1
fi

DOMAINS=( '.com' '.net' '.info' '.us' '.co' \ 
'.org' '.tel' '.biz' '.tv' '.cc' '.eu' '.ru' \ 
'.in' '.it' '.sk' '.com.au' '.sh' '.re' '.dk' )

ELEMENTS=${#DOMAINS[@]}

while (( "$#" )); do

  for (( i=0;i<$ELEMENTS;i++)); do
      whois $1${DOMAINS[${i}]} | egrep -q '^No match|^NOT FOUND|^Not fo|AVAILABLE|^No Data Fou|has not been regi|No entri'
          if [ $? -eq 0 ]; then
              echo "$1${DOMAINS[${i}]} : available" 
          fi
  done

shift

done
