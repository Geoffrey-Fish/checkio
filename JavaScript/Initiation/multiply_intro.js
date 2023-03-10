#!/home/jeff/.local/bin/checkio --domain=js run multiply-intro

// (At the top right of the mission description there is always a list of available translations)
// 
// This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO and how to get the most out of solving them. As you solve missions more stations become available to you, containing more complex missions.
// 
// This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
// 
// Input:Two arguments. Both are of type int.
// 
// Output:Int.
// 
// How does it work?
// 
// When you start working on the problem, the initial code consists of an “empty” function (which you will need to populate with your code). Asserts are included in the code to check whether the function performs as expected. Pay attention that your function returns values, and does not print them.In order to do this, usethe return commandinstead ofthe console.log function.
// 
// The asserts in the code can be used in order to check your solution by pressing the “Run” button (). CheckiO also uses several additional tests in order to check your solution when you click the “Check” button ().
// 
// If the solution didn’t pass the internal tests, the right panel will display an error message containing the following 3 items:
// 
// Fail- shows how your function was called.Your Result- shows what it returned.Right Result- what it should’ve returned.To solve the task the “empty” function must be replaced with the following code:
// 
// 
// function multTwo(a, b) {
//     return a*b;
// }
// Try to click “Check” button now.
// 
// If the solution passes all the tests, the congratulations should appear on the right panel along with a suggestion for the following actions (yes, this is not the end of the story):
// 
// View other solutions- when the task is solved, you can access the solutions of other players, which are divided into categories.Publish your solution- publish your own solution.Next Mission- go to the next mission.It is recommended you go through the solutions of other players before publishing your own.
// 
// Last but not least, some tasks have a list of hints for helping you solve them at the end. But since in this task we’ve already described to you how to solve it, in hints we’ll instead add some interesting facts about CheckiO.
// 
// 
// END_DESC

import assert from "assert";

function multTwo(a: number, b: number): number {
    // your code here
    return a*b;
}

console.log("Example:");
console.log(multTwo(3, 2));

// These "asserts" are used for self-checking
assert.equal(multTwo(3, 2), 6);
assert.equal(multTwo(0, 1), 0);

console.log("Coding complete? Click 'Check' to earn cool rewards!");