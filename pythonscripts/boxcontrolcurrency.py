
import requests
#http://www.boxcontrol.net/write-simple-currency-converter-in-python.html#.VQwM5_mUdA4
#https://github.com/boxcontrol
a = raw_input('Enter currency to convert from?')
a = a.upper()

b = raw_input('Enter currency to convert to?')
b = b.upper()

c = float(raw_input('Enter value to convert?'))

url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (a, b)
print url

r = requests.get(url)
print r.json()['v']

print c*r.json()['v']

urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)
print urlalt

#split and strip
split1 = (' : 1 %s = ') % a
strip1 = (' %s</h4>') % b

ralt = requests.get(urlalt)
d = float(ralt.text.split(split1)[1].split(strip1)[0].strip())
print d

print c * d
