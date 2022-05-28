from PIL import Image
import os

path = '/home/jd/Desktop/web/SR/BI/Result_2/Set5/x2/'
ConvertedToPdfPath = '/home/jd/Desktop/web/'
file_list = os.listdir(path)

img_list=[]
img_path = path + file_list[0]
im_buf = Image.open(img_path)
cvt_rgb_0 = im_buf.convert('RGB')

for i in file_list:
    img_path = '/home/jd/Desktop/web/SR/BI/Result_2/Set5/x2/' + i
    im_buf = Image.open(img_path)
    cvt_rgb = im_buf.convert('RGB')
    img_list.append(cvt_rgb)

del img_list[0]
cvt_rgb_0.save('/home/jd/Desktop/web/Result_x2.pdf', save_all = True, append_images = img_list)


merged = Image.new('L', (300 * ))