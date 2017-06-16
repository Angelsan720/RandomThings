#!/bin/bash
#export PATH=$PATH:/work/humberto/asanquiche/tools/Trimmomatic-0.36/
mkdir /work/humberto/asanquiche/pepino/trimmed

for file in /work/humberto/asanquiche/pepino/raw/*.fastq.gz
do
	#takes the base name of the file for usage in renaming
	base=$(basename $file .fastq.gz)
	echo $base "Is being proccessed"
	#This is a bit complicated
	#Trimmomatic is a java program
	#Illuminaclip files are in the adapters folder
	#I recomend reading up on how to use it on your own
	java -jar /work/humberto/asanquiche/tools/Trimmomatic-0.36/trimmomatic-0.36.jar SE -threads 8 /work/humberto/asanquiche/pepino/raw/$base.fastq.gz $base_trimmed.fastq.gz ILLUMINACLIP:/work/humberto/asanquiche/tools/Trimmomatic-0.36/adapters/TruSeq3-SE.fa:2:30:10 LEADING:20 TRAILING:24 SLIDINGWINDOW:4:4  MINLEN:26

echo finished trim $base >> ~/trimjob

done
 
mv *trimmed* /work/humberto/asanquiche/pepino/trimmed/	
