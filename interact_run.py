import requests

while(True):
    s = raw_input()
    #print s
    url = 'http://0.0.0.0:8003/get/{}'.format(s)
    #print url
    res = requests.get(url)
    print res.text