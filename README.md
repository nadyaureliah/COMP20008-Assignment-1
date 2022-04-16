# COMP20008 2021 Semester 1 Assignment 1

This project consists of two parts – Part A and Part B. 

## Part A
Part A pre-processes and visualizes "Our World in Data COVID-19 dataset" ("owid-covid-data.csv", available for download from this [link](https://covid.ourworldindata.org/data/owid-covid-data.csv)). This part consists of:

### • parta1.py (Data Pre-processing)
Which prints the first 5 rows of the final dataframe to the standard output and saves a new dataframe "owid-covid-data-2020-monthly.csv" in the same directory as the python program. The program should be called from the command line as follows:

```bash
python parta1.py owid-covid-data-2020-monthly.csv
```

### • parta2.py (Visualization)
Which visualizes the new dataframe obtained from parta1.py, "owid-covid-data-2020-monthly.csv", to produce two scatter plots. The program should be called from the command line as follows:

```bash
python parta2.py scatter-a.png scatter-b.png
```

## Part A
Part B is a search engine that allows users to specify keywords and find all articles in relation to the keywords. The cricket dataset is needed and can be downloaded from the LMS. This part consists of:

### • partb1.py (Data Pre-processing)
Which produces a new dataframe "partb1.csv" containing the filenames and Document IDs of each document in the dataset. The program should be called from the command line along with the name of the CSV file:

```bash
python partb1.py partb1.csv
```

### • partb2.py (Pre-Processing)
Which pre-processes article in the cricket folder from the specified file in the input command.
The program should be called from the command line along with the filename of a document (only one filename at a time). For example:

```bash
python partb2.py cricket001.txt
```

### • partb3.py (Basic Search)
Which allows users to search for articles containing particular keywords (between 1 and 5 keywords, separated by whitespace character), and returns the document IDs of the documents that contain all the keywords in the search query. Your program should be called from the command line along with the keywords being searched for. For example:

```bash
python partb3.py keyword1 keyword2 keyword3
```

### • partb4.py (Advanced Search)
Which allows users to search for articles containing particular keywords that enables inexact matching (between 1 and 5 keywords, separated by whitespace character), and returns the document IDs of the documents that contain all the keywords in the search query, or words considered to have the same base. Your program should be called from the command line along with the keywords being searched for. For example:

```bash
python partb4.py keyword1 keyword2 keyword3
```

### • partb5.py (Search Rankings)
Which allows users to search for articles containing particular keywords that enables inexact matching (between 1 and 5 keywords, separated by whitespace character), and returns the document IDs of the documents that contain all the keywords in the search query, or words considered to have the same base, ranked by cosine similarity scores in descending order. Your program should be called from the command line along with the keywords being searched for. For example:

```bash
python partb5.py keyword1 keyword2 keyword3
```

## Dependencies
• argparse (partb1.py)
• nltk (partb3.py)
• math (found in partb5.py)
• sklearn (found in partb5.py)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
