#!/bin/bash
#SBATCH --mem-per-cpu=110000
#SBATCH --time=150:00:00
#SBATCH --job-name=Trinity-pp
#SBATCH --mail-user=angelsan720@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --error=error-trin-pp.txt
#SBATCH --output=out-trin-pp.txt
#SBATCH --ntasks=8

rm -rf /work/humberto/asanquiche/pepino/trinity/
/work/humberto/asanquiche/tools/scripts/trinity-pp.sh
