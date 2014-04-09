#!/bin/bash

cmdline='git pull'
exsufix='\.git'

err() {
	echo -e $1
	exit -1
}

if [ $# -eq 1 ];then
	srcdir=$1
	dstdir=`pwd`
else
	err "Usage: $0 gitdir\n\tgitdir: source directory, a git directory."
fi
# echo $srcdir
# echo $dstdir

cd $srcdir || err "cd $tagpath failed"
$cmdline || err "run $cmdline failed"
find . -type f | grep -v $exsufix | xargs -I {}  cp -ur --parent {} $dstdir
echo 'completed.'



