#!/bin/bash
#SBATCH --mem-per-cpu=110000
#SBATCH --time=150:00:00
#SBATCH --job-name=Trinity-nm
#SBATCH --mail-user=angelsan720@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --error=error-trin-nm.txt
#SBATCH --output=out-trin-nm.txt
#SBATCH --ntasks=8

rm -rf /work/humberto/asanquiche/nemastotela/trinity/
/work/humberto/asanquiche/tools/scripts/trinity-nm.sh
