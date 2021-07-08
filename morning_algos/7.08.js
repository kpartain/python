/* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
        - palindrome = string that is same forwards and backwards
    
    Do not ignore spaces, punctuation and capitalization
*/

function isPalindrome(str) {
    var myNonMatchCount = 0;
    var rightCounter = str.length - 1;
    var returnBoolean = false;
    for(var left = 0; left < rightCounter; left++) {
        if(str.charAt(left) != str.charAt(rightCounter)) {
            myNonMatchCount++;
        }
        rightCounter--;
    }
    if(myNonMatchCount == 0) {
        returnBoolean = true;
    } else {
        returnBoolean = false;
    }
    return returnBoolean;
}

const str1 = "a x a";
// const expected1 = true;
console.log(isPalindrome(str1));

const str2 = "racecar";
// const expected2 = true;
console.log(isPalindrome(str2));

const str3 = "Dud";
// const expected3 = false;
console.log(isPalindrome(str3));

const str4 = "oho!";
// const expected4 = false;
console.log(isPalindrome(str4));




/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

// const { isPalindrome } = require("./isPalindrome");

// const str1 = "what up, daddy-o?";
// const expected1 = "dad";

// const str2 = "uh, not much";
// const expected2 = "u";

// const str3 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";

// const str4 = "";
// const expected4 = false;

function longestPalindromicSubstring(str) {

}