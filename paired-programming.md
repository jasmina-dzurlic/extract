# Paired Programming Assignment - 3amMcspicy

### Goal of the project:
The goal of the project is to parse research papers quickly to extract the gps coordinates of the sample locations and plotting them on a map. A module that I found that could be useful is Camelot that extracts tables from PDF files as well. As for plotting, I would suggest geopandas for creating the points. 

### The Data:
There is an example of the research paper in the repo. There is also a picture of the table as an example of the data that is being extracted and a map with red dots as a result of plotting the coordinates. 


### The Code:
No code has been written so far

### Does the current code include a proper skeleton (pseudocode) for starting this project? What can this code do so far?

Not skeleton code yet.

### Code contributions/ideas: 
I see that you have a problem with installing it. I think it is because you don't have an setup.py file.

I imagine that this program could work as a command line interface where it would execute like this:

extract.py research_paper.pdf

and a map would be displayed.

In this case, a starting point would be writing the argument parser in the code. 