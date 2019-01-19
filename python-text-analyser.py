"""
Counts the total numbers of words and the use of defined words in a given set of texts

I have used the following online repo for testing purposes which includes a number of online texts in
the public domain:
http://www.gutenberg.org/

Usage:
    Update the books, directory_path & search_words_list variables and then run as usual

Tested on Python 3+
"""


def analyse_books(path, *search_words):
    """
    Function to count the total number of words and instances of certain words in a given text file

    Arguments:
        path:           the absolute path to the text to to be searched
        search_words:   an arbitrary number of strings to search for within the text (number of times used)
    """
    print("Analysing book:", path)

    # Open the file and read as a string for later processing. Throw an exception if unable to access file
    try:
        with open(path) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("WARNING: file not found:", path, "\n")
    else:
        # Calculate the number of words in the text by splitting the string into a list
        #  using a space deliminator
        in_words = contents.split()
        number_of_words = len(in_words)
        print("The approx. number of words in", book, "is", number_of_words)

        # Calculate the number of instances of the 'search_words' parameters in the text
        #  This is an arbitrary number passed to the function
        for search_word in search_words:
            # Convert to lowercase before searching
            search_word_count = contents.lower().count(search_word)
            print("The word '" + search_word + "' appears", search_word_count, "times in this text")
    print()


# File names of the books to search through
books = ['Moby Dick.txt', 'Pride and Prejudice.txt', 'Sherlock Holmes.txt']

# Directory the books are stored in
directory_path = '/path/to/file/'

# Word to search for within the text
search_words_list = ('the', 'and', 'sherlock')

# Iterate through the books and call the function (if the books list is not empty)
if books:
    for book in books:
        file_path = directory_path + book
        # Prefix search_words_list with * to expand the list before sending as an argument
        analyse_books(file_path, *search_words_list)
else:
    print("There are no books to process as the 'books' list is empty.")
