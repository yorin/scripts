#!/usr/bin/perl

# Display all the files in /tmp directory.
$dir = "/tmp/*";
my @files = glob( $dir );

foreach (@files ){
   print $_ . "\n";
}

# Display all the C source files in /tmp directory.
$dir = "/tmp/*.c";
@files = glob( $dir );

foreach (@files ){
   print $_ . "\n";
}

# Display all the hidden files.
$dir = "/tmp/.*";
@files = glob( $dir );
foreach (@files ){
   print $_ . "\n";
}

# Display all the files from /tmp and /home directories.
$dir = "/tmp/* /home/*";
@files = glob( $dir );

foreach (@files ){
   print $_ . "\n";
}
