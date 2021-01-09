import shutil
import os
import my_resize
import multiprocessing

Proj_zip = "Ball_Block_Proj.zip"
Proj_name = Proj_zip.replace(".zip", "")
shutil.unpack_archive(Proj_zip, Proj_name)
resize_string = "resized"
test_string = "test"
train_string = "train"


def multi_func(directories):
    print(directories + " Starting")
    my_resize.make_dirs(resize_string + "/" + directories)
    my_resize.make_dirs(test_string + "/" + directories)
    my_resize.make_dirs(train_string + "/" + directories)
    my_resize.my_img_resize(Proj_name+"/"+directories,
                            resize_string+"/"+directories+"/")
    print(directories+ " Finished")


if __name__ == '__main__':

    my_resize.make_dirs(resize_string)
    my_resize.make_dirs(test_string)
    my_resize.make_dirs(train_string)

    directories = os.listdir(Proj_name)

    print("starting")
    processes = []

    for i in range(len(directories)):
        p = multiprocessing.Process(target=multi_func, args=(directories[i],))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    for i in range(len(directories)):
        my_resize.my_img_randomizer(resize_string + "/" + directories[i],
                                   train_string + "/" + directories[i],
                                   test_string + "/" + directories[i])


    print("randomizing finished")