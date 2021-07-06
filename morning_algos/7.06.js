//create a function that, given a string returns the acronym
//first letter of each word capitalized
var testString = "this is a test";
var testStringSpace = " oh no, a Space";
function stringToAcronym(str){
    var newString = "";
    //this does not account for index 0 being a non-alphabet character
    for(var i = 0; i < testString.length; i++) {
        if(str[i] == " ") {
            newString += str[i+1].toUpperCase();
            i++;
        }
            // else do nothing
    }
    return newString;
}
console.log(stringToAcronym(testString));
console.log(stringToAcronym(testStringSpace));

//create a function that, given a string, returns a new string that is reversed
var testString2 = "this is another test";
function reverseString(str) {
    var newString = "";
    for(var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}
console.log("ANSWER: " + reverseString(testString2));