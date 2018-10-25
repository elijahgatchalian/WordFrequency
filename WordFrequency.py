# Eli Gatchalian
# April 8, 2016
# CPSC 3400 - P1
# Version 1 - Python 3.5.1

# This program reads two files given in the command line and extracts
# words from both files. Any puncuation or digit is not read from 
# either file. The program then counts how frequent each word in both files 
# is used and outputs the results to the user sorted by high to low 
# frequency. The program outputs the words with the greatest
# frequency from both files and outputs the words that only occur once
# from either file.

import itertools
import sys
import string

def main():
    file_one = open(sys.argv[1], "r")
    file_two = open(sys.argv[2], "r")
    print ("COMPLETED: Part One: Read in two files")
    print ()
    punctuations = list(string.punctuation)
    nums = list(string.digits)
    
    list_one = []
    for line in file_one:
        line = ''.join(ch for ch in line if ch not in punctuations)
        line = ''.join(ch for ch in line if ch not in nums).lower()
        line.rstrip('\n')
        word = line.split()
        list_one.append(word)
    
    list_two = []
    for line in file_two:
        line = ''.join(ch for ch in line if ch not in punctuations)
        line = ''.join(ch for ch in line if ch not in nums).lower()
        line.rstrip('\n')
        word = line.split()
        list_two.append(word)
    print ("COMPLETED: Part Two: Extract words from files")
    print ()
           
    merge_list_one = list(itertools.chain.from_iterable(list_one))
    merge_list_two = list(itertools.chain.from_iterable(list_two))
    in_both_files = {}
    for word_one in merge_list_one:
        if word_one in merge_list_two:
            in_both_files[word_one] = merge_list_one.count(word_one) + merge_list_two.count(word_one)
    print("Part Three: Outputs lists of words that appear in both files")
    print (sorted(in_both_files))
    sorted_list = sorted(in_both_files.values(), reverse = True)
    print (sorted_list)
    print("COMPELTED: Part Three: Outputs list of words that appear in both files")
    print()
    
    print ("Part Four: Greatest frequency in both files and occuring only once in either file")
    print ("File One:")
    for word in merge_list_one:
        if merge_list_one.count(word) == 1:
            print ("Occured once:", word)
    print()
    print ("File Two:")
    for word in merge_list_two:
        if merge_list_two.count(word) == 1:
            print ("Occured once:", word)
    print()
    highest_frequency = sorted_list[0]
    for word in in_both_files:
        if in_both_files[word] == highest_frequency:
            print ("Highest Frequency (",highest_frequency,"): ",word)
    print ("COMPLETED: Part Four: Greatest frequency in both files and occuring only once in either file")
    
if __name__ == "__main__":
    main()