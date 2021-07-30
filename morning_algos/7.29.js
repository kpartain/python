/* 
  recursively find the lowest common multiple between two numbers
  "A common multiple is a number that is a multiple of two or more integers. 
  The common multiples of 3 and 4 are 0, 12, 24, .... 
  The least common multiple (LCM) of two numbers is the smallest number (not zero) 
  that is a multiple of both."
  
  Try writing two columns of multiples as a starting point:
  starting with 15 and 25 and keep writing their multiples until you find the lowest common one
  then turn this in to a step by step instruction
  15 25
  30 50
  45 75
  60
  75
  75 is the first common
*/

/**
 * Add params if needed for recursion
 * Finds the lowest common multiple of the two given ints.
 * @param {number} a
 * @param {number} b
 * @returns {number} The lowest common multiple of the given ints.
 */
function lowestCommonMult(a, b, largestPlusLargest = 0) {
    //edge cases
    if(a == b) {
        return a;
    }
    let largest = 0;
    let smallest = 0;
    //find the bigger & smaller number
    if (a > b) {
        largest = a;
        smallest = b;
    } else {
        largest = b;
        smallest = a;
    }
    largestPlusLargest += largest;
    if(largestPlusLargest % smallest != 0) {
        return lowestCommonMult(a, b, largestPlusLargest)
    } else {
       return largestPlusLargest 
    }
    
}

const num1A = 1; //1
const num1B = 1; //1
const expected1 = 1;
var test1 = lowestCommonMult(num1A, num1B);
console.log(test1);

const num2A = 5; //5, 10, 15, 20
const num2B = 10; //10, 20, 30
const expected2 = 10;
var test2 = lowestCommonMult(num2A, num2B);
console.log(test2);

const num3A = 10; //10, 20, 30
const num3B = 5; //5, 10, 15, 20
const expected3 = 10;
var test3 = lowestCommonMult(num3A, num3B);
console.log(test3);

const num4A = 6; // 6, 12, 18, 24
const num4B = 8; // 8, 16, 24
const expected4 = 24;
var test4 = lowestCommonMult(num4A, num4B);
console.log(test4);

const num5A = 15; //15, 30, 45, 60, 75
const num5B = 25; //24, 50, 75
const expected5 = 75;
var test5 = lowestCommonMult(num5A, num5B);
console.log(test5);

  
// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129

/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/
// output list order does not matter

/**
 * Add params if needed for recursion
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
 */
function binaryStringExpansion(str, returnArray = [], currentStr = str) {
    if(str.length == 0) {
        return false;
    } else {
        for(var i = 0; i < currentStr.length; i++) {
            if(currentStr[i] == "?") {
                currentStr[i] = 1;
            }
        }
        return binaryStringExpansion(str, returnArray, currentStr)
    }
    return returnArray;
}
const str1 = "1?0?";
const expectedResult = ["1000", "1001", "1100", "1101"];
var theResult = binaryStringExpansion(str1)
console.log(theResult)