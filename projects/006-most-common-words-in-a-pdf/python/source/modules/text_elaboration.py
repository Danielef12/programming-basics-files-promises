import string


def clean_text(text: str) -> list[str]:
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    words = text.split()
    return words


def word_count(words: list[str]) -> dict[str, int]:
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    return words_count
