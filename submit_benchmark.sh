#!/bin/bash

# Test number of CPU nodes
cd CPU/test_Nnodes/
sbatch npt_N1.job
sbatch npt_N2.job
sbatch npt_N3.job
sbatch npt_N4.job
sbatch npt_N5.job

# Test number of processors
cd ../test_np/
sbatch npt.job

# Test number of GPU nodes
cd ../../GPU/G1/
sbatch npt.job

cd ../G2/
sbatch npt.job

cd ../G4/
sbatch npt.job

cd ../G8/
sbatch npt.job