/*
    breakCircular() 

    Now that we've found a way to determine if a singly linked list is circular, let's 
    write a method that will BREAK the singly linked list. 

    To break a singly linked list, we must find what SHOULD be the last node (i.e. the node that
    has a .next pointing back at a previous node), and redirect its .next to null

    Challenge: Do this without any extra data structures
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
        var startOfCircle = this.head; //cap
        var runner = this.head; //sam
        while(startOfCircle != null && startOfCircle.next != null && startOfCircle.next.next) {
            startOfCircle = startOfCircle.next.next;
            runner = runner.next;
            if(startOfCircle == runner) {
                return true;
            }
        }
        return false;
    }

    breakCircle() {
        //if someone ran this on a non-circle, return false
       if(this.head == null || this.head.next == null || this.head.next.next == null ){
           return False;
       }
       var couchPotato = this.head;
       var runner = this.head.next;
       while(runner.next != couchPotato){
           while (runner.next != runner) {
               if(runner.next == runner) {
                   break;
                }
                runner.next = runner.next.next;
           }
           if(runner.next == couchPotato){
               break;
           } else {
               couchPotato = couchPotato.next;
               runner = runner.next; //or couchpotato.next
           }
       }
       runner.next = null;
       return this;
    }

    breakcirc2(){
        var walker = this.head;
        var runner = this.head.next
        while (walker != runner) {
            if(runner == null || runner.next == null) {
                return this
            }
            walker = walker.next
            runner = runner.next.next
        }
        walker = this.head
        while (runner.next != walker) {
            walker = walker.next
            runner = runner.next
        }
        runner.next = null
        return this
    }
    printAll() {
        var string = "Current: "
        var potato = this.head;
        while (potato.next != null) {
            string += potato.value + ", "; 
            potato = potato.next;
            if(potato.next == null) {
                string += potato.value + " END"
            }
            
        }
        console.log(string);
    }
}


var list1 = new SLList();
list1.addToBack(1).addToBack(2).addToBack(3).addToBack(4);
list1.head.next.next.next.next = list1.head.next;
console.log(list1.isCircular())
console.log(list1)
list1.breakcirc2()
console.log(list1.isCircular())
console.log(list1)
list1.printAll()