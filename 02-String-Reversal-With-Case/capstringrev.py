# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

def reverse(sentence):
    words=sentence.split()
    reversed_words = [word.lower()[::-1].capitalize() for word in words]
    return ' '.join(reversed_words)


sentence = "Python is Awesome"
reversed_words_sentence = reverse(sentence)
print(reversed_words_sentence)