#!/bin/bash
#SBATCH --mem-per-cpu=64000
#SBATCH --time=150:00:00
#SBATCH --job-name=Normalize_Run
#SBATCH --mail-user=angelsan720@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --error=errornormalize.txt
#SBATCH --output=outnormalize.txt
#SBATCH --ntasks=8


#echo Started pepino >> /work/humberto/asanquiche/working/normjob
/work/humberto/asanquiche/tools/scripts/./normalize-pepino.sh

#echo Started sea demon >> /work/humberto/asanquiche/working/normjob
#/work/humberto/asanquiche/tools/scripts/./normalize-nemastotema.sh

#echo finished >> normjob
