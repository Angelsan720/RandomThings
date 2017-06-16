#!/bin/bash
#SBATCH --mem-per-cpu=35000
#SBATCH --time=48:00:00
#SBATCH --job-name=Trim_Run
#SBATCH --mail-user=angelsan720@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --error=error.txt
#SBATCH --output=out.txt
#SBATCH --ntasks=8
#This script simply prints out current clock time in 12-hour format

echo Started pepino >> /work/humberto/asanquiche/workingdir/trimjob
#/work/humberto/asanquiche/tools/scripts/./trim-pepino2.sh
echo Started sea demon >> /work/humberto/asanquiche/workingdir/trimjob
/work/humberto/asanquiche/tools/scripts/./trim-nemastotema.sh

echo finished
