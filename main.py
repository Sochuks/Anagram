# An Anagram of a word contains the same letters that make up the word.
# EXAMPLE: Pots, Spots 
# This program checks if two words are anagrams
# Outputs True or False 

# Collect First Word
word1 = input("Enter First Word: ")

# Collect Second word
word2 = input("Enter Second Word: ")


def find_anagram(word, anagram):
    # Set word as a list
    word=list(word)

    #Set anagram as a list 
    anagram = list(anagram)

    return (sorted(word)==sorted(anagram)) 
    

print(find_anagram(word1, word2))
