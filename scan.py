import os
import glob
from base import *
import argparse
import time

parser = argparse.ArgumentParser(description="Compare and optionally delete similar images",usage='This Python program allows to compare a huge number of images using their hash to evaluate '
    +'their similarity. You can tell the program to compare several hash size to evaluate the result prior to delete the images. '+
    'Use hashlist parameter in the form 6,8,20 or more values to get a count of how many images would be left using different hashes.')
parser.add_argument("imagePath",help="Define the source path for images to compare/delete")
parser.add_argument("hashlist",help="List of preferred hash size to evaluate image difference (6,8,20,50) NO SPACES ALLOWED")
parser.add_argument("--removesimilarimages",action="store_true",help="With this parameter the program will delete identical images using the first hash size you specified")
args = parser.parse_args()

hash_size_tuple=(4,6,8,20)
if len(args.hashlist)>0:
    print(f"Working on hash size: {args.hashlist}")
    hash_size_tuple=tuple(map(int, args.hashlist.split(',')))
mypath=""
if len(args.imagePath)>0:
    mypath=args.imagePath

print(f"Scan source path: {mypath}")
filelist = glob.glob(mypath)
if len(filelist)<=1:
    print(f"Unable to find any file")
    exit(1)
print(f"Found {len(filelist)} images")
if args.removesimilarimages:
    hash_size_tuple=tuple(list(hash_size_tuple)[:1])
    print(f"To remove similar images will be used {hash_size_tuple} hash size")
    print(f"Deleting images can result in the loss of important data. Are you sure you want to delete similar images in the path mentioned above? No guarantee of good functioning by the developer. Did you make a backup?")
    answ=input("Would you like to continue? (yes/*):")
    if answ!="yes":
        print("Terminated")
        exit(2)
    
        

for aHash in hash_size_tuple:
    dhash_z_transformed = with_ztransform_preprocess(imagehash.dhash, hash_size = aHash)

    
    resultList=[]
    
    fileprev=""
    startTime = time.time()
    filecount=0
    for thisFile in sorted(filelist): 
        filecount+=1
        if startTime!=time.time():
                print(f"Working on image {filecount}, ({int(filecount/len(filelist)*100)}%)",end="\r")
        if not fileprev:
            fileprev=thisFile
            hash1=dhash_z_transformed(fileprev)
        else:
            #hash1=dhash_z_transformed(fileprev)
            hash2=dhash_z_transformed(thisFile)
            if hash1==hash2:
                #stesso hash, non fare nulla
                if args.removesimilarimages:
                    os.rename(thisFile,thisFile+".similar")
            else:
                resultList.append(thisFile)
                fileprev=thisFile
                hash1=dhash_z_transformed(fileprev)
    if args.removesimilarimages:
        print(f"Using size: {aHash} {len(resultList)} images are kept")
    else:
        print(f"Hash size: {aHash} will remains {len(resultList)} images")
