# Text-Analysis-Web-Scrapping

                                                                    INSTRUCTIONS

DATA EXTRACTION

•	I have created two python files. They are Data Extraction and Data Analysis.
•	I have used Requests and Beautiful Soup library for Data Extraction from the URL.
•	I have used the and ‘request.get(URL)’ and ‘soup.find()’ function to get the text from URL.
•	I removed “Blackcoffer Insights’’ block by using ‘decompose’ function.


DATA ANALYSIS

•	Firstly I have called the libraries. They are:
•	from nltk.sentiment import SentimentIntensityAnalyzer as sa
•	from nltk.tokenize import sent_tokenize
•	import pyphen
•	import string
•	from nltk.corpus import stopwords
•	import re

•	To open Text file, I have used ‘open’ and ‘read’ function.

•	With the help of ‘split’ function, I converted text files in to list.

•	With the help of ‘set’ and ‘len’ function, I got the list which has no stopwords.

•	After having no stopwords in the list, I got positive score and negative score.

•	With the help of ‘if’ and ‘for’ function, I have done all the calculations by using Text Analysis document.

•	I also added simple test for sentiment analyzer in the data analysis.py file by using Sentiment Intensity Analyzer from NLTK.

•	I have written the comments in python file to understand the program easily.



Finally, Thank you very much.



