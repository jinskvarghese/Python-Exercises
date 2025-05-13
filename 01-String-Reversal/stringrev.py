# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"

def reverse(sentence):
    words=sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


sentence = "Python is Awesome"
reversed_words_sentence = reverse(sentence)
print(reversed_words_sentence)