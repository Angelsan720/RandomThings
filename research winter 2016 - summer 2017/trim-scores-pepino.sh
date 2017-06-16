#! /bin/bash
export PATH=$PATH:~/tools/FastQC/

mkdir /data/angelsan720/data/pepino/trimmed/fastqc
for file in /data/angelsan720/data/pepino/trimmed/*.fastq
do
	echo $file 
	fastqc $file
done
mv *fastqc* /data/angelsan720/data/pepino/trimmed/fastqc/
#mv scores.txt /data/angelsan720/data/pepino/trimmed/fastqc/

