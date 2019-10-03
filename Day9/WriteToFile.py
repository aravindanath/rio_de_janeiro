"""
File Input/Output mode

w --> write to a file
r --> read from a file
r+ --> read and write to a file
a --> append mode
\n --> new line


There are 6 access modes in python.

Read Only (‘r’) : Open text file for reading. The handle is positioned at
the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
Read and Write (‘r+’) : Open the file for reading and writing. The handle
is positioned at the beginning of the file. Raises I/O error if the file does not exists.
Write Only (‘w’) : Open the file for writing. For existing file,
the data is truncated and over-written. The handle is positioned at
the beginning of the file. Creates the file if the file does not exists.
Write and Read (‘w+’) : Open the file for reading and writing.
 For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
Append Only (‘a’) : Open the file for writing.
The file is created if it does not exist.
The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
Append and Read (‘a+’) : Open the file for reading and writing.
The file is created if it does not exist.
 The handle is positioned at the end of the file.
  The data being written will be inserted at the end, after the existing data.
Openin

"""

my_list =["Ashwin","Shobin","Bhuvaneshwari","Deepak","Josh"]

my_file = open("./TestData_1.txt",'w')


for item in my_list:
    # my_file.write(str(item))
    my_file.write(str(item)+ "\n")

my_file.close()