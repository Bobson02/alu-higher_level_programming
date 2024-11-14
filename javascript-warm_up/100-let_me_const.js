#!/usr/bin/node
const myModule = require('./100-variable_declare.js');
console.log(myModule.myVar);
myModule.myVar = 333; // Modify the value of myVar
console.log(myModule.myVar);
