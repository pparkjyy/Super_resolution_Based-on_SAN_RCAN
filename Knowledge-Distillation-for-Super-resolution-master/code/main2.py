import os
import sys

os.system("python test.py --data_test Demo --ckp_path student_checkpoint/RCAN_BIX2.pt --TS S --scale 2 --model RCAN --n_resgroups 10 --n_resblocks 6 --test_only --save_results")
