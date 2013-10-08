""" ExportParser.py
	Parsing program that takes the Powerscribe attending template export text 
	files and separates them out to individual text files.

	This version was written by Shahein Tajmir while he was a medical student
	doing research at the Center for Evidence Based Imaging at Brigham and 
	Women's Hospital (CEBI @ BWH).    

	Comments will try and document everything as necessary.

	Last edited:  October 8, 2013
"""

from sys import argv
from bs4 import BeautifulSoup  # parses the HTML output from percipio
import csv 					   # read/write CSV files
import re 					   # allows for regex functionality

# ********************************************************************
# Start ExportParser.py here
# ********************************************************************

# Source TXT has 3 fields predictable structure.  Each template is separated
#   by $$$.  
# First job is to rip them apart.
# Second job is to save them as txt files

scriptname, fileName = argv

file = open(fileName)
text = file.read()

# Splits into a list of strings by the $$$\r\n delimiter
reports = re.split(r"\$\$\$\r?\n", text)
print "r= ", reports

# Read through the each report
for x in reports:
	print "x=", x
	# Get title matchobject. This has 3 groups, title, newlines, body
	xMatchObject = re.match(r"(.+)(\n)((\W|\w)+)", x)
	print "xMO =", xMatchObject, "end xMO"

	title = xMatchObject.group(1)
	print "t= ", title
	body = xMatchObject.group(3)
	print "b= ", body

	newfilename = title
	newfilename = newfilename.translate(None, '/\r')
	newfile = open(newfilename + ".txt", "wb")
	newfile.write(body)
	newfile.close()

file.close()