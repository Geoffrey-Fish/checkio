#!/home/jeff/.local/bin/checkio --domain=js run cut-sentence

// Your task in this mission is to truncate a sentence to a length, that does not exceed a  given number of characters.
// 
// If the given sentence already is short enough you don't have to do anything to it, but  if it needs to be truncated the omission must be indicated by concatenating an ellipsis  ("...") to the end of the shortened sentence.
// 
// The shortened sentence can contain complete words and spaces.
// It must neither contain truncated words nor trailing spaces.
// The ellipsis has been taken into account for the allowed number of characters, so it  does not count against the given length.
// 
// Input:Two arguments:one-line sentence as a stringmax length of the truncated sentence as an int
// 
// Output:The shortened sentence plus the ellipsis (if required) as a  one-line string.
// 
// Precondition:
// line.startsWith(' ') === false0<line.length ≤ 790<length ≤ 76all chars in line are English Letters and/or spaces
// 
// 
// END_DESC

import assert from "assert";

function cutSentence(line: string, length: number): string {
    // your code here
    return line;
}

console.log('Example:');
console.log(cutSentence('Hi my name is Alex', 8));

// These "asserts" are used for self-checking
assert.equal(cutSentence('Hi my name is Alex', 8), 'Hi my...');
assert.equal(cutSentence('Hi my name is Alex', 4), 'Hi...');
assert.equal(cutSentence('Hi my name is Alex', 20), 'Hi my name is Alex');
assert.equal(cutSentence('Hi my name is Alex', 18), 'Hi my name is Alex');

console.log("Coding complete? Click 'Check' to earn cool rewards!");