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

if(len(sys.argv) == 1):
    print("\n Usage: \n kmgn 'dummy_folder' 'actual_folder' 'dummy_password' 'actual_password' 'destination_folder_path' compresslevel(0-9) \n Extract: \n kmgn 'pathtofile'")

elif(len(sys.argv) == 7):
    print("\n working on...")
    print(sys.argv[5])
    pyminizip.compress(sys.argv[1], None, sys.argv[5] + "\\dummy.zip", sys.argv[3], int(sys.argv[6]))
    print("\n Dummy files compressed.")
    pyminizip.compress(sys.argv[2], None, sys.argv[5] + "\\actual.zip", sys.argv[4], int(sys.argv[6]))
    print("\n Actual files compressed. \n Starting merging sequence...")
    with open(sys.argv[5] + "\\dummy.zip", 'rb') as dummy:
        contentDummy = dummy.read()
    
    dummyhex = binascii.hexlify(contentDummy)

    with open(sys.argv[5] + "\\actual.zip", 'rb') as actual:
        contentActual = actual.read()

    actualhex = binascii.hexlify(contentActual)

    fullhex = actualhex + dummyhex
    
    f = open(sys.argv[5] + "\\result.zip", "wb")
    f.write(binascii.unhexlify(fullhex))

elif(len(sys.argv) == 2):
    with open(sys.argv[1], 'rb') as extract:
        contentExtract = extract.read()
    extractHex =  binascii.hexlify(contentExtract)
    
    extractedArray = extractHex.decode().split("504b0304140003000800")
    print (extractedArray)
    extractedArray[1] = "504b0304140003000800" + extractedArray[1]
    f = open(sys.argv[1] + "extracted.zip", "wb")
    f.write(binascii.unhexlify(extractedArray[1]))


