from weibo import Client
from datetime import datetime

API_KEY = '308244242'
API_SECRET = '4532eb6062e29c14707cc8527bc9ec4f'
REDIRECT_URI = 'http://tools.iadright.com'

c = Client(API_KEY, API_SECRET, REDIRECT_URI)
print(c.authorize_url)
c.set_code(input('Please input token:'))
print(c.token)
