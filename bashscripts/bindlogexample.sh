#https://raymii.org/s/software/Bind-GNUPlot-DNS-Bar-Graph.html
#http://www.pablumfication.co.uk/2010/09/03/bind-logs-top-dns-queries/
#https://encodable.com/tech/blog/2008/12/17/Count_IP_Addresses_in_Access_Log_File_BASH_OneLiner
awk '{ print $8 }' /var/named/data/named.run | sort | uniq -c | sort -n | tail -n 100
