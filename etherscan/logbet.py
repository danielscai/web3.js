#!/usr/bin/python 

import json 
from web3 import Web3


json_file = "sample.json"
json_file_content = open(json_file,'r').read()



def print_log_bet(result):
    topic = result['topics']
    (event_topic, betID, PlayerAddress, RewardValue) = topic
    p_address = Web3.toChecksumAddress(PlayerAddress)
    print(p_address, Web3.fromWei(int(RewardValue,16), 'ether'))

parsed_json = json.loads(json_file_content)

results=parsed_json['result']

for r in results:
    print_log_bet(r)
