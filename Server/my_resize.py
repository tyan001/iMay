import PIL
from PIL import Image
import os
from random import shuffle

 
    
def my_img_resize(pull_dir, my_dir, Hsize=720, Vsize=540):
    
	#This function is used to resize images to desire pixel amount
	#pull_dir is the directory you are pulling your images from
	#my_dir = is the desire directory you want to put the resize images into
	#Hsize is the Horizontal pixel amount
	#Vsize is the Vertical pixel amount
	
    try:
        my_list = os.listdir(os.path.abspath(pull_dir))
    except FileNotFoundError:
        print (pull_dir + " directory does not exist")
        return
    
    #try: 
    #    os.makedirs(my_dir)
    #except OSError:
    #   if not os.path.isdir(my_dir):
    #      raise
            
    for i in range(len(my_list)):
        img = Image.open(pull_dir + '/' + my_list[i])
        img = img.resize((Hsize,Vsize), PIL.Image.ANTIALIAS)
        #img.save(pull_dir + "/")
        img.save(my_dir +"/"+ my_list[i])
		

def make_dirs(dir_name):   
    try: 
        os.makedirs(dir_name)
    except OSError:
        if not os.path.isdir(dir_name):
            raise

		
def my_img_randomizer(my_dir, train_dir, test_dir, train=0.8, test=0.2):
    
	#This function is to randomize an image dataset and split it to a training and testing dataset
	#my_dir is the directory is the directory where all the images are located
	#train_dir is the training directory where 80% of images are going
	#test_dir is the test directory where 20% of images are going
	#EXAMPLE:
	#_type = "BlueBlock"
	#my_path = "C:/Users/user/Desktop/Test/Resize_Ball/" + _type
	#train_dir = "C:/Users/user/Desktop/Test/random_dataset/Train/" + _type
	#test_dir = "C:/Users/user/Desktop/Test/random_dataset/Test/" + _type
	#my_img_randomizer(my_path, train_dir, test_dir)
	
	
	
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
        
    
    for j in range(int(len(my_list))):
        os.rename(my_dir + '/' + my_list[0], test_dir + '/' + my_list[0])
        my_list.remove(my_list[0])