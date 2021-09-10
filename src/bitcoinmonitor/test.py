import datetime
import logging
import sys
import requests
from typing import Any, Dict, List, Optional

def get_cardano_data() -> List[Dict[str, Any]]:
    url = 'https://api.coincap.io/v2/assets/cardano'
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        print("error")
        sys.exit(1)
    data = r.json().get('data', [])
    time = r.json().get('timestamp', [])
    composite = [data, time]
    return composite

def get_utc_from_unix_time(
    unix_ts: Optional[Any], second: int = 1000
) -> Optional[datetime.datetime]:
    return (
        datetime.datetime.utcfromtimestamp(int(unix_ts) / second)
        if unix_ts
        else None
    )

def get_exchange_data() -> List[Dict[str, Any]]:
    url = 'https://api.coincap.io/v2/exchanges'
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get('data', [])

def get_assets_data() -> List[Dict[str, Any]]:
    url = 'https://api.coincap.io/v2/assets'
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get('data', [])

#data = get_cardano_data()
#print(data)
#time = get_utc_from_unix_time(data[1])
#cardanoDict = data[0]
#cardanoDict['update_dt'] = time
#print (cardanoDict)

data = get_assets_data()
#insert a timestamp. note: it will be off by very small fractions of seconds due to latency
timeInsert = datetime.datetime.now()
for d in data:
    d['update_dt'] = timeInsert
print(data)