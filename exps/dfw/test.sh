python $CS548_DIR/dfw/run.py test \
  --img_size 256 --msg_l 31 --device 0 --batch_size 256 \
  --noise_type no_noise --enc_scale 0.01 --dec_scale 1
  
python $CS548_DIR/dfw/run.py test \
  --img_size 256 --msg_l 31 --device 0 --batch_size 256 \
  --noise_type combined --enc_scale 0.01 --dec_scale 1
