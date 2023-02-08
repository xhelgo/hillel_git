# import os
import os

# create "files" directory
os.mkdir("files")

# change current directory to "files"
os.chdir("files")

# create 9 new directories using for loop
for i in range(1, 10):
    os.mkdir("new_dir_" + str(i))

# check if manually create file is file
os.path.isfile("C:/Users/02hop/PycharmProjects/Hillel_HW/HW_11/new_dir_3/test.txt")

# remove dirs 7-9
for i in range(7, 10):
    os.rmdir("C:/Users/02hop/PycharmProjects/Hillel_HW/HW_11/new_dir_" + str(i))

# create a decorator measure execution time
import time


def measuretime(func):
    def time_measurer(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executed in: {end_time - start_time} seconds")
        return result

    return time_measurer


@measuretime
def my_function():
    time.sleep(2)


my_function()
