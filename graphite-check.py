#!/usr/bin/env python
from optparse import OptionParser
import sys
import requests


options = OptionParser()
options.add_option("-u", "--url"      , dest="url",help="graphite url", default="http://graphite.example.com")
options.add_option("-c", "--critical", 	dest="critical",help="critical limit", default="1024" , type ="int")
options.add_option("-w", "--warning", 	dest="warning",help="warning limit",  default="800" , type = "int")
options.add_option("-t", "--target", 	dest="target",help="graphite target", default="server.web1.load.load.longterm")
options.add_option("-T", "--time", 	dest="time",help="time in minutes", default="5", type="int")

(options, args) = options.parse_args()

URL=("%s/render/?target=%s&from=-%dminutes&format=json" % ( options.url , options.target , options.time ))

r  = requests.get(URL).json()
i = 0
total = 0

for x in r :
	for d in x['datapoints']: 	
		if d[0] != None:
			total = total + d[0]
		i = i + 1 
avg = total / i 

if avg >= options.critical:
	print "Critical Avg : %d " % avg
	sys.exit(1)
elif avg >= options.warning:
	print "Warning Avg : %d " % avg
	sys.exit(2)
elif avg < options.warning:
	print "OK Avg : %i " % avg
	sys.exit(0)
else:
	print "Unknow"
	sys.exit(3)



