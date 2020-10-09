import sys
import pyminizip
import binascii
import os

print ("""\

                          | |                
  ___  __ _  ___  __ _  __| | __ _ _ __ ___  
 / _ \/ _` |/ _ \/ _` |/ _` |/ _` | '_ ` _ \ 
|  __/ (_| |  __/ (_| | (_| | (_| | | | | | |
 \___|\__, |\___|\__,_|\__,_|\__,_|_| |_| |_|
       __/ |                                 
      |___/         
	  https://egemenkazanasmaz.com \n
""")

if(len(sys.argv) == 1):
    print("\n Usage: \n kmgn 'dummy_folder' 'actual_folder' 'dummy_password' 'actual_password' 'destination_folder_path' compresslevel(0-9) \n Extract: \n kmgn 'pathtofile'")

elif(len(sys.argv) == 7):
    print("\n working on...")
    pyminizip(getListOfFiles(sys.argv[1]), None, sys.argv[5] + "dummy.zip", sys.argv[3], int(sys.argv[6]))
    print("\n Dummy files compressed.")
    pyminizip(getListOfFiles(sys.argv[2]), None, sys.argv[5] + "actual.zip", sys.argv[4], int(sys.argv[6]))
    print("\n Actual files compressed. \n Starting merging sequence...")
    with open(sys.argv[5] + "dummy.zip", 'rb') as dummy:
        contentDummy = dummy.read()
    
    binascii.hexlify(contentDummy)


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles