# python-text-analyser
Python script to calculate the total number of words and also the number of uses of supplied words (e.g. how many times does 'the' appear in the text) in a given set of text files.
The script gathers a list of text files by globbing a path specified by the user.

I have used the following online repo for testing purposes which includes a number of online texts such as 'Sherlock Holmes' in the public domain:
http://www.gutenberg.org/

Usage:
Update the following variables:
- `directory_path`: a directory path which contains one or more *.txt files
- `search_words_list`: list of words to search for the number of times they occur in each text file

    python3 python-text-analyser.py
