#!/usr/bin/env bash
EXP_NAME="new_table_2"
INIT_HYP=1
LOOP_HYP=1
DEV_NUM=0
python start_bayes_optim.py $EXP_NAME $INIT_HYP
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $INIT_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $INIT_HYP 0
for value in {1..2}
do
  echo $value
  python start_bayes_optim4.py $EXP_NAME $LOOP_HYP gpyopt max
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $LOOP_HYP 0
  CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $LOOP_HYP 0
done
echo finished
