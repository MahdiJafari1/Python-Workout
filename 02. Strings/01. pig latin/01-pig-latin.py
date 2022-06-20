def pig_latin():
    word = input("Enter an English word: ")
    if word.startswith(("a", "e", "i", "o", "u")):
        word = f"{word}way"
    else:
        word = f"{word[1:]}{word[0]}ay"

    print(word)
    return word


pig_latin()
