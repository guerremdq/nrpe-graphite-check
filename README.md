nrpe-graphite-check
===================

Nagios Alert for graphite targets

Install requests

	pip install requests

Run the script:

	python graphite-check.py  -u http://graphite.foo.com/ -t foo.db.maxConnections.size  -w 40 -c 70
