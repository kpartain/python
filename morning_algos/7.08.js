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
//references https://duncan-mcardle.medium.com/leetcode-problem-5-longest-palindromic-substring-javascript-9c7c7cea0003
//was not able to do without brute force
function longestPalindromicSubstring(str) {
    let longestPalLength = 0;
    let longestPalLeft = 0;
    let longestPalRight = 0;

    var getLongestPalindrome = function (leftPosition, rightPosition) {
        while (
            leftPosition >= 0 &&
            rightPosition < str.length &&
            str[leftPosition] === str[rightPosition]
        ) {
            leftPosition--;
            rightPosition++;
        }
        if (rightPosition - leftPosition > longestPalLength) {
            longestPalLeft = leftPosition + 1;
            longestPalRight = rightPosition - 1;
            longestPalLength = longestPalRight - longestPalLeft + 1;
        }
    };
    for (let i = 0; i < str.length; i++) {
        getLongestPalindrome(i, i + 1);
        getLongestPalindrome(i, i);
        if ((str.length - i) * 2 < longestPalLength) {
            break;
        }
    }
    return str.slice(longestPalLeft, longestPalRight + 1);
}
// const { isPalindrome } = require("./isPalindrome");

const str5 = "what up, daddy-o?";
// const expected1 = "dad";
console.log(longestPalindromicSubstring(str5))

const str6 = "uh, not much";
// const expected2 = "u";
console.log(longestPalindromicSubstring(str6))

const str7 = "Yikes! my favorite racecar erupted!";
// const expected3 = "e racecar e";
console.log(longestPalindromicSubstring(str7))

const str8 = "";
// const expected4 = false;
console.log(longestPalindromicSubstring(str8))

