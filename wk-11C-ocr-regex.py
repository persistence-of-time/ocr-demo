## import libraries
import re
from PIL import Image
import pytesseract ## python interface for tesseractpip insta
import os ## navitage, create directories
import shutil ## to delete the image folders with their imgs
from pdf2image import convert_from_path ## to turn pdf to image
import glob ## to glob files into a list
from pathlib import Path ## to specify path to your files
from natsort import natsorted, ns ## natural sorting
from kiwano import ocr

print("Hello world!")

## Single file test
## Nixon Document

# ocr.ocr_file("practice-docs/nixon-memo1.pdf", "nixon.txt")

# ocr.ocr_file("practice-docs/columbus_bank_trust.pdf", "columbus_bank.txt")


## Multifile test
## Nixon docs

# nixon_docs = glob.glob("practice-docs/nixon*.pdf")
# print(nixon_docs)

## run multi file kiwano on list
# ocr.ocr_files(nixon_docs, "multi-nixon.txt")


## glob files together

## how many files


## run kiwano ocr function. remember language and resolutions have default values.


## name of expored file

'''Back to original California finance files'''



## glob files together

#cal_files = glob.glob("docs/*.pdf")
#print(cal_files)

## how many files

#print(len(cal_files))

#ocr.ocr_files(cal_files, "cal_revenue.txt")

## run kiwano ocr function. remember language and resolutions have default values.


## name of exported file
file_name = "output/cal_revenue.txt"
with open(file_name, "r") as mytext:
    all_text = mytext.read()

print(all_text)

## pull into a variable all the text


## regex to capture alcohol numbers i used \S which captures any ***non-space*** characters in case the OCR turns out strange characters



## Method 1 pattern.findall(source_text)


#print 

## check to see if equal to number of files


## regex to capture date
## i used literals for the months


## dates list and print it


## check to see if equal to number of files



## run regex within list comprehension



## convert to dataframe


## export to csv

##BACK TO JUPYTER NOTEBOOK