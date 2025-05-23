CUDA_VISIBLE_DEVICES=0 CUDA_LAUNCH_BLOCKING=1 python fusion_main.py \
--dim 256 --dropout 0.3 --layers 2 \
--vision-backbone resnet34 \
--mode eval \
--epochs 50 --batch_size 16 \
--vision_num_classes 14 --num_classes 25 \
--data_pairs partial_ehr_cxr \
--fusion_type lstm \
--load_state checkpoints/phenotyping/medfuse_optimal/best_checkpoint.pth.tar