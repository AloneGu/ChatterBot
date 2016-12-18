import requests

while(True):
    print 'A:',
    s = raw_input()
    url = 'http://101.200.49.134:8003/get/{}'.format(s)
    res = requests.get(url)
    print 'B:',
    print res.text
