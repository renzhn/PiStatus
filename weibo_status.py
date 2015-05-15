import json
import requests

from weibo import Client

def sizeof_fmt(num, suffix='B'):
    if not isinstance(num, int):
        num = int(num)
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


TOKEN = '{"expires_at": 1432321199, "access_token": "2.00FQbohB0163r16466e4dde5sLRuVB", "remind_in": "646258", "uid": "1563574905"}'
OPENWRT_TOKEN = 'edd6c6c96d057ff458770ae907d227e9'


API_KEY = '308244242'
API_SECRET = '4532eb6062e29c14707cc8527bc9ec4f'
REDIRECT_URI = 'http://tools.iadright.com'
OPENWRT_URL = 'http://miwifi.com/cgi-bin/luci/;stok=' + OPENWRT_TOKEN + '/api/misystem/status'

c = Client(API_KEY, API_SECRET, REDIRECT_URI, json.loads(TOKEN)) 

tempfile = open("/sys/class/thermal/thermal_zone0/temp")
thetext = tempfile.read()
tempfile.close()
temperature = float(thetext)
temperature = str(round(temperature / 1000, 1))
temperature_status = 'RPi Temp:' + temperature + "℃"

r = requests.get(OPENWRT_URL)
json = r.json()
downspeed = sizeof_fmt(json['wan']['downspeed'], 'B/s')
upspeed = sizeof_fmt(json['wan']['upspeed'], 'B/s')
download = sizeof_fmt(json['wan']['download'])
upload = sizeof_fmt(json['wan']['upload'])
count_all = str(json['count']['all'])
count_online = str(json['count']['online'])

router_status = 'WAN D:' + downspeed + ' U:' + upspeed + ' Total:' + download + '/' + upload + ' Clients:' + count_online + '/' + count_all

status = temperature_status + ' ' + router_status

print(status)

c.post('statuses/update', status=status)
