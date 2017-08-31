#!/usr/bin/env node

var Web3 = require('../index.js');
var web3 = new Web3();

web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));

web3.eth.getTransaction(process.argv[2],function (error, result){
    console.log(result);
    }
    );
