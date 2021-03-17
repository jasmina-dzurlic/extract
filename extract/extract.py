#!/usr/bin/env python

"""
A function to extract GPS coordinates from a PDF table and outputting a CSV file with coordinates and plotting to a map
"""

# First step in creating program is to extract the relevant infromation from a PDF table 

import tabula
import pandas as pd 
import os

# create a pdf path to the documents folder where you will have your PDF documents
 
#pdf_path =os.relativepath(/project/documents/MurphyRTL2017.pdf)

pdf_path = "https://link.springer.com/content/pdf/10.1007/s10764-017-9967-8.pdf"

# create a table variable and read all the pages and extract all the tables from the PDF 

all_tables = tabula.read_pdf(pdf_path, pages = "all", stream = True)

all_tables.head()
# read the first table with coordiantes into a dataframe
