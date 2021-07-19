
/*
    removeNegatives(): Write a method that will remove all nodes with negative values from our singly linked list.

    EXAMPLES:

    H: -1 -> 5 -> 7 -> -3 -> 4 -> will become H: 5 -> 7 -> 4 ->

    H: 7 -> -4 -> -3 -> -2 -> will become H: 7 ->

    H: -10 -> -7 -> -4 -> will become H: (an empty list)

    H: (empty list) will become H: (empty list)

    secondToLastValue(): Write a method that will find the second to last node and return its value

    EXAMPLES:
    H: 10 -> 9 -> 4 -> 1 ->  would return 4
    H: (empty list) would return false
    H: 10 -> would return false
    
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

    printAll() {
        var string = "Current: ";
        var potato = this.head;
        while (potato != null) {
            string += potato.value + ", ";
            potato = potato.next;
        }
        console.log(string);
    }

    removeNegatives(){
        if(this.head == null) {
            return false;
        }
        var lagger = null;
        var leader = this.head;
        while(leader != null) {
            if(leader.value < 0) {
                leader = leader.next;
                lagger = leader;
                if (leader.next == null) {
                    return this;
                } else {
                    leader = leader.next;
                }
            }
            lagger = leader;
            if(leader.next == null){
                return this;
            }     
            leader = leader.next;
        }
        return this;
    }

    secondToLastValue(){
        if(this.head == null || this.head.next == null) {
            return false;
        }
        var lagger = null; 
        var leader = this.head; 
        while(leader.next != null) {
            lagger = leader;
            leader = leader.next;
        }
        return lagger.value;
    }
}

//REMOVE NEGATIVES
// H: -1 -> 5 -> 7 -> -3 -> 4 -> will become H: 5 -> 7 -> 4 ->
var t1 = new SLList();
t1.addToFront(4).addToFront(-3).addToFront(7).addToFront(5).addToFront(-1);
console.log("******BEFORE********");
console.log(t1.printAll());
t1.removeNegatives();
console.log("******AFTER********");
console.log(t1.printAll());
// H: 7 -> -4 -> -3 -> -2 -> will become H: 7 ->
// var t2 = new SLList();
// t2.addToFront(-2).addToFront(-3).addToFront(-4).addToFront(7);
// console.log("******BEFORE********");
// console.log(t2.printAll());
// t2.removeNegatives();
// console.log("******AFTER********");
// console.log(t2.printAll());
// H: -10 -> -7 -> -4 -> will become H: (an empty list)
// var t3 = new SLList();
// t3.addToFront(-4).addToFront(-7).addToFront(-10)
// console.log("******BEFORE********")
// console.log(t3.printAll())
// t3.removeNegatives()
// console.log("******AFTER********")
// console.log(t3.printAll())
// : (empty list) will become H: (empty list)
// var t4 = new SLList();
// console.log("******BEFORE********")
// console.log(t4)
// t1.removeNegatives()
// console.log("******AFTER********")
// console.log(t4)

// //SECOND TO LAST VALUE 
// // EXAMPLES:
// // H: 10 -> 9 -> 4 -> 1 ->  would return 4
// var t5 = new SLList();
// t5.addToFront(1).addToFront(4).addToFront(9).addToFront(10);
// console.log("******BEFORE********")
// console.log(t5)
// var t5return = t5.secondToLastValue()
// console.log("******AFTER********")
// console.log(t5return)
// // H: (empty list) would return false
// var t6 = new SLList();
// console.log("******BEFORE********")
// console.log(t6)
// var t6return = t6.secondToLastValue()
// console.log("******AFTER********")
// console.log(t6return)
// // H: 10 -> would return false
// var t7 = new SLList();
// t7.addToFront(10)
// console.log("******BEFORE********")
// console.log(t7)
// var t7return = t7.secondToLastValue();
// console.log("******AFTER********");
// console.log(t7return);
