import os
import sys
path = '/home/jd/Desktop/web/deblock_1/'
os.chdir(path)

os.system("bazel-bin/knusperli sanx2.jpg sanx2_D.png")
os.system("bazel-bin/knusperli sanx3.jpg sanx3_D.png")
os.system("bazel-bin/knusperli sanx4.jpg sanx4_D.png")
os.system("bazel-bin/knusperli rcanx2.jpg rcanx2_D.png")
os.system("bazel-bin/knusperli rcanx3.jpg rcanx3_D.png")
os.system("bazel-bin/knusperli rcanx4.jpg rcanx4_D.png")
