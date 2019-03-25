#this is a solution for Q6 

str = input("Please enter a sentence: ")

words = " ".join(words for i, words in enumerate(str.split())if not i%2)

words = " ".join(str.split()[::2])

print (repr(words))