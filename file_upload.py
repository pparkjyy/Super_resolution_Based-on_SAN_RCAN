import os
import sys

from werkzeug.utils import secure_filename
#from torchvision import transforms
from flask import Flask, request, render_template, redirect
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
app = Flask(__name__)
#path = './TestCode/code'  # For SAN model

@app.route('/')
def Webpage():
	return render_template("Webpage.html")

# For SAN model
@app.route('/convert', methods=['GET', 'POST'])
def ConvertPage():
	if request.method == 'POST':
		sr = request.form['SR']
		if sr == "1":
			scale = request.form['Scale'] # scale value
			if scale == "2":
				#scale = request.form['Scale'] # scale value
				f = request.files['file']
				filename = f.filename         # original file name
				f.save(secure_filename('input.jpg'))
				from code_san import image_segmentation_2
				from code_san import main2
				os.chdir('/home/jd/Desktop/web')
				return render_template('Webpage.html')
			elif scale == "3":
				#scale = request.form['Scale'] # scale value
				f = request.files['file']     
				filename = f.filename         # original file name
				f.save(secure_filename('input.jpg'))
				from code_san import image_segmentation_3
				from code_san import main3
				os.chdir('/home/jd/Desktop/web')
				return render_template('Webpage.html')
			elif scale == "4":
				#scale = request.form['Scale'] # scale value
				f = request.files['file']     
				filename = f.filename         # original file name
				f.save(secure_filename('input.jpg'))
				from code_san import image_segmentation_4
				from code_san import main4
				os.chdir('/home/jd/Desktop/web')
				return render_template('Webpage.html')
		
		elif sr == "2": # RCAN
			f = request.files['file']
			filename = f.filename         # original file name
			path = '/home/jd/Desktop/web/Knowledge-Distillation-for-Super-resolution-master/code/'
			os.chdir(path)
			f.save(secure_filename('input.jpg'))
		#	path = '/home/jd/Desktop/web/Knowledge-Distillation-for-Super-resolution-master/code/'
		#	os.chdir(path)
			scale = request.form['Scale'] # scale value
			if scale == "2":
				#scale = request.form['Scale'] # scale value
				os.system("python image_segmentation.py")
				os.system("python test.py --data_test Demo --ckp_path student_checkpoint/RCAN_BIX2.pt --TS S --scale 2 --model RCAN --n_resgroups 10 --n_resblocks 6 --test_only --save_results")
				
				return render_template('Webpage.html')
			elif scale == "3":
				os.system("python image_segmentation.py")
				os.system("python test.py --data_test Demo --ckp_path student_checkpoint/RCAN_BIX3.pt --TS S --scale 3 --model RCAN --n_resgroups 10 --n_resblocks 6 --test_only --save_results")
				
				return render_template('Webpage.html')

			elif scale == "4":
				os.system("python image_segmentation_4.py")
				os.system("python test.py --data_test Demo --ckp_path student_checkpoint/RCAN_BIX4.pt --TS S --scale 4 --model RCAN --n_resgroups 10 --n_resblocks 6 --test_only --save_results")
				
				return render_template('Webpage.html')
				
	else:
		return render_template('Webpage.html')

@app.route('/deblock', methods = ['POST'])
def Deblock():
	if request.method == 'POST':
		import deblock
		return render_template('Webpage.html')


if __name__ == '__main__':
	app.run(host="223.194.46.69", debug = True)

def allwoed_file(filename):
	return '-' in filename and \
		filename.rsplit('-', 1)[1] in ALLOWED_EXTENSIONS