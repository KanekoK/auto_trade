# レートの取得

base_domain = MODE.get('production')
url_base = 'https://{}/v1/candles?'.format(base_domain)
url = url_base + 'instrument={}&'.format(currency_pair.name) + \
        'count=5000' +\
        'candleFormat=midpoint&' +\
        'granularity={}'.format(granularity.name) +\
        'dailyAlignment=0&' +\
        'alignmentTimezone=Asia%2FTokyo&' +\
        'start={}T00%3A00%3A00Z'.format(start)

response = requests_api(url)

def requests_api(url, payload=None):
    auth = 'Bearer {}'.format(get_password('OandaRestAPIToken'))
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
                'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0',
                'Content-type': 'application/json; charset=utf-8',
                'Authorization': auth}

    if payload:
        requests.adapters.DEFAULT_RETRIES = 2
        response = requests.post(url, headers=headers, date=payload, timeout=10)
    else:
        requests.adapters.DEFAULT_RETRIES = 2
        response = requests.get(url, headers=headers, timeout=10)
    print 'REQUEST_API: {}'.format(url)
    return response
