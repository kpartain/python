class SLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SLList {
    constructor() {
        this.head = null;
    }

    addToFront(value) {
        var newHead = new SLNode(value);
        newHead.next = this.head;
        this.head = newHead;
        return this;
    }

    addToBack(value) {
        if (this.head == null) {
            this.addToFront(value);
            return this;
        }

        var newNode = new SLNode(value);
        var runner = this.head;

        while (runner.next != null) {
            runner = runner.next;
        }

        runner.next = newNode;
        return this;
    }

    contains(value) {
        if (this.head == null) {
            return false;
        }

        var runner = this.head;

        while (runner != null) {
            if (runner.value == value) {
                return true;
            } else {
                runner = runner.next;
            }
        }

        return false;
    }

    removeFront() {
        if (this.head == null) {
            return false;
        }

        var nodeToRemove = this.head;
        this.head = nodeToRemove.next;
        nodeToRemove.next = null;

        return nodeToRemove;
    }

    removeBack() {
        if (this.head == null) {
            return false;
        } else if ((this.head.next = null)) {
            return this.removeFront();
        }

        var lagger = null;
        var leader = this.head;
        while (leader.next != null) {
            lagger = leader;
            leader = leader.next;
        }

        lagger.next = null;
        return leader;
    }

    moveMinToFront() {
        if (this.head == null || this.head.next == null) {
            return this;
        }
        var minPrev = null; // At the end, we'll use this to "skip around" the min
        var min = this.head; // And this will be our min value node

        var lagger = null;
        var leader = this.head;

        while (leader != null) {
            if (leader.value < min.value) {
                min = leader;
                minPrev = lagger;
            }
            lagger = leader;
            leader = leader.next;
        }

        if (min != this.head) {
            minPrev.next = min.next;
            min.next = this.head;
            this.head = min;
        }
        return this;
    }

    moveMaxToBack() {
        if (this.head == null || this.head.next == null) {
            return this;
        }
        var maxPrev = null;
        var max = this.head;
        var lagger = null;
        var leader = this.head;
        while (leader != null) {
            if (leader.value > max.value) {
                max = leader;
                maxPrev = lagger;
            }
            lagger = leader;
            leader = leader.next;
        }

        if ((max = this.head)) {
            this.head = max.next;
        } else {
            maxPrev.next = max.next;
        }
        lagger.next = max;
        max.next = null;
        return this;
    }

    prepend(valueToFind, valueToAdd) {
        // - What if the list is empty?
        if (this.head == null) {
            return false;
        } // - What if the value I'm looking for isn't there?
        else if (this.contains(valueToFind) == false) {
            return false;
        } else {
            var findNode = new SLNode(valueToFind);
            var firstPos = this.head;
            while (firstPos != findNode && firstPos.next != null) {
                if(firstPos == findNode) {
                    break;
                } else {
                    firstPos = firstPos.next;
                }
            }
            console.log("First Pos:");
            console.log(firstPos);
            var nodeAdded = new SLNode(valueToAdd);
            nodeAdded.next = firstPos;
            var runner = firstPos.next;
            while (firstPos != null) {
                runner = firstPos;
                firstPos = firstPos.next;
            }
            return this;
        }
    }

    append(valueToFind, valueToAdd) {
        // - What if the list is empty?
        if (this.head == null) {
            return false;
        } // - What if the value I'm looking for isn't there?
        else if (this.contains(valueToFind) == false) {
            return false;
        } else {
        }
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
}
/*
    Prepend => 2 parameters: valueToFind, valueToAdd
    - Find the node with a value of valueToFind, and add a new node with a value of
    valueToAdd before it.
    EXAMPLE: 
    someList = H: 5 -> 4 -> 2 -> 1 ->
    someList.prepend(2, 3) would make someList H: 5 -> 4 -> 3 -> 2 -> 1 ->
*/
someList = new SLList();
someList.addToFront(1).addToFront(2).addToFront(4).addToFront(5);
console.log("Before Prepend: ----------------------");
someList.printAll();
someList.prepend(2, 3);
console.log("After Prepend: ----------------------");
someList.printAll();

/*
    Append => 2 parameters: valueToFind, valueToAdd
    - Find the node with a value of valueToFind, and add a new node with a value of
    valueToAdd after it.
    someList = H: 7 -> 2 -> 4 -> 8 -> 11 ->
    someList.append(4, 5) would make someList H: 7 -> 2 -> 4 -> 5 -> 8 -> 11 ->
*/
// someList1 = new SLList();
// someList1.addToFront(11).addToFront(8).addToFront(4).addToFront(2).addToFront(7);
// console.log("Before Append: ----------------------")
// someList.printAll();
// someList.append(4,5);
// console.log("After Append: ----------------------")
// someList.printAll();
