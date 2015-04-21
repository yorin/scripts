sed -e '1d' -e '2d' -e '5d' books.txt 

sed -n '
h;n;H;x
s/\n/, /
/Paulo/!b Print
s/^/- /
:Print
p' books.txt

sed -n 'h;n;H;x;s/\n/, /;/Paulo/!b Print; s/^/- /; :Print;p' books.txt 

sed -n 'h;n;H;x; s/\n/, /; :Loop;/Paulo/s/^/-/; /----/!t Loop; p' books.txt 

sed 'p' books.txt

sed -n '/Paulo/ p' books.txt

sed -n '/Alchemist/, 5 p' books.txt

sed -n '/The/,$ p' books.txt
