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
console.log(web3.version.ethereum);
console.log(web3.eth.mining);
//console.log(web3.eth.fromWei(web3.eth.gasPrice.toString(10)));


web3.eth.getAccounts(function (error, result){
    console.log(result)
}
)

var abi = [{"constant":true,"inputs":[{"name":"a","type":"uint256"}],"name":"multiply","outputs":[{"name":"d","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]
var c = web3.eth.contract(abi);
var contract = c.at('0xb1e23ce2dd190d30e7c0d4f5907d43814d8c96e8');

result = contract.multiply(7)
console.log("print result")
console.log(result)
