from bs4 import BeautifulSoup
import urllib2
import json

ALI_BANKS = 'http://ab.alipay.com/i/yinhang.htm'

try:
    response = urllib2.urlopen(ALI_BANKS)
except urllib2.HTTPError, e:
    print "HTTP Error %s : %s" % (e.code, e.reason)
    system.exit(1)
except urllib2.URLError, e:
    print "Unable to connect the remote server."
    system.exit(1)

content = response.read()

soup = BeautifulSoup(content)
spans = soup.find_all("span", class_="icon")
# banks = {}
# for span in spans:
#     banks[span['class'][1]] = span.text

banks = { span['class'][1] : span.text for span in spans }

print json.dumps(banks, ensure_ascii=False, indent=2)
print "total : %d" % len(banks)