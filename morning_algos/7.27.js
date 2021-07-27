/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

function binarySearch(sortedNums, searchNum) {
  var lastIndex = sortedNums.length - 1
  // BASE CASE
  //if we have an empty array or the last value is lower than search, false
  if (sortedNums.length == 0 || sortedNums[lastIndex] < searchNum){
      return false;
  }
  var startIndex = 0
  var middleIndex = Math.floor(sortedNums.length/2)
  //if any index variable is the searchnum, return true{
  if(sortedNums[startIndex] == searchNum || sortedNums[middleIndex] == searchNum || sortedNums[lastIndex] == searchNum) {
      return true;
  }
  // RECURSIVE CALL
  if(sortedNums[middleIndex] > searchNum){
      //go backwards
      while(sortedNums.includes(sortedNums[middleIndex])){
          sortedNums.pop();
      }
      return binarySearch(sortedNums, searchNum)
  } else {
      //go forwards
      while(sortedNums.includes(sortedNums[middleIndex])){
          sortedNums.shift();
      }
      return binarySearch(sortedNums, searchNum)
  }
  return false;
}

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
console.log(binarySearch(nums1, searchNum1));
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
console.log(binarySearch(nums2, searchNum2));
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
console.log(binarySearch(nums3, searchNum3));
const expected3 = true;