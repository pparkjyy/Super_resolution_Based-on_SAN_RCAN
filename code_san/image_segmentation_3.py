from PIL import Image
import os

path = os.getcwd() # + '/code_san'
os.chdir(path)
path = '/home/jd/Desktop/web/code_san/input.jpg'
imfilename = os.path.basename(path)
save_path = os.getcwd() + '/code_san/test/Set5/x3/'
img = Image.open(imfilename)
(img_h, img_w) = img.size
grid_w = 180 # crop height
grid_h = 300 # crop width
range_w = (int)(img_w / grid_w)
range_h = (int)(img_h / grid_h)
i = 0
for w in range(range_w):
	for h in range(range_h):
		bbox = (h * grid_h, w * grid_w, (h + 1)*(grid_h), (w + 1)*(grid_w))
		crop_img = img.crop(bbox)
		fname = "{}.jpg".format("{0:05d}".format(i))
		savename = save_path + fname
		os.chdir(save_path)
		crop_img.save(savename)
		i += 1
