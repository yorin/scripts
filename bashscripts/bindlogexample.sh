#https://raymii.org/s/software/Bind-GNUPlot-DNS-Bar-Graph.html
#http://www.pablumfication.co.uk/2010/09/03/bind-logs-top-dns-queries/
 awk '{ print $8 }' /var/named/data/named.run | sort | uniq -c | sort -n | tail -n 100
