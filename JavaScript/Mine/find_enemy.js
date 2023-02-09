#!/home/jeff/.local/bin/checkio --domain=js run find-enemy

// Find the distance and directions to an enemy in a HEX-grid.
// 
// HEX-grid
// 
// 
// 
// Absolute Directions
// 
// 
// 
// Relative Directions
// 
// * if your absolute directions are "N"
// 
// 
// 
// Input:Three arguments: your current coordinates, your current absolute directions, and enemy's coordinates.
// 
// Output:A list with relative directions and distance to the enemy.
// 
// 
// 
// 
// How it is used:War-game design using hex-grid.
// 
// 
// 
// Precondition:
// 'A1' ≤ coordinates ≤ 'Z9'.
// direction in ('N', 'NE', 'SE', 'S', 'SW', 'NW').
// your coordinates ≠ enemy's coordinates.
// 
// 
// END_DESC

import assert from "assert";

function findEnemy(you: string, dir: string, enemy: string): [string, number] {
    // your code here
    return ['', 0];
}

console.log('Example:');
console.log(findEnemy('G5', 'N', 'G4'));

// These "asserts" are used for self-checking
assert.deepEqual(findEnemy('G5', 'N', 'G4'), ['F', 1]);
assert.deepEqual(findEnemy('G5', 'N', 'I4'), ['R', 2]);
assert.deepEqual(findEnemy('G5', 'N', 'J6'), ['R', 3]);
assert.deepEqual(findEnemy('G5', 'N', 'G9'), ['B', 4]);
assert.deepEqual(findEnemy('G5', 'N', 'B7'), ['L', 5]);
assert.deepEqual(findEnemy('G5', 'N', 'A2'), ['L', 6]);
assert.deepEqual(findEnemy('G3', 'NE', 'C5'), ['B', 4]);
assert.deepEqual(findEnemy('H3', 'SW', 'E2'), ['R', 3]);
assert.deepEqual(findEnemy('A4', 'S', 'M4'), ['L', 12]);

console.log("Coding complete? Click 'Check' to earn cool rewards!");