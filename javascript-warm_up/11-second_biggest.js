#!/usr/bin/node
// Get arguments, excluding the first two (node and script path)
const args = process.argv.slice(2).map(Number);
// Check if there are less than two numbers
if (args.length <= 2) {
  console.log(0);
} else {
  // Sort arguments in descending order and remove duplicates
  const sortedArgs = [...new Set(args)].sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}
