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

@theList = (205, 4, 100, 1, 2, 2000, 6, 93, 2, 65);
@theSortedList = sort {$a cmp $b} @theList;
print join(', ', @theSortedList)."\n";

%h = {
    'a' => 40,
    'b' => 45,
    'c' => 7,
    'd' => 100,
    'e' => 2
};

@sortedKeys1 = sort { $h{$a} <=> $h{$b} } keys %h;
print join(', ', @sortedKeys1)."\n";
