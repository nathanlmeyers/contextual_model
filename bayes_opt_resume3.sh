#!/usr/bin/env bash
EXP_NAME="best_params"
LOOP_HYP=104
DEV_NUM=3
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3a.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_3b.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_4.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_5.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_7.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbp.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_tbtcso.py $EXP_NAME $LOOP_HYP 0
CUDA_VISIBLE_DEVICES=$DEV_NUM python per_script_optimization/db_fig_bw.py $EXP_NAME $LOOP_HYP 0
