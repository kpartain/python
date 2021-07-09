function bookIndex(pages) {
    var output = "";
    for (var i = 0; i < pages.length; i++) {
        var rangeStart = pages[i];
        //check pages[i] and pages[i+1] are not consecutive
        while (pages[i] + 1 == pages[i + 1]) {
            i++;
        }
        var rangeEnd = pages[i];
        if (i != pages.length - 1) {
            if (rangeStart == rangeEnd) {
                output += rangeStart + ",";
            } else {
                output += rangeStart + "-" + rangeEnd + ",";
            }
        } else {
            if (rangeStart == rangeEnd) {
                output += rangeStart;
            } else {
                output += rangeStart + "-" + rangeEnd;
            }
        }
    }
    return output;
}
console.log(bookIndex([1, 5, 6, 7, 8, 9, 10, 14, 22, 23, 24, 25, 27]));
