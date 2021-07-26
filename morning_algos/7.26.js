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

function factorial(num){
    if(num == 0){
        return 0
    }
    return num == 1 ? num :  num * factorial(num - 1);
}
console.log(factorial(5))


// BONUS:
function findNthFibNum(n) {
    
}