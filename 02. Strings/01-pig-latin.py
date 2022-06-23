# def pig_latin():
#     """ My Solution

#     Returns:
#         string: word in pig latin
#     """
#     word = input("Enter an English word: ")
#     if word.startswith(("a", "e", "i", "o", "u")):
#         word = f"{word}way"
#     else:
#         word = f"{word[1:]}{word[0]}ay"

#     print(word)
#     return word

# pig_latin()


# def pig_latin(word):
#     """The book solution

#     Returns:
#         string: word in pig latin
#     """
#     if word[0] in "aeiou":
#         return f"{word}way"
#     return f"{word[1:]}{word[0]}ay"


# print(pig_latin('python'))
