"""
File: anagram.py
Name: Janelle
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    print('Welcome to stanCode "Anagram Generator" (or ' + str(EXIT) + ' to quit)')
    while True:
        entered = str(input('Find anagrams for: ')).lower()
        if not entered == EXIT:

            start = time.time()
            find_anagrams(entered)  # Look for anagrams
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')

        else:
            break


def read_dictionary(s):
    """
    :return: the result of file reading
    """
    dictionary = []
    with open(FILE, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) == len(s):
                dictionary.append(word)
    dictionary = set(dictionary)
    return dictionary


def find_anagrams(s):
    """
    :param s: Input string to be looked up for anagrams
    :return: None
    """
    anagram_list = []
    sub_dic = read_dictionary(s)  # Create a split of original dict contains words in the same length as s only
    print('Searching...')
    find_anagrams_helper(s, anagram_list, '', sub_dic, [])  # Use helper to find anagrams
    print(f"{len(anagram_list)} anagrams: {anagram_list}")


def find_anagrams_helper(word, anagram_list, temp_result, dictionary, index_list):
    """
    :param word: The word entered to look up in dictionary
    :param anagram_list: The dictionary that save results from duplication
    :param temp_result: The list that save temporary results for prefix look up
    :param dictionary: The list in which we look for anagrams
    :return: None
    """
    if len(temp_result) == len(word):
        if temp_result in dictionary and temp_result not in anagram_list:
            print('Found: ' + temp_result)
            print('Searching...')
            anagram_list.append(temp_result)

    else:
        for i in range(len(word)):
            if i not in index_list:
                # choose
                index_list.append(i)
                temp_result += word[i]

                # explore
                # if has_prefix(temp_result, dictionary):
                find_anagrams_helper(word, anagram_list, temp_result, dictionary, index_list)

                # un-choose
                index_list.pop()
                temp_result = temp_result[:-1]


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: The sub-string to be looked up in dictionary
    :return: True/False
    """
    found = False
    for word in dictionary:
        if word.startswith(sub_s):
            found = True
            break

    return found


if __name__ == '__main__':
    main()
