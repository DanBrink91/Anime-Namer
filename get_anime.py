import requests
from lxml import etree

MAX_ID = 16090
def grab_stuff(url):
	r = requests.get(url)

	return r.content

# Allows up to 50 IDs seperated by /
API_URL = "http://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime=%s"
names = []
for i in xrange(0, MAX_ID, 50):
	ids = map(str, range(i, i+50))
	try:
		root = etree.fromstring(grab_stuff(API_URL % ("/").join(ids)))
	except:
		continue
	names.extend([child.get("name").encode('utf-8') for child in root if child.get("name") is not None])
with open("anime.txt", "w") as f:
	f.write("\n".join(names))