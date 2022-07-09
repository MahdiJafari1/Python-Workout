def get_sv(filename):
    vowels = {"a", "e", "i", "e", "u"}

    return {word.strip() for word in open(filename) if vowels < set(word.lower())}
