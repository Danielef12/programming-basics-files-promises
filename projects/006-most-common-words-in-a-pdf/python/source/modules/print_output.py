def print_words_count(words_count: dict[str, int], top_n: int) -> None:
    sorted_words_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words_count[:top_n]:
        print(f"{word}: {count}")
