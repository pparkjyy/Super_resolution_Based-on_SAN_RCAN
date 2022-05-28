# Development of Deep Learning Based on Super Resolution Restoration Software for Drone Images

# 1. Abstract
 We propose a Deep Learning based super-resolution software system that restores the image quality of images taken through drones.
Block effects generated in the process of dividing and resolution images by the input of a model based on a Second-Order Attention Network(SAN) to restore image quality are removed using a Blocking Filter. To make the model lighter, the overall model is implemented using Feature-Affinity Based Knowledge Distillation(FAKD).

![image](https://user-images.githubusercontent.com/73782975/170811749-a7448561-3330-4b3b-8c56-9d85f1baf57f.png)

# 2. Test Code
* SAN
> * You can use Web site to SR
> * change directory to '/web/'
>(we used Flask to connect with server)
>>  $ python file_upload.py
>>  then Choose ::Scale::, SAN ( ::SR:: ) and file by browsing. And press Submit Query to SR.
>>  At last, Press 'Submit Query' upper button.
>>  You can find the SR image at 'web/deblock_1' with 'xxx_D.jpg'.

* Distillated Model (RCAN)
+ ! We used RCAN model which doesn't using SOCA operation because of the lack of our laboratory computer graphic memory.
> * You can also use Web site to SR
> * change directory to '/web/'
>(we used Flask to connect with server)
>> $ python file_upload.py
>> the Choose ::Scale::, RCAN ( ::SR:: ) and file by browsing. And press Submit Query to SR.
>> At last, Press 'Submit Query' upper button.
>> You can find the SR image at 'web/deblock_1' with 'xxx_D.jpg'.

# 3. Acknowledge
The code is built on [RCAN(pytorch)](https://github.com/yulunzhang/RCAN) and [SAN](https://github.com/daitao/SAN).
We thank the authors for sharing the codes.

# 4.Future research
* Our codes are quite messy, so we need to refactory the codes and folders.
* We couldn't merge the seperated images. if you know how to merge the images with Python, let us know by Issue Tab, it will be very thanksful


