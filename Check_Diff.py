#testing json queries
import urllib.parse
import requests
import time

chainz_api = 'https://chainz.cryptoid.info/xjo/api.dws?'

check = 'summary'

url = chainz_api + urllib.parse.urlencode({'q': check})

json_data = requests.get(url).json()

zet_coin_raw = json_data['zet']['diff']
xjo_coin_raw = json_data['xjo']['diff']
v_coin_raw = json_data['vcn']['diff']

#remove dec
v_coin = int(v_coin_raw)
xjo_coin = int(xjo_coin_raw)
zet_coin =int(zet_coin_raw)


print("Vcoin Difficulty: " + str(v_coin))
print("JouleCoin Difficulty: " + str(xjo_coin)) 
print("Zetacoin Difficulty: " + str(zet_coin))

time.sleep(10)
