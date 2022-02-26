#!/home/danama45/Development/Python_project/bin/python
#Create a list with 5 file names.
# Write a function to create folder and then create the five 5 files in the previous exercise into it.
#Your function should write the name of the file as the contents of the file.
#Write some code to read the files that you just created in the previous exercise
#Your code should loop over the list of files,
#open each file,
#read the lines for each file  and split those lines into its component parts.
#then print items from the split, one item at a time.

import os

file_names = ['Richard.txt', 'Okere.txt', 'Nora.txt', 'Terez.txt', 'Grace.txt']
folder = 'Assignment_folder'
men = ['Richard', 'Okere']
ladies = ['Grace', 'Nora' 'Terez']

def create_folder(folder_name, file_names):
    """create a folder and write some files into it"""
    os.mkdir(folder_name)  #makes a new folder
    os.chdir(folder_name) # changes into the folder we just created
    for file in file_names:
        with open(file, 'w') as a_file:
            print(file, file=a_file) # we write to it, and we writr by writing its name
    os.chdir('..') #goes back to the root
    print('I am done creating all files.') #if you want to be fancy,

#Exercise 2
def read_files(folder_name):
    """reads the files in a directory and slipt the lines into the component words"""
    path = (os.path.join(os.getcwd(),folder_name)) #create the absolute path for use with os.listdir
    os.chdir(path)
    files = os.listdir('.') #list all files based on the current location
    for file in files: #we focus only on the file in the directory
        with open(file, 'r') as a_file: #we open each file in read mode
            lines = a_file.readlines() #we grab all the libes in the file
            for line in lines: #then we iterate over all lines 
                for i in line.split(): #we split each lines
                    print(i) # we print the contents from the split
    print('I am done with reading all the files in the directory')

if __name__=="__main__":
    create_folder(folder, file_names)  
    read_files(folder)     