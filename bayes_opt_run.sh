#!/bin/sh

sudo python start_bayes_optim.py 5 drop
sudo CUDA_VISIBLE_DEVICES=0 python per_script_optimization/db_fig_3a.py 5 0
sudo CUDA_VISIBLE_DEVICES=0 python per_script_optimization/db_fig_3b.py 5 0
sudo python ops/generate_and_insert_next_combo.py
sudo CUDA_VISIBLE_DEVICES=0 python per_script_optimization/db_fig_3a.py 1 0
sudo CUDA_VISIBLE_DEVICES=0 python per_script_optimization/db_fig_3b.py 1 0
