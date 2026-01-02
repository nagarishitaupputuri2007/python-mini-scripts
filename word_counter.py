"""
word_counter.py

A simple utility script to calculate the frequency of words
in a given sentence.

This script is intended for daily Python practice and
demonstrates basic string processing and dictionary usage.
"""


def word_frequency(text: str) -> dict:
    """
    Calculate the frequency of each word in a given text.

    Args:
        text (str): Input sentence provided by the user.

    Returns:
        dict: A dictionary mapping words to their frequency count.
    """
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def main() -> None:
    """
    Main execution function.
    Reads input from the user and prints word frequencies.
    """
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("No input provided.")
        return

    result = word_frequency(sentence)

    print("\nWord Frequency:")
    for word, count in result.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
