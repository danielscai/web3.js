#!/usr/bin/python 

import re
import json 
import requests
from datetime import datetime, timezone, timedelta
from web3 import Web3
from lxml import etree


json_file = "sample.json"
json_file_content = open(json_file,'r').read()

log_result_file = "logResultSample.json"

def read_json_from_file(file_name):
    file_content = open(file_name,'r').read()
    return json.loads(file_content)

last_ok_block = 4623060


def get_block_hight():
    url = 'https://etherscan.io/blocks'
    r = requests.get(url)
    html = etree.HTML(r.text)
    result  = html.xpath('/html/body/div[1]/div[4]/div[1]/div[1]/span[2]')
    info  = result[0]
    string = str(etree.tostring(info))

    match=re.match(r'[^(]+\(#(\d+)', string)
    
    block_hight = match.group(1)
    return block_hight

def request_ether_scan(fromBlock,toBlock):
    host = 'https://api.etherscan.io'
    address = '0xD91E45416bfbBEc6e2D1ae4aC83b788A21Acf583'
    topic0='0x8dd0b145385d04711e29558ceab40b456976a2b9a7d648cc1bcd416161bf97b9'
    apikey='3P1Y527CV18KVXFQD696CMHMQZMUSY8HHB'

    url_pattern = '{host}/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={topic0}&apikey={apikey}'

    url = url_pattern.format(
        host = host,
        address=address,
        fromBlock=fromBlock,
        toBlock=toBlock,
        topic0=topic0,
        apikey=apikey,
    )
    print(url)
    #r =  requests.get(url)
    #return r.json()

def stream_scan():
    block_hight = get_block_hight()
    global last_ok_block
    rjson = request_ether_scan(last_ok_block, block_hight)  
    if rjson['status'] == 1:
        last_ok_block = block_hight


def print_log_bet(result):
    topic = result['topics']
    (event_topic, betID, PlayerAddress, RewardValue) = topic
    p_address = Web3.toChecksumAddress(PlayerAddress)
    print(p_address, Web3.fromWei(int(RewardValue,16), 'ether'))


def print_log_result(result):
    data = result['data']
    topic = result['topics']
    timeStamp = result['timeStamp']
    tz = timezone(timedelta(hours=8))
    bet_time = datetime.fromtimestamp(int(timeStamp,16),tz)

    (event_topic, ResultSerialNumber, BetID, PlayerAddress) = topic
    
    PlayerNumber = data[2::65]
    DiceResult = data[66::129]
    Value = data[130::193]
    Status = data[194::257]
    Proof = data[258::]
    
    p_address = Web3.toChecksumAddress(PlayerAddress)
    print(bet_time.isoformat(), p_address, int(PlayerNumber,16), int(DiceResult,16))



#parsed_json = json.loads(json_file_content)

#results=parsed_json['result']

parsed_log_result = read_json_from_file(log_result_file)
results2= parsed_log_result['result']

#for r in results2:
#    print_log_result(r)
    
#request_ether_scan()
get_block_hight()

#for r in results:
#    print_log_bet(r)
