#!/usr/bin/perl
use Modern::Perl;
use strict;
use warnings;
use Data::Dumper;
use CGI qw/:standard/;
use CGI::Carp qw/fatalsToBrowser/;

 print header(), start_html(-title=>'my gallery' -stile=> 'background-color:lightgray; font-family:courier' );
 print a ( { -href=>'/' },
               "HOME" ),p(); 

 print p(); 
 
 my $file = 'shield_2D.bl';
 open ( FILE, "<", $file ) or die "$file: $!\n";
 my @lines = <FILE>;
 close FILE;
 
 for my $line (@lines){
	print $line,p();
}
print end_html();




  





	




