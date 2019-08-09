#3 times we should repeat
#open foler: (Project2) 
#see how many files: (Jerusha1 , Jerusha2 , one.py)
#getting filenames & writing filenames to topics.txt

import os,sys
from os import path
location='.'  #'.' gives current directory path i.e., Project2 (./ gives next directory)
files=os.listdir(location)# used to get list of files and folders
fd=open("topics.txt","w+")#open func.
# for loop is used to check each file
for names in files:
    print(names,path.isfile(names))#to print names
    if(path.isfile(names)):#checking if its file or a folder
        if(names!="topics.txt"):
            fd.write(names+"\n")#writing the file name into topics.txt
    else:
        # Creating path for folders (./Jerusha1, ./Jerusha2)
        location2 = location+"/"+names #'/' is used to get next directory
        print(location2)
        files2=(os.listdir(location2))# to list all files and folders in directory
        fd1=open(location2+"/"+"topics.txt","w+")
        for names1 in files2:
            print(location2+"/"+names1,path.isfile(location2+"/"+names1))
            if(path.isfile(location2+"/"+names1)):
                # Skip writing topics.txt 
                if(names1!="topics.txt"):
                    fd1.write(names1+"\n")
                    fd.write(names1+"\n")
        fd1.close()
fd.close()

   

