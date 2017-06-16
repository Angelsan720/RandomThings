#! /bin/bash
echo date
export PATH=$PATH:/work/humberto/asanquiche/tools/sratoolkit.2.7.0-ubuntu64/bin/

#create work directory
mkdir /work/humberto/asanquiche/pepino

mkdir /work/humberto/asanquiche/pepino/raw

#pipe list of sra ids to loop
cat /work/humberto/asanquiche/tools/pepino | while read ID;
do

	echo $ID
	#download the data compressed using gzip
	fastq-dump.2.7.0  --defline-seq '@$sn[_$rn]/$ri' --gzip $ID

done
#echo date
#move the data to the rad data directory
mv *fast* /work/humberto/asanquiche/pepino/raw/


#important SRATOOLS will download the data to a folder named ncbi
#this is a copy of the data you can delete it if not needed
