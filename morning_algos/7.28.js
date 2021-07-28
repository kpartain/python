/*
    reverse(various parameters here???) --> write a method that will reverse the order of the singly linked list.

    Input: H: 5 -> 4 -> 3 -> 2 -> 1 -> 
    Output: H: 1 -> 2 -> 3 -> 4 -> 5 ->
*/

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
        if(this.head == null || this.head.next == null) {
            return this;
        }

        var minPrev = null; 
        var min = this.head; 

        var lagger = null;
        var leader = this.head;

        while(leader != null) {
            if(leader.value < min.value) {
                min = leader;
                minPrev = lagger;
            }

            lagger = leader;
            leader = leader.next;
        }

        if(min != this.head) {
            minPrev.next = min.next;
            min.next = this.head;
            this.head = min;
        }
        return this;
    }

    moveMaxToBack(){
        if(this.head == null || this.head.next == null) {
            return this;
        }
        var maxPrev = null;
        var max = this.head;

        var lagger = null;
        var leader = this.head;

        while(leader != null) {
            if(leader.value > max.value) {
                max = leader;
                maxPrev = lagger;
            }

            lagger = leader;
            leader = leader.next;
        }
        if(max = this.head) {
            this.head = max.next;
        } else {
            maxPrev.next = max.next;
        }
        lagger.next = max;
        max.next = null;
        return this;
    }

    prependValue(valueToFind, newValue){
        if(this.head == null) {
            return false;
        } else if (this.head.value == valueToFind){
            return this.addToFront(newValue);
        }

        var walker = null;
        var runner = this.head;

        while(runner != null) {
            if(runner.value == valueToFind){
                var newNode = new SLNode(newValue);
                newNode.next = runner;
                walker.next = newNode;
                return this;
            }
            walker = runner;
            runner = runner.next;
        }
        return false;
    }

    appendValue(valueToFind, newValue){
        if(this.head == null) {
            return false;
        }
        var runner = this.head;
        while(runner != null) {
            if(runner.value == valueToFind){
                var newNode = new SLNode(newValue);
                newNode.next = runner.next;
                runner.next = newNode;
                return this;
            }
            runner = runner.next;
        }
        return false;
    }

    removeNegatives(){
        if(this.head == null) {
            return this;
        }

        while(this.head != null && this.head.value < 0) {
            this.head = this.head.next;
        }

        if(this.head == null) {
            return this;
        }

        var walker = this.head;
        var runner = walker.next;

        while(runner != null) {
            if(runner.value < 0){
                walker.next = runner.next;
                runner = runner.next;
            } else {
                walker = runner;
                runner = runner.next;
            }
        }

        return this;
    }

    secondToLastValue(){
        if(this.head == null || this.head.next == null) {
            return false;
        }

        var walker = null;
        var runner = this.head;
        while(runner.next != null) {
            walker = runner;
            runner = runner.next;
        }

        return walker.value;
    }

    isCircular() {
        if(this.head == null) {
            return false;
        }
        var cap = this.head;
        var sam = this.head;

        while(cap != null && cap.next != null && cap.next.next) {
            cap = cap.next.next;
            sam = sam.next;

            if(cap == sam) {
                return true;
            }
        }

        return false;
    }

    breakCircular(){
        if(this.head == null || this.head.next == null) {
            return false;
        }

        var walker = this.head;
        var runner = this.head;

        while(walker != runner) {
            if(runner == null || runner.next == null) {
                return this;
            }

            walker = walker.next;
            runner = runner.next.next;
        }
        
        walker = this.head;

        while(runner.next != walker.next){
            walker = walker.next;
            runner = runner.next;
        }
        runner.next = null;
        return this;
    }

    printAll(){
        var string = "Current: "
        var potato = this.head;
        while(potato.next != null) {
            string += potato.value + ", "
            potato = potato.next;
        }
        string += potato.value + ".";
        console.log(string);
    }

    findLastNode(){
        var lastNode = null;
        var leader = this.head.next;
        while(leader.next != null) {
            leader = leader.next;
        }
        lastNode = leader;
        return lastNode;
    }

    reverse() {
    //edge cases
        //if list is empty
        if(this.head == null || this.head.next == null) {
            return this;
        }
    //standard cases
        var leftNode = null;
        var middleNode = this.head;
        var rightNode = this.head.next;
        while(middleNode.next != null) {
            middleNode.next = leftNode;
            leftNode = middleNode;
            middleNode = rightNode;
            rightNode = rightNode.next;
        }
        this.head = middleNode;
        middleNode.next = leftNode;
        return this;
    }
        
        
}

// Input: H: 5 -> 4 -> 3 -> 2 -> 1 -> 
// Output: H: 1 -> 2 -> 3 -> 4 -> 5 ->
var testlist = new SLList();
testlist.addToBack(5).addToBack(4).addToBack(3).addToBack(2).addToBack(1);
console.log("****BEFORE****")
testlist.printAll()
console.log("****AFTER****")
testlist.reverse()
testlist.printAll()
