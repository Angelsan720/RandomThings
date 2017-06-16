#! /bin/bash

#This script requires preparation
# ask the prof

#this is magic to me
module load gcc
module load python2
. /work/humberto/asanquiche/tools/khmerenv/bin/activate khmer

#make the normalized data folder
#mkdir /work/humberto/asanquiche/pepino/nomalized

for file in /work/humberto/asanquiche/pepino/trimmed/*
do

	#This can take a some time
	echo working on $file >> normjob
	normalize-by-median.py -C 20 -x 6e9 $file  
done
#normalized data has a ".keep" extension
#mv *keep /work/humberto/asanquiche/pepino/normalized/



deactivate
