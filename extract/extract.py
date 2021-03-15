#!/usr/bin/env python

"""
A function to extract GPS coordinates from a PDF table and outputting a CSV file with coordinates and plotting to a map
"""

# First step in creating program is to extract the relevant infromation from a PDF table 

import tabula
import pandas as pd 
import os

# create a pdf path to the documents folder where you will have your PDF documents
 
relative_path = '/documents/Murphy2017.pdf'
current_dir = os.getcwd()
pdf_path = os.path.join(current_dir, relative_path)

print(pdf_path)

# create a table variable and read all the pages and extract all the tables from the PDF 

# all_tables = tabula.read_pdf(pdf_path, pages = "all", multiple_tables = True)