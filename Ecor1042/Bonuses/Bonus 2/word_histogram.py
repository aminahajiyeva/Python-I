"""
ECOR 1042 Text Processing Exercises
Using a Dictionary to Implement a Histogram
"""
import string

# Exercise 1

def build_histogram(filename: str) -> dict[str, int]:
    """Return a histogram of the words in the specified file.

    (A histogram is a dictionary of counters. Each counter
    keeps track of the number of occurrences of one word.)

    Assume sample.txt contains:

    First line of text.
    Second line of text?
    Third line of text!

    >>> hist = build_histogram('sample.txt')
    >>> hist
    {'first': 1, 'line': 3, 'of': 3, 'text': 3, 'second': 1, 'third': 1}

    >>> len(hist)  # How many different words are in the file?
    6
    """
    # open and read in the file
    word_file = open(filename, 'r')
    # create an empty dictionary to store the histogram
    histogram = {}
    # for each line in the file seperate each word and store it
    for line in word_file:
        words = line.split()
        # for each word in the file, remove all the extra punctuation and put all letters in lower case
        for word in words:
            word = word.strip(string.punctuation).lower()
            # if the word is already in the histogram, add the counter to indicate this. Otherwise set the counter to one to show that only one word of its kind is present
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
    # close the file
    word_file.close()
    # return the histogram
    return histogram

# Exercise 2


def most_frequent_word(hist: dict[str, int]) -> tuple[str, int]:
    """Return a tuple containing the most frequently occurring word in the
    histogram hist (a dictionary of word/frequency pairs), along with its
    frequency.

    >>> hist = build_histogram('sample.txt')
    >>> most_frequent_word(hist)  # Which word occurs most often?
    ('line', 3)
    """

    # set a default max word
    most_freq_word = ""
    # set a default max frequency of the word
    max_frequency_of_word = 0
    
    # for each word in the histogram, reset its respective frequency
    for word in hist:
        frequency_of_word = hist[word]
        # if the frequency of the word exceeds the current maximum frequency, switch the variables accordingly
        if frequency_of_word > max_frequency_of_word:
            most_freq_word = word
            max_frequency_of_word = frequency_of_word

    # return the maximum frequency and its respectice word
    return (most_freq_word, max_frequency_of_word)


if __name__ == '__main__':
    most_frequent_word(build_histogram("whyEnglishIsSoHard.txt"))
