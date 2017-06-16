#! /bin/bash
export PATH=$PATH:~/tools/FastQC/

mkdir /data/angelsan720/data/nemastotema/trimmed/fastqc
for file in /data/angelsan720/data/nemastotema/trimmed/*.fastq
do
	echo $file 
	fastqc $file
done
mv *fastqc* /data/angelsan720/data/nemastotema/trimmed/fastqc/
#mv scores.txt /data/angelsan720/data/nemastotema/trimmed/fastqc/

