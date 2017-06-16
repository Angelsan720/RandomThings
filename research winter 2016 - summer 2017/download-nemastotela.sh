#! /bin/bash
echo date
mkdir /work/humberto/asanquiche/nemastotela
mkdir /work/humberto/asanquiche/nemastotela/raw
cat /work/humberto/asanquiche/tools/nm | while read link;
do
	#echo $link
	wget $link
	echo gotNM >> download
done
echo date
#mv *fast* /work/humberto/asanquiche/nemastotela/raw/
