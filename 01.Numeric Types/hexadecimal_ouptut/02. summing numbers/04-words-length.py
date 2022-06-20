def summarize(words):
    words_length = [len(word) for word in words]
    return min(words_length), max(words_length), sum(words_length)/len(words_length)
