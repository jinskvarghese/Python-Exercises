def reverse(sentence):
    words=sentence.split()
    reversed_words = [word.lower()[::-1].capitalize() for word in words]
    return ' '.join(reversed_words)


sentence = "Python is Awesome"
reversed_words_sentence = reverse(sentence)
print(reversed_words_sentence)