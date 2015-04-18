 awk '{ print $8 }' /var/named/data/named.run | sort | uniq -c | sort -n | tail -n 100
