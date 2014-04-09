#!/bin/bash

cmdline='svn update'
exsufix='\.svn'

err() {
	echo -e $1
	exit -1
}

if [ $# -eq 1 ];then
	srcdir=$1
	dstdir=`pwd`
else
	err "Usage: $0 svndir\n\tsvndir: source directory, a svn directory."
fi
# echo $srcdir
# echo $dstdir

cd $srcdir || err "cd $tagpath failed"
$cmdline || err "run $cmdline failed"
find . -type f | grep -v $exsufix | xargs -I {}  cp -ur --parent {} $dstdir
echo 'completed.'



