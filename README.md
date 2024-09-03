# Benchmark_Project_CS435

## GUI Parser and Highlighter

This program takes pairs of xml and png files and returns a folder containing new png files with all leaf level GUI components highlighted in yellow. 


## Setup and Running
Before running the xml_parser.py file, please run the following code snippet
`pip install -r requirements.txt`
This will install all dependencies needed for this file.

The xml_parser file can be run with the following code snippet
`python xml_parser.py`

## Background
BeautifulSoup: I opted to use BeautifulSoup to parse the xml files since some contain errors, such as missing tags, which BeautifulSoup can handle better than other libraries such as xml ElementTree.
Since some of the xml files contain errors, such as missing tags, I have opted to use BeautifulSoup, since it can handle malformated xml files. 
https://realpython.com/python-xml-parser/#beautifulsoup-deal-with-malformed-xml
https://www.roborabbit.com/blog/how-to-use-beautifulsoups-find-and-find-all-method/

OS: OS is used so that the program can read files from the current working directory in order to make the xml, png file pairs, and to help with creating a new folder for the highlighted pngs to reside.
https://www.geeksforgeeks.org/os-module-python-examples/

PIL: Pillow is used for marking up the png files. Using Image and ImageDraw from PIL, the program can draw rectangles using the previously extracted bound coordinates to highlight each leaf level GUI component.
https://www.geeksforgeeks.org/python-pillow-tutorial/
https://www.geeksforgeeks.org/python-pil-imagedraw-draw-rectangle/