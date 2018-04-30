# BigDataAnalysis-Yelp-Academic-Dataset-Round7-using-MapReduce
The Yelp dataset round 7 consists of 5 problems , which are solved by using mapReduce in hadoop.

HADOOP SETUP is done on windows.
The instructions for Setup in windows is uploaded above.

Eclipse is used as an IDE.

Dataset : Yelp Dataset : https://www.yelp.com/academic_dataset
Once the dataset is downloaded it is extracted and file named "yelp_dataset" with extension type "File" is extracted.
rename this with extenion ".tar" and extract it again, you will get the dataset in JSON format.

The JSON files (User,Business,Review) are extracted and converted into CSV files. Further, these three files are merged together and the input file "out-put.csv" is made.

Analyzed yelp dataset to derive useful statistics about "user”, “business" and "review" entities. Dataset was stored in Hadoop HDFS. Designed Map Reduce java programs for following concepts:

Problem 1 : Counting & Filtering Data : Counted number of entities

