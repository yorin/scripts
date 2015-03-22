import urllib2
import re
#http://stackoverflow.com/questions/3398852/using-python-remove-html-tags-formatting-from-a-string
#http://stackoverflow.com/questions/3272123/python-regex-search-multiple-values-in-one-string

req ='http://www.google.com/finance/converter?a=1&from=USD&to=PHP'
#req ='http://www.google.com/finance/converter?a=1&from=USD&to=PHP?format=json'
#req = 'http://www.voidspace.org.uk'
response = urllib2.urlopen(req)
#print response.read()
#the_page = response.read()
raw_data = response.read()
#raw_data = raw_data.replace('\xa0','')
#j = req.sanitize(raw_data)
#data = json.loads(j)
#print raw_data
print re.search("<div id=currency_converter_result>.*", raw_data).group()
raw_data = re.search("<div id=currency_converter_result>.*", raw_data).group()
p = re.compile(r'<.*?>|=')
print p.sub( '', raw_data)
#raw_date = p.sub('', raw_data)
print re.split("\s+", p.sub('', raw_data))
list1 = re.split("\s+", p.sub('', raw_data))

print list1[2]
