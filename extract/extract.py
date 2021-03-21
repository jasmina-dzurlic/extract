#!/usr/bin/env python

"""
A function to extract GPS coordinates from a PDF table and outputting a CSV file with coordinates and plotting to a map
"""

# First step in creating program is to extract the relevant infromation from a PDF 

from tika import parser
import pandas as pd 
import os

# create a pdf path to the documents folder where you will have your PDF documents

pdf_path = os.path.realpath("../project/documents/MurphyRTL2017.pdf")

# opening up PDF with tika parser

parsed_pdf = parser.from_file(pdf_path)

# saving content of PDF

data = parsed_pdf['content']

print(data)