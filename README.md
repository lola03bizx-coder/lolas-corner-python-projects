# Word Length Histogram

A Python program that reads a text file, analyses the lengths of words in the text, and visualises the results as a histogram using the TPlot graphics library.

The program processes the text by removing punctuation, converting all words to lowercase, and counting how many words occur at each length. The results are displayed graphically as a histogram where:

X-axis: Word length (number of characters)

Y-axis: Frequency of words with that length

This project demonstrates text preprocessing, data analysis, and graphical visualisation in Python.

# Features

- Reads text from a file

- Removes punctuation and normalises case

- Counts the frequency of each word length

- Displays results as a graphical histogram

- Automatically scales axes based on the data

- Uses multiple colours to distinguish bars

- Displays axis labels, title, and legend

# How It Works

The program reads a text file.

Punctuation is removed and text is converted to lowercase.

Words are split and their lengths are measured.

A dictionary stores the frequency of each word length.

A histogram is drawn using TPlot.

Example dictionary output:

Word Length Counts: {1: 5, 2: 12, 3: 18, 4: 9, 5: 7}

# Example Output

The histogram includes:

- Colored bars representing word length frequency

- Word length labels on the X-axis

- Frequency values on the Y-axis

- Counts displayed above each bar

- Legend explaining the graph

# Learning Goals

This project demonstrates:

- File handling in Python

- Text preprocessing

- Dictionaries and counting algorithms

- Basic data visualisation

- Modular program design

- Graphics with TPlot

# What's next?

- Support for large text datasets

- Export histogram as an image

- Interactive UI for selecting files

- Additional text statistics (average word length, most common length)

- Option to plot other distributions (word frequency, sentence length)
