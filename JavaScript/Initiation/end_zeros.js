#!/home/jeff/.local/bin/checkio --domain=js run end-zeros

// Try to find out how many zeros a given number has at the end.
// 
// Input:A positive Int
// 
// Output:An Int.
// 
// 
// END_DESC

import assert from "assert";

function endZeros(value: number): number {
    let nummer = value.toString();
    let counter = 0;
    for (var i = nummer.length -1; i >= 0; i--){
        if (nummer[i] == '0') {
            counter += 1;
        } else {
            return counter;
        }
    }
    return counter;
}

console.log('Example:');
console.log(endZeros(0));

// These "asserts" are used for self-checking
assert.equal(endZeros(0), 1);
assert.equal(endZeros(1), 0);
assert.equal(endZeros(10), 1);
assert.equal(endZeros(101), 0);
assert.equal(endZeros(245), 0);
assert.equal(endZeros(100100), 2);

console.log("Coding complete? Click 'Check' to earn cool rewards!");