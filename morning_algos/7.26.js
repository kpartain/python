/*
    Let's practice recursion now!

    factorial(num) -> find the factorial of a number.
    Example: factorial(5) should give us 120, because
    5! = 5 * 4 * 3 * 2 * 1 which is 120

    BONUS: findNthFibNum(n) 
    Find the nth value of the fibonacci sequence.

    Fibonacci sequence:

    0, 1, 1, 2, 3, 5, 8, 13, ... 

    Where the first 2 numbers are 0 and 1, and then each consecutive value is the sum 
    of the previous 2 numbers

    So findNthFibNum(7) would return 8, because 8 is the 7th number in the fibonacci sequence.
*/

// n * n-1 until n is 1
//n should never hit 0 as n*0 = 0
function factorial(num){
    if(num == 0 || num == 1){
        return num 
    } else {
        return num * factorial(num - 1);
    }
    
}
console.log("0:",factorial(0))
console.log("1:",factorial(1))
console.log("2:",factorial(2))
console.log("5:",factorial(5))


// BONUS:
// 0, 1, 1, 2, 3, 5, 8, 13, ... 
//assumes never negative
function findNthFibNum(n) {
    if(n <= 1) {
        return 0;
    } else if (n < 4) {
        return 1;
    } else {
        return (findNthFibNum(n - 1) + findNthFibNum(n -2));
    }
    
}
console.log("0, 1, 1, 2, 3, 5, 8, 13, ... ")
console.log("0:",findNthFibNum(0))
console.log("1:",findNthFibNum(1))
console.log("2:",findNthFibNum(2))
console.log("3:",findNthFibNum(3))
console.log("4:",findNthFibNum(4))
console.log("7:",findNthFibNum(7))
console.log("8:",findNthFibNum(8))