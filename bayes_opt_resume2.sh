#!/usr/bin/env bash
for value in {1..100}
do
  echo $value
  python start_bayes_optim4.py 10 gpyopt max
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_3a.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_3b.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_4.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_5.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_tbp.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_tbtcso.py 10 0
  CUDA_VISIBLE_DEVICES=3 python per_script_optimization/db_fig_bw.py 10 0
done
echo finished
