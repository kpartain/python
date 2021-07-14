const { thomsonCrossSectionDependencies } = require("mathjs");

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
        if(this.head.next == null) {
            this.head = null;
            return true;
        }
        var positionOne = this.head;
        this.head = positionOne.next;
        while(positionOne.next != null) {
            positionOne = positionOne.next;
        }
        positionOne.next = null;
        return true;
    }

    removeBack() {
        //if we have an empty list
        if(this.head == null){
            return false;
        }
        //if we only have a head
        var runner = this.head;
        if(runner.next == null) {
            this.head = null;
            return this;
        }
        //otherwise if we have a head and at least one child node
        var runner = this.head;
        var runnerNext = runner.next
        while(runnerNext.next != null) {
            runner = runnerNext;
            runnerNext = runnerNext.next; 
        }
        runner.next = null;
    }
}

var mySLL = new SLList()
mySLL.addToFront(3).addToFront(2).addToFront(1);
console.log("ORIGINAL")
console.log(mySLL)
mySLL.removeFront();
console.log("REMOVE FRONT")
console.log(mySLL);
mySLL.removeBack();
console.log("REMOVE BACK");
console.log(mySLL)