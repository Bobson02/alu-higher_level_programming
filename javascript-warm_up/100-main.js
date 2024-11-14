#!/usr/bin/node

const myModule = require('./100-let_me_const');

console.log(myModule.myVar);
myModule.myVar = 333; // Modify the value of myVar
console.log(myModule.myVar);
