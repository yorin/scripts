# standard sorting
@theList = (4, 1, 2, 6, 93, 2, 65);
@theSortedList = sort @theList;
print join(', ', @theSortedList)."\n";

#custom sorting
@theList = (4, 1, 2, 6, 93, 2, 65);
@theSortedList = sort {$b <=> $a} @theList;
print join(', ', @theSortedList)."\n";

@theList = (3, "pear", "four", "apple", 7);
@theSortedList = sort {$b cmp $a} @theList;
print join(', ', @theSortedList)."\n";
