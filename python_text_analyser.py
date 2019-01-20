"""
Counts the total numbers of words and the use of defined words in a given set of texts, based on the directory
 path which is passed. Glob is used to retrieve the list of *.txt files in a given path

Usage:
    Update the following variables:
        directory_path: a directory path which contains one or more *.txt files
        search_words_list: list of words to search for the number of times they occur in each text file

    python3 <script.py>
"""


def analyse_books_in_path(path, *search_words):
    """
    Function to count the total number of words and instances of certain words in a given text file

    Arguments:
        path:           the absolute path to a directory which contains one or more *.txt files
        search_words:   an arbitrary number of strings to search for within the text (number of times used)
    """

    import glob

    # Suffix the path with the correct glob expression to search for only text files
    # Check whether we need to apply a trailing "/" character or not first
    if path[-1] == "/":
        glob_path = path + "*.txt"
    else:
        glob_path = path + "/*.txt"

    # Retrieve the list of files with a *.txt extension in the path argument
    books = glob.glob(glob_path)

    # Iterate through the books (if the list isn't empty)
    if books:
        for book in books:

            print("Analysing book:", book)

            # Open the file and read as a string for later processing. Throw an exception if unable to access file
            try:
                with open(book) as file_object:
                    contents = file_object.read()
            except FileNotFoundError:
                print("WARNING: file not found:", book, "\n")
            else:
                # Calculate the total number of words in the text by splitting the string into a list
                #  using a space deliminator. Then check the length of the list
                in_words = contents.split()
                number_of_words = len(in_words)
                print("The approx. number of words in", book, "is", number_of_words)

                # Calculate the number of instances of the 'search_words' parameters in the text
                #  This is an arbitrary number passed to the function
                if search_words:
                    for search_word in search_words:
                        # Convert to lowercase before searching
                        search_word_count = contents.lower().count(search_word)
                        print("The word '" + search_word + "' appears", search_word_count, "times in this text")
                else:
                    print("INFO: No search_words parameters were passed")

            print()
    else:
        print("No files with *.txt extensions found in path:", path)


# Only execute the following if running the script directly,
# rather than imported by a unittest based class for example
if __name__ == '__main__':
    # Directory the books are stored in. Function will search for *.txt files in this directory
    # Provide an absolute path
    directory_path = '/Users/michael.price/Downloads'

    # Word(s) to search for within the text
    search_words_list = ['the', 'and', 'sherlock']

    # Call the function. Prefix search_words_list with * to expand list before passing arguments
    analyse_books_in_path(directory_path, *search_words_list)
