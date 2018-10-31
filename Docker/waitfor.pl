#!/usr/bin/perl
use strict;
use warnings;
use Socket qw(PF_INET SOCK_STREAM pack_sockaddr_in inet_aton);
use IO::Socket::INET;

my ( $addr, $port ) = @ARGV;

while (1) {
    socket( my $socket, PF_INET, SOCK_STREAM, 0 )
      or die "socket: $!";
    if ( connect( $socket, pack_sockaddr_in( $port, inet_aton($addr) ) ) ) {
        close $socket;
        exit 0;
    }
    else { sleep(1); }
}
