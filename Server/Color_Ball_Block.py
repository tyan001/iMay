import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import TensorBoard, EarlyStopping
import time
import os
from keras.preprocessing.image import ImageDataGenerator
import numpy as np


NAME = "Color_Ball_Blocks_CNN_{}".format(int(time.time()))

tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME)) #tensorboard --logdir=logs/

classifier=Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape=(128,128,3), activation=tf.nn.relu))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(32, (3, 3), input_shape=(128,128,3), activation=tf.nn.relu))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())

classifier.add(Dense(activation = tf.nn.relu, units=128))
classifier.add(Dropout(0.5))
classifier.add(Dense(activation = tf.nn.softmax,  units=7))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', 
                   metrics=['accuracy'])

 

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        )

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('train',
                                                 target_size=(128, 128), #same as input_shape in step1
                                                 batch_size=25, 
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('test',
                                            target_size=(128, 128),
                                            batch_size=25,
                                            class_mode='categorical')


es= keras.callbacks.EarlyStopping(monitor='acc', min_delta=.05, patience=3)


history = classifier.fit_generator(training_set,
                        steps_per_epoch=(4000/25),
                        epochs=20,
                        validation_data=test_set,
                        validation_steps=(1000/25),
                        callbacks=[tensorboard, es])


classifier.summary()


#my_list = []
# pred = []
# label_map = training_set.class_indices
# my_test_data=os.listdir(os.path.abspath('C:/Users/Thony/Desktop/Color_Ball_Block/Resize_Predict/'))
#
# for i in range(len(my_test_data)):
#     test = image.load_img('C:/Users/Thony/Desktop/Color_Ball_Block/Resize_Predict/' + my_test_data[i], target_size=(32,32))
#     test_tensor = image.img_to_array(test)
#     test_tensor = np.expand_dims(test_tensor, axis=0)
#     test_tensor /= 255
#     my_list.append(test_tensor)
#     pred.append(classifier.predict(my_list[i]))
#     #pred = classifier.predict(my_list[0])


classifier.save("Color_Ball_Block3.h5")
json_string = classifier.model.to_json()
with open("model3.json", "w") as json_file:
    json_file.write(json_string)