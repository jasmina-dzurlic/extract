#!/usr/bin/env python

"""
A function to extract GPS coordinates from a PDF and outputting a CSV file with coordinates and plotting to a map
"""

# First step in creating program is to extract the relevant infromation from a PDF 

from tika import parser
import os

# create a pdf path to the documents folder where you will have your PDF documents
# pdf_path = os.path.realpath("../project/documents/MurphyRTL2017.pdf")
# opening up PDF with tika parser
# parsed_pdf = parser.from_file(pdf_path)
# saving content of PDF
# data = parsed_pdf['content']

def extract(pdf_path):
    """This function will extract the content from a PDF file and retrun it
    when given a path"""
    # opening up PDF with tika parser
    parsed_pdf = parser.from_file(pdf_path)
    # saving content of PDF
    data = parsed_pdf['content']  # Does the pdf have to be organized and sparsed when uploaded or would some code here to parse and select certain values 
                                  # of the pdf be useful to the user? 
    return(data)

# asks user to import the path to pdf that they want extract to get the content from (remeber to have .pdf at end of file --add
# that to the help section)
pdf_path = input("Please input full pdf path \n").lower()

-------
# We discussed in out paired-programming meetings that once you are able to extract and convert decimal GPS points, your goal
# will be to plot these. In our group meeting, Jared mentioned the plotting program Folium. 

# Here is an example of plotting longitude and latitude points using folium

import folium
mapit = None
latlon = [ (51.249443914705175, -0.13878830247011467), (51.249443914705175, -0.13878830247011467), (51.249768239976866, -2.8610415615063034)]
for coord in latlon:
    mapit = folium.Map( location=[ coord[0], coord[1] ] )

mapit.save( 'map.html')

-------
