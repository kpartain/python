/* 
    Three challenges!

    addToFront: Write a method of the SLList class that accepts a value, and adds a node with that 
    value to the front of the list. 
    
    Steps:
        1. Create a new node
        2. Assign that node's next attribute to the list's current head
        3. Assign the list's current head to the new node

    KEEP IN MIND: What dictates that a node is the first element in the list? Might need to reset that.

    addToBack: Write a method of the SLList class that accepts a value, and adds a node with that
    value to the BACK of the list.

    Steps:
        1. Create a new node
        2. Start at the head of the list
        3. Run to the last node
        4. Set the last node's next attribute to the new node
    EDGE CASE: What if the list is empty? How do we even know if the list is empty?

    contains: Write a method of the SLList class that accepts a value, and returns a boolean based
    on whether or not a node with that value exists in the list

    Steps:
        1. Start at the head of the list
        2. Check if the value of the node we're looking at equals the value passed in
        3. If it does, return true
        4. If not, go to the next node.
        5. If we checked every single node and we're still running the method, the value does not exist in the list.
*/

class Node {
    constructor(value) {
        this.value = value;
        this.next = null; // Why??
    }
}

class SLList {
    constructor(){
        this.head = null;
    }

    addToFront(value) {
        var newNode = new Node(value)
        if(this.head == null) {
            this.head = newNode;
            return this;
        } else {
            newNode.next = this.head;
            this.head = newNode;
            return this;
        }
        //vs
        // newNode.next = this.head;
        // this.head = newNode;
        // return this;

    }

    addToBack(value) {
        var newLastNode = new Node(value)
        if (this.head == null){
            this.head = newLastNode;
            console.log(newLastNode)
            console.log(this.head)
            return this
        }
        var currentNode = this.head;
        while (currentNode.next != null) {
            currentNode = currentNode.next;
            console.log(currentNode);
            }
        currentNode.next = newLastNode;
        return this;
    }

    contains(value) {
        var returnBoolean = false;
        console.log("value " + value)
        console.log("thishead " + this.head.value)
        if(this.head.value == value) {
            console.log("inside if " + value)
            returnBoolean = true;
            return returnBoolean;
        }
        var currentNode = this.head;
        while(currentNode.next != null) {
            if(currentNode.head == value){
                returnBoolean = true;
            }
            currentNode = currentNode.next;
            console.log(currentNode);
        }
        console.log("return boolean " + returnBoolean)
        return returnBoolean
    }
}

var newList = new SLList();

newList.addToBack(5).addToBack(1).addToFront(3);

var contains5 = newList.contains(5);
console.log("contains five: " + contains5)
var contains5Expected = true;

var contains2 = newList.contains(2);
console.log("contains two: " + contains2)
var contains2Expected = false;

var contains3 = newList.contains(3);
console.log("Contains three: " + contains3)
var contains3Expected = true;