#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --mem=100G
#SBATCH -t 48:00:00
#SBATCH --partition=cpu        
#SBATCH --account=bbkc-delta-cpu
#SBATCH --job-name=ecosys
#SBATCH --mail-user=langzhou@illinois.edu
#SBATCH --mail-type=ALL
#SBATCH --export=ALL

module load anaconda3_cpu/23.7.4
cd $SLURM_SUBMIT_DIR
source activate
conda activate medfuse
export PYTHONUNBUFFERED=TRUE
mpirun -np 1 python -m mimic3benchmark.scripts.create_decompensation data/root/ data/decompensation/