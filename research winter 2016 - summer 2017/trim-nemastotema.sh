#!/bin/bash
#export PATH=$PATH:/work/humberto/asanquiche/tools/Trimmomatic-0.36/
#mkdir /work/humberto/asanquiche/nemastotela/trimmed
ex='_trimmed.fastq.gz'
for file in /work/humberto/asanquiche/nemastotela/raw/*.fastq.gz
do
	base=$(basename $file .fastq.gz)
	echo $base "Is being proccessed"
	java -jar /work/humberto/asanquiche/tools/Trimmomatic-0.36/trimmomatic-0.36.jar SE -threads 8 /work/humberto/asanquiche/nemastotela/raw/$base.fastq.gz $base$ex ILLUMINACLIP:/work/humberto/asanquiche/tools/Trimmomatic-0.36/adapters/TruSeq3-SE.fa:2:30:10 LEADING:28 TRAILING:28 SLIDINGWINDOW:4:4 MINLEN:50


echo finished trim $base >> trimjob
 
#mv *trimmed* /work/humberto/asanquiche/nemastotela/trimmed/	
done
