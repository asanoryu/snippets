
input_dir = '.'

#only files from dir
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]

# find file in dir and subdirs
import os

filename = 'test.txt'

for root, dirs, files in os.walk(input_dir):
	if filename in files:
		print("The file is present.")
	else:
		print("No such filename present.")

# find all files with extension
import os

extension = 'exe'
location = os.listdir(input_dir)

for files in location:
	if files.endswith(extension):
		print(files)

#find kword in file
import operator

fname = 'text.txt'
kword = 'find'
linedict = {}

ff = open(fname, 'r', encoding = 'utf-8')
fflist = list(enumerate(ff, start = 1))

for line in fflist:
	if kword in line[1]:
		print(line[0], line[1])
		

linedict = {line[0]: line[1].rstrip("\n") for line in fflist if kword in line[1]}
linedict = sorted(linedict.items(), key = operator.itemgetter(0)) #order by key

print(linedict)
