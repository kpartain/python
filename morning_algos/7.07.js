//string encode
//all the letters will be together

const { number } = require("mathjs");

//if the string is empty, returm empty string
var str1 = ""; //should return ""
//if the result is equal to or longer than orginal string, return original
var str2 = "bbcc"; //return "bbcc"
//otherwise return the letter, the number of times it appears, then the next one
//if there is only one, do not put the 1
var str3 = "aaaabbcddda"; //return a4b2c1d3a

// function stringEncode(str) {
//     var returnString = "";
//     if (str === "") {
//         returnString = "";
//     } else {
//         var letter = "";
//         for (var i = 0; i < str.length; i++) {
//             count = 0;
//             letter = str[i];
//             count++;
//             while (str[i + 1] == letter) {
//                 count++;
//                 i++;
//             }
//             if (count == 1) {
//                 returnString += letter;
//             } else if (count > 1) {
//                 returnString += letter;
//                 returnString += count.toString();
//             }
//         }
//         var originalLength = str.length;
//         var newStringLength = returnString.length;
//         if (newStringLength >= originalLength) {
//             returnString = str;
//         } else {
//             returnString = returnString;
//         }
//     }
//     return returnString;
// }

//string decode
//return the original string
function stringDecode(str) {
    var returnString = "";
    var hasANumber = false;
    for (var i = 0; i < str.length; i++) {
        if (!isNaN(str.charAt(i))) {
            hasANumber = true;
        }
    }
    //if the string does not have a number, return string is string, return it there
    if (hasANumber == false) {
        returnString = str;
        return returnString;
    //otherwise if it does have a number...
    } else {
        for (var i = 0; i < str.length; i++) {
            var thisChar = str.charAt(i);
            var nextChar = str.charAt(i + 1);
            //if the next character is a number, add it that many times
            if (!isNaN(nextChar)) {
                for (var j = 0; j < parseInt(nextChar); j++) {
                    returnString += str.charAt(i);
                }
                i++;
            //otherwise add it once
            } else {
                returnString += thisChar;
            }
        }
    }
    return returnString;
}

var str4 = ""; //returns ""
var return4 = stringDecode(str4);
console.log(return4);
//check if it has numbers, if not, return itself
var str5 = "abcc"; //"abcc".
var return5 = stringDecode(str5);
console.log(return5);
//otherwise check at the number to return that many of the letter at i
var str6 = "a3bcd3"; // "aaabbcddd"
var return6 = stringDecode(str6);
console.log(return6);

//need to consider if there is a 10, 11, 100, etc. continue checking until not a number

