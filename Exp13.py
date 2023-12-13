def unique_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            unique_words = sorted(set(words))
            return unique_words
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []


def main():
    file_name = input("Enter the name of the text file: ")
    unique_words = unique_words_in_file(file_name)

    if unique_words:
        print("Unique words in the file (in alphabetical order):")
        for word in unique_words:
            print(word)
    else:
        print("No unique words found in the file.")


if __name__ == "__main__":
    main()