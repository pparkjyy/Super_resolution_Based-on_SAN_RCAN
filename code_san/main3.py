import os
import sys
path = '/home/jd/Desktop/web/code_san/'
os.chdir(path)

os.system("python main1.py --model san --data_test MyImage --save Result_3 --scale 3 --n_resgroups 20 --n_resblocks 10 --n_feats 64 --reset --chop --save_results --test_only --testpath test --testset Set5 --pre_train ../model/SAN_BIX3.pt")
