#! /bin/bash

#module load trinityrnaseq/2.1.1

/work/humberto/asanquiche/tools/trinityrnaseq-2.2.0/Trinity --seqType fq --max_memory 100G --single /work/humberto/asanquiche/pepino/nomalized/SRR490649_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490669_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490752_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490772_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490864_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490868_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490918_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490919_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490920_trimmed.fastq.gz.keep,/work/humberto/asanquiche/pepino/nomalized/SRR490921_trimmed.fastq.gz.keep --CPU 8 --output /work/humberto/asanquiche/pepino/trinity

#module unload trinityrnaseq/2.1.1

