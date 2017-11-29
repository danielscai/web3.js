#!/usr/bin/env node

const fs = require('fs');

var log_result_file = "logResultSample.json";

fs.readFile(log_result_file,'UTF-8', (error,data)=>{
	if (error){
		return console.log(error);
	}
	json_data = JSON.parse(data);
	console.log(json_data.status);
	results = json_data.result;
	for ( i in results) {
		r = results[i]
		rdata = r.data
		topics = r.topics;
		timeStamp = r.timeStamp;
		event_topic = topics[0];
		ResultSerialNumber = topics[1];
		BetID = topics[2];
		PlayerAddress = topics[3];
		PlayerNumber = rdata.slice(2,65);
    		DiceResult = rdata.slice(66,129);
    		Value = rdata.slice(130,193);
    		Status = rdata.slice(194,257);
    		Proof = rdata.slice(258);
		console.log(PlayerAddress, PlayerNumber, DiceResult);
	}
	//result.forEach( (e,data) => {
		//console.log(data.address);
	//})

}
);
