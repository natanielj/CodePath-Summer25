# Problem: Given a list of strings, words, group the strings that are anagrams of a each other

def group_anagrams():
    anagrams = []
    return 0

# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, seq):
    n = 0 # for every num in list
    for l in lst: # subseq index
        if (seq[n] == l): 
            n += 1 # if subseq[n] = lst[i] bool is true
    
    if (n == len(seq)): # else bool is false
        return True
    else:
        return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values. keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.
def create_dictionary(keys, values):
    #init a dictionary
    dictionary = {}
    #go thru keys in loop of len(keys):
    for i in range(len(keys)):
        dictionary[keys] = values[i]
        #append to dictionary in key value pairs


    return dictionary

def cooler_dictionary(keys, values):
    new_dict = {}
    for i in keys:
        new_dict.update({keys[i]: values[i]})
    return new_dict


keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
print(cooler_dictionary(keys, values))
