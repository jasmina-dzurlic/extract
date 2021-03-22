# `extract`

This program will accomplish three things: (1) read a PDF and extract sample location names and GPS coordinates; (2) convert to decimal deggrees format, and (3) plot converted coordinates to a map. 

---
## Requirements

Java version 7 is needed for python package `tika`. To install use: 

`pip install tika`

### In development 

Developers can install and test the program using `git clone`

`git clone git@github.com:aparnac25/extract.git`

once cloned change directory `cd ./extract/` and run `python extract.py` in terminal. It will input you to enter in a path to the PDF you wish to upload. That is as far as I have gotten. I am currently trying to extract out the GPS coordinates using `regex` 


## Not working 

Currently the `pip install` is not working. Hopefully soon one can use below code to run on command line.

`cd ./extract`

`pip install -e .`



