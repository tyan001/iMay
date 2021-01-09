import PIL
from PIL import Image
import os
from random import shuffle

BlueBallDir = "C:/Users/Thony/Desktop/Test/Ball/BlueBall"

Horizontal_size = 720
Vertical_size = 540
#img = Image.open('Ball/BlueBall/BlueBall 001.JPG')
#img = img.resize((720,540), PIL.Image.ANTIALIAS)

BlueBall_dataset = os.path.abspath(BlueBallDir)
BlueBall_list = os.listdir(BlueBall_dataset)
x = 10
len(str(len(BlueBall_list))) - len(str(x))


my_path = 'Resize_Ball/YellowBall/'
try: 
    os.makedirs(my_path)
except OSError:
    if not os.path.isdir(my_path):
        raise
        
for x in range(len(BlueBall_list)):
    img = Image.open(BlueBallDir + '/' + BlueBall_list[x])
    img = img.resize((720,540), PIL.Image.ANTIALIAS)
    img.save(my_path + BlueBall_list[x])




def my_img_resize(pull_dir, my_dir, Hsize=720, Vsize=540):
    
    try:
        my_list = os.listdir(os.path.abspath(pull_dir))
    except FileNotFoundError:
        print (pull_dir + " directory does not exist")
        return
    
    
    try: 
        os.makedirs(my_dir)
    except OSError:
        if not os.path.isdir(my_dir):
            raise
            
    for i in range(len(my_list)):
        img = Image.open(pull_dir + '/' + my_list[i])
        img = img.resize((Hsize,Vsize), PIL.Image.ANTIALIAS)
        img.save(my_dir + my_list[i])


BallDir = "C:/Users/Thony/Desktop/Test/Block/YellowBlock"   
my_path =  'Resize_Ball/YellowBlock/'
    
my_img_resize(BallDir, my_path)


test_path = "C:/Users/Thony/Desktop/Test/Resize_Ball/BlueBall"
test_dir = os.path.abspath(test_path)
test_list = os.listdir(test_dir)
target_path = 'C:/Users/Thony/Desktop/Test/Resize_Ball/Train_BlueBall'
shuffle(test_list)
len(test_list) * 0.8
test_list.remove(test_list[0])

os.rename(test_path + '/' + test_list[0], target_path + '/' + test_list[0])

def my_img_randomizer(my_dir, train_dir, test_dir, train=0.8, test=0.2):
    
    if train+test>1 or train+test<0:
        print("Variable train and test must add up to 1")
        return
    
    try:
        my_list = os.listdir(os.path.abspath(my_dir))
    except FileNotFoundError:
        print (my_dir + " directory does not exist")
        return
    
    try: 
        os.makedirs(test_dir)
    except OSError:
        if not os.path.isdir(test_dir):
            raise
    
    try: 
        os.makedirs(train_dir)
    except OSError:
        if not os.path.isdir(train_dir):
            raise
    
    shuffle(my_list)
    
    for i in range(int(len(my_list) * train)):
        os.rename(my_dir + '/' + my_list[0], train_dir + '/' + my_list[0])
        my_list.remove(my_list[0])
        
    
    for j in range(int(len(my_list) * test)):
        os.rename(my_dir + '/' + my_list[0], test_dir + '/' + my_list[0])
        my_list.remove(my_list[0])
        
    
        

_type = "BlueBlock"
my_path = "C:/Users/Thony/Desktop/Test/Resize_Ball/" + _type
train_dir = "C:/Users/Thony/Desktop/Test/random_dataset/Train/" + _type
test_dir = "C:/Users/Thony/Desktop/Test/random_dataset/Test/" + _type
my_img_randomizer(my_path, train_dir, test_dir)
        
        
        

