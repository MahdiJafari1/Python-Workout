# # MY SOLUTION
# def pl_sentence(sentence):
#     sentence = list(sentence.split())
#     result = []
#     for word in sentence:
#         if word.startswith(("a", "e", "i", "o", "u")):
#             result.append(f"{word}way")
#         else:
#             result.append(f"{word[1:]}{word[0]}ay")
#     return " ".join(result)


# print(pl_sentence("this is a test translation"))
# # Exptected output: histay isway away estay ranslationtay

# # BOOK SOLUTION
# def pl_sentence(sentence):
#     output = []
#     for word in sentence.split():
#         if word[0] in "aeiou":
#             output.append(f"{word}ay")
#         else:
#             output.append(f"{word[1:]}{word[0]}ay")
#     return " ".join(output)


# print(pl_sentence("this is a test"))


# COMBINATION SOLUTION
def pl_sentence(sentence):
    translated_text = []
    for word in sentence.split():
        if word[0] in "aeiou":
            translated_text.append(f"{word}ay")
        else:
            translated_text.append(f"{word[1:]}{word[0]}ay")
    return " ".join(translated_text)


print(pl_sentence("this is a test"))
