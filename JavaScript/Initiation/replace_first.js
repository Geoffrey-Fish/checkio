#!/home/jeff/.local/bin/checkio --domain=js run replace-first

// In a given array the first element should become the last one. An empty array or array with only one element should stay the same.
// 
// 
// 
// Input:Array.
// 
// Output:Array.
// 
// 
// END_DESC

import assert from "assert";

function replaceFirst(values: number[]): number[] {
    // your code here
    return undefined;
}

console.log('Example:');
console.log(replaceFirst([1, 2, 3, 4]));

// These "asserts" are used for self-checking
assert.deepEqual(replaceFirst([1, 2, 3, 4]), [2, 3, 4, 1]);
assert.deepEqual(replaceFirst([1]), [1]);
assert.deepEqual(replaceFirst([]), []);

console.log("Coding complete? Click 'Check' to earn cool rewards!");