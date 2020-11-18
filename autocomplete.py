# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:59:48 2020

@author: ralls
"""
"""
Your code must take user input and produce a list of up to 5 autocomplete options, or a message saying no results were found.
Your code must work using the my_history.txt file provided in the introduction, even if you also made it work on your own data.
Your code must use a trie to do the autocomplete
Your code must have an autocomplete() function that is recursive - providing the right arguments to this function can make all the difference!
You must be able to autocomplete at the word level or at the letter/character level. You should ask the user which they would like to do.
"""
import codecs

file_object = codecs.open('words.txt', 'r', encoding='utf8', errors='ignore')
content_string = file_object.readlines()
file_object.close()

trie = {'value' : '^', 'count' : 1, 'children' : {}}
test_list_c = content_string
test_list_w = content_string

def check_letter(trie, letter):
    child_tries = trie['children']
    if letter in child_tries:
        return True
    else:
        return False


def create_trie_c(word, trie):
    if len(word) == 0:
        return trie
    elif len(word) > 0:
        for num, letter in enumerate(word):
            i = check_letter(trie, letter)
            if i == False:
                trie['children'][letter] = {'value' : letter, 'count' : 1, 'children' : {}}
                return create_trie_c(word[1:], trie['children'][letter])
            else:
                trie['children'][letter]['count'] += 1
                return create_trie_c(word[1:], trie['children'][letter])


def create_trie_w(word, trie):
    if len(word) == 0:
        return trie
    elif len(word) > 0:
        i = check_letter(trie, word[0])
        if i == False:
            trie['children'][word[0]] = {'value' : word[0], 'count' : 1, 'children' : {}}
            return create_trie_w(word[1:], trie['children'][word[0]])
        else:
            trie['children'][word[0]]['count'] += 1
            return create_trie_w(word[1:], trie['children'][word[0]])
    

def search_c(word, trie, matches, word_list):
    if len(word) == 0:
        return matches
    for letter in word:
        if word[:] in trie['children']:
            for x in word_list:
                if word[0] == x[0]:
                    matches.append(x)
                else:
                    continue
        if letter in trie['children']:
            return matches
        else:
            return matches

def search_w(word, trie, matches, word_list):
    if len(word) == 0:
        return matches
    for letter in word:
        for x in word_list:
            if word[0] == x[0]:
                matches.append(x)
            else:
                continue
        if letter in trie['children']:
            return matches
        else:
            return []



choice = input('Would you like to search by word(w) or character(c)')
word = input('What is the word you want to find?')


if choice == 'c':
    for i in range(len(test_list_c)):
        create_trie_c(test_list_c[i], trie)
    matches = search_c(word, trie, [], test_list_c)


elif choice == 'w':
    for i in range(len(test_list_w)):
        create_trie_w(test_list_w[i].split(), trie)
    matches = search_w(word.split(), trie, [], test_list_w)
    
if len(matches) < 5:
    for i, match in enumerate(matches):
        print('\nMatch {}: {}'.format(str(i + 1), str(match)))
        
elif len(matches) > 5:
    for i in range(5):
        print('\nMatch {}: {}'.format(str(i + 1), str(matches[i])))
        
elif len(matches) == 0:
    print('There were no matches :(')
 