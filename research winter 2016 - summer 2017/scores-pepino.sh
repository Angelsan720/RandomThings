#! /bin/bash
export PATH=$PATH:/work/humberto/asanquiche/tools/FastQC/

#make the fastqc folder for the quality scores data
mkdir /data/angelsan720/data/pepino/raw/fastqc

for file in /data/angelsan720/data/pepino/raw/*.fastq.gz
do
	echo $file 
	fastqc $file
done    
mv *fastqc* /data/angelsan720/pepino/raw/fastqc/

#youll have to download the data to view it

