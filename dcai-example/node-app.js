#!/usr/bin/env node

var Web3 = require('../index.js');
var web3 = new Web3();

web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));

var coinbase = web3.eth.coinbase;
console.log(coinbase);

var balance = web3.eth.getBalance(coinbase);
console.log(balance.toString(10));

//var balance = new BigNumber('131242344353464564564574574567456');
console.log('add 21 to balance');
var new_balance = balance.plus(21).toString(10);
console.log(new_balance);
console.log(web3.version.api);
console.log(web3.version.network);
