#! /bin/sh

srcdir=`dirname $0`
test -z "$srcdir" && srcdir=.

ORIGDIR=`pwd`
cd $srcdir

rm -rf $srcdir/autom*
rm -f $srcdir/config.*

intltoolize --copy -f --automake

autoreconf -v --install || exit 1
cd $ORIGDIR || exit $?

$srcdir/configure "$@"
