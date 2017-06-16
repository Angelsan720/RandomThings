#! /bin/bash
export PATH=$PATH:~/tools/FastQC/

rm -rf /data/angelsan720/data/nemastotema/raw/fastqc/
mkdir /data/angelsan720/data/nemastotema/raw/fastqc
for file in /data/angelsan720/data/nemastotema/raw/*fast*
do
	echo $file
	fastqc $file
done    
mv /data/angelsan720/data/nemastotema/raw/*fastqc* /data/angelsan720/nemastotema/raw/fastqc/

