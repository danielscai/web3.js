#!/usr/bin/env node

var Web3 = require('../index.js');
var web3 = new Web3();

web3.setProvider(new web3.providers.HttpProvider('http://localhost:8546'));

//var coinbase = web3.eth.coinbase;
//console.log(web3.fromWei(web3.eth.getBalance(contract_address).toString(10)));
console.log(web3.eth.syncing);

