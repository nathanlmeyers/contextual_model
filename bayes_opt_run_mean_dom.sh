#!/usr/bin/env bash
EXP_NAME="ntest1"
INIT_HYP=20
LOOP_HYP=5
DEV_NUM=3
python start_bayes_optim.py $EXP_NAME $INIT_HYP
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_7.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $INIT_HYP 0
for value in {1..1}
do
  echo $value
  python start_opt_min.py $EXP_NAME $LOOP_HYP gpyopt max
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_7.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $LOOP_HYP 0
  python start_opt_mean.py $EXP_NAME $LOOP_HYP gpyopt max
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_7.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $LOOP_HYP 0
done
echo finished
