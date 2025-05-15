# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

def reverse_with_case(sentence):
    def reverse_word_with_case(word):
        upper_indices = [i for i, c in enumerate(word) if c.isupper()]
        reversed_chars = list(word.lower()[::-1])
        for i in upper_indices:
            if i < len(reversed_chars):
                reversed_chars[i] = reversed_chars[i].upper()
        return ''.join(reversed_chars)

    words = sentence.split()
    reversed_words = [reverse_word_with_case(word) for word in words]
    return ' '.join(reversed_words)

# sample test
sentence = "Python is Awesome"
print(reverse_with_case(sentence))
