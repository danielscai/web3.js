#!/usr/bin/env node

var contract_address = '0xa22cd99692127cb2784bf3d76b029b293e17bea6';
var Web3 = require('../index.js');
var web3 = new Web3();

web3.sha3("event LogBet(bytes32 indexed BetID, address indexed PlayerAddress, uint indexed RewardValue, uint ProfitValue, uint BetValue, uint PlayerNumber);")
