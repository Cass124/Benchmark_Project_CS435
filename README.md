# Benchmark_Project_CS435

## GUI Parser and Highlighter

This program will take xml and png file pairs and return a folder containing new png files with all leaf leel GUI components highlighted in yellow.


## Setup and Running
Before running the xml_parser.py file, please run the following code snippet
`pip install -r requirements.txt`
This will intall all dependencies needed for this file.

The xml_parser file can be run with the following code snippet
`python xml_parser.py`

## Background
BeautifulSoup: I opted to use BeautifulSoup to parse the xml files since some contain errors, such as missing tags, which BeautifulSoup can handle better than otehr libraries such as lxml or xml ElementTree.
Since some of the xml files contain errors, such as missing tags, I have opted to use BeautifulSoup, since it can handle malformated xml files. 