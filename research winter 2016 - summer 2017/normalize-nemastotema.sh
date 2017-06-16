#! /bin/bash

module load gcc
module load python2
source /work/humberto/asanquiche/tools/khmerenv/bin/activate khmer
mkdir /work/humberto/asanquiche/nemastotela/nomalized

for file in /work/humberto/asanquiche/nemastotela/trimmed/*
do
	echo working on $file >> normjob
	normalize-by-median.py -C 20 -x 6e9 $file  
done
#mv *keep /work/humberto/asanquiche/nemastotela/normalized/

deactivate
