/*
    Key focus of the day? Removing a node from the middle of a SLL.
    Let's think about this. If we have:
    H: 5 -> 4 -> 3 -> 2 -> 1 ->

    And we want to remove the node with a value of 3, how might we do this?
    The end result should look something like:
    H: 5 -> 4 -> 2 -> 1 ->

    Well in that case, all we really need to do is move 4's .next to be 3's .next, right?
    Right.

    With that in mind...

    Two challenges today!

    Challenge 1: moveMinToFront()
    Write a method that will find the node with the smallest value, and move it to the front. 
    EXAMPLE:
    H: 5 -> 3 -> 6 -> 1 -> 2 ->
    would become
    H: 1 -> 5 -> 3 -> 6 -> 2 -> 

    Challenge 2: moveMaxToBack()
    Write a method that will find the node with the largets value, and move it to the back.
    EXAMPLE:
    H: 1 -> 7 -> 11 -> 2 -> 18 -> 4 ->
    would become
    H: 1 -> 7 -> 11 -> 2 -> 4 -> 18 ->
*/

const { compositionDependencies } = require("mathjs");

class SLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLList {
    constructor(){
        this.head = null;
    }

    addToFront(value) {
        var newHead = new SLNode(value);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    addToBack(value) {
        if(this.head == null) {
            this.addToFront(value);
            return this;
        }

        var newNode = new SLNode(value);
        var runner = this.head;

        while(runner.next != null) {
            runner = runner.next;
        }

        runner.next = newNode;
        return this;
    }

    contains(value) {
        if(this.head == null) {
            return false;
        }

        var runner = this.head;

        while(runner != null) {
            if(runner.value == value) {
                return true;
            } else { 
                runner = runner.next;
            }
        }

        return false;
    }

    removeFront() {
        if(this.head == null) {
            return false;
        }

        var nodeToRemove = this.head;
        this.head = nodeToRemove.next;
        nodeToRemove.next = null;

        return nodeToRemove;
    }

    removeBack() {
        if(this.head == null) {
            return false;
        } else if(this.head.next = null) {
            return this.removeFront();
        }

        var lagger = null; 
        var leader = this.head; 
        while(leader.next != null) {
            lagger = leader;
            leader = leader.next;
        }

        lagger.next = null;
        return leader;
    }

    moveMinToFront(){
        //edge case - null SLL
        if(this.head == null) {
            return false;
        }
        //edge case = head but no child nodes
        if(this.head != null && this.head.next == null) {
            return true;
        }
        //instantiate a variable to compare - if the comparison is less, reassign it
        //we start it at the highest possible so the first number smaller is assigned 
        var theMinimum = Number.MAX_VALUE;
        var runner = this.head.next;
        while(runner.next != null) {
            //assume we will not have two matching lowest numbers 
            if(runner.value < theMinimum) {
                theMinimum = runner.value;
            }
            runner = runner.next;
        }
        console.log("Minimum Value found:", theMinimum);
        var first = this.head;
        var replaces = first.next;
        while(replaces != null){
            replaces.value = first.value;
            first = replaces;
            replaces = replaces.next;
        }
        this.head.value = theMinimum;
        return this;
    }

    moveMaxToBack(){
        //edge case - null SLL
        if(this.head == null) {
            return false;
        }
        //edge case = head but no child nodes
        if(this.head != null && this.head.next == null) {
            return true;
        }
        //instantiate a variable to compare - if the comparison is more, reassign it
        //we start it at the lowest possible so the first number larger is assigned 
        var theMaximum = Number.MIN_VALUE;
        var runner = this.head.next;
        while(runner.next != null) {
            //assume we will not have two matching lowest numbers 
            if(runner.value > theMaximum) {
                theMaximum = runner.value;
            }
            runner = runner.next;
        }
        console.log("Maximum Value found:", theMaximum);
        runner = this.head;
        while(runner.next != null) {
            if(runner.value == theMaximum) {
                runner.value = runner.next.value;
            }
            runner = runner.next;
        }
        runner.next = theMaximum;
        return this;
    }

    printAll(){
        var potato = this.head;
        while(potato.next != null) {
            console.log(potato);
            potato = potato.next;
        }
    }
}
// Challenge 1: moveMinToFront()
// H: 5 -> 3 -> 6 -> 1 -> 2 -> would become H: 1 -> 5 -> 3 -> 6 -> 2 -> 
var test1 = new SLList();
test1.addToFront(2).addToFront(1).addToFront(6).addToFront(3).addToFront(5);
console.log("========================BEFORE========================");
console.log(test1);
test1.moveMinToFront()
console.log("=*=*=*=*=*==============AFTER==============*=*=*=*=*=");
console.log(test1);

// Challenge 2: moveMaxToBack()
// H: 1 -> 7 -> 11 -> 2 -> 18 -> 4 -> would become H: 1 -> 7 -> 11 -> 2 -> 4 -> 18 ->
// var test2 = new SLList();
// test2.addToFront(4).addToFront(18).addToFront(2).addToFront(11).addToFront(7).addToFront(1);
// console.log("========================BEFORE========================");
// console.log(test2);
// test2.moveMaxToBack();
// console.log("=*=*=*=*=*==============AFTER==============*=*=*=*=*=");
// console.log(test2);
// test2.printAll();