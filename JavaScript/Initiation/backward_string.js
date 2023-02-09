#!/home/jeff/.local/bin/checkio --domain=js run backward-string

// You should return a given string in reverse order.
// 
// Input:A string.
// 
// Output:A string.
// 
// 
// END_DESC

import assert from "assert";

function backwardString(value: string): string {
    var newString = ''
    for (var i = value.length - 1; i >= 0; i--) { 
        newString += value[i]};
    return newString;
}

console.log('Example:');
console.log(backwardString('val'));

// These "asserts" are used for self-checking
assert.equal(backwardString('val'), 'lav');
assert.equal(backwardString(''), '');
assert.equal(backwardString('ohho'), 'ohho');
assert.equal(backwardString('123456789'), '987654321');

console.log("Coding complete? Click 'Check' to earn cool rewards!");