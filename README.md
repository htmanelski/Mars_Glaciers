# Mars_Glaciers
A program I created that will allow you to map mid-latitude glaciers on Mars and gather detailed statistics.  

Glaciers will be a key source of water ice for future Martian colonists so I developed this tool to allow anyone to compare landing sites. 
Simply put in coordinates of your landing site and it will tell you the average distance to the nearest 'k' glaciers, 
map those glaciers, give you the total area of those glaciers, etc. 

The data is from the “2012 Glacier-Like Form Database”, the description of which is below:

“Martian glacier-like forms (GLFs) indicate that water ice has undergone deformation on the planet within its recent geological past. 
This database is the result of a comprehensive inventory of GLFs, derived from a database of 8058 Context Camera (CTX) images. 
The inventory identifies 1309 GLFs (727 GLFs in the northern hemisphere and 582 in the southern hemisphere) clustered in the mid-latitudes 
and in areas of rough topography.”

Citation: Souness, C. et al., 2012. An inventory and population-scale analysis of martian glacier-like forms. Icarus 217, 243–255. 
http://dx.doi.org/10.1016/j.icarus.2011.10.020.

Link: https://www.sciencedirect.com/science/article/abs/pii/S0019103511004131#!

The file "glaciers.py" will simply map all the glaciers found in this dataset and print out some graphs of useful statistics.

The file "distance_to_glaciers.py" is in my view much more interesting. What this program does is allow you to input a pair of longitude and latitude values 
and it will show a map of the nearest 10 glaciers on Mars, their total area, their average distance, along with other statistics. This is designed to let you
evaluate a particular landing site based on the number of glaciers nearby.

Note 1: you can see the author is careful to use the term “Glacier-Like form” rather than glacier. This is because for something to 
be a glacier it has to actually flow, and because for many of these features we are not sure the structure is currently moving 
Glacier-Like form is a more accurate term (https://www.sciencedirect.com/science/article/abs/pii/S0019103510004069?via%3Dihub).

Note 2: I am a applied math undergraduate student, not a professional programmer so I apoligize in advance for violating various design principles.
My goal was to create functioning and useful code. 
