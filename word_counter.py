def word_frequency(text: str) -> dict:
    words = text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = word_frequency(sentence)

    for word, count in result.items():
        print(f"{word}: {count}")
