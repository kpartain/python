//create a function that, given a string returns the acronym
//first letter of each word capitalized
var testString = "this is a test"
function stringToAcronym(str){
    var newString = "";
    newString += str[0].toUpperCase();
    for(var i = 1; i < testString.length; i++) {
        if(str[i] == " ") {
            newString += " ";
            newString += str[i+1].toUpperCase();
            i++;
        } else {
            newString += str[i];
        }
    }
    return newString;
}
console.log(stringToAcronym(testString));
//create a function that, given a string, returns a new string that is reversed
