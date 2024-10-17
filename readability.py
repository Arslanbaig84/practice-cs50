# TODO
def main():
    string = input("Input Text: ")

    letters = count_letters(string)
    print(f"Letters: {letters}")

    words = count_words(string)
    print(f"words: {words}")

    sentences = count_sentences(string)
    print(f"sentences: {sentences}")

    L = letters/words * 100
    S = sentences/words * 100

    index = 0.0588 * L -0.296 * S - 15.8
    print(f"Index: {index}")

    index = round(index)
    print(f"Index: {index}")

    check_value(index)


def count_letters(string):
    letter_count = 0

    for letter in string:
        if letter.isalpha():
            letter_count += 1
    print(f"letters: {letter_count}")
    return letter_count


def count_words(string):
    word_list = string.split()
    num_words = len(word_list)
    return num_words


def count_sentences(string):
    num_sentences = 0
    for character in string:
        if character in [".", "!", "?"]:
            num_sentences += 1
    return num_sentences


def check_value(index):
    match index:
        case _ if index < 1:
            print("Before Grade 1")
        case 1:
            print("Grade 1")
        case 2:
            print("Grade 2")
        case 3:
            print("Grade 3")
        case 4:
            print("Grade 4")
        case 5:
            print("Grade 5")
        case 6:
            print("Grade 6")
        case 7:
            print("Grade 7")
        case 8:
            print("Grade 8")
        case 9:
            print("Grade 9")
        case 10:
            print("Grade 10")
        case 11:
            print("Grade 11")
        case 12:
            print("Grade 12")
        case 13:
            print("Grade 13")
        case 14:
            print("Grade 14")
        case 15:
            print("Grade 15")
        case 16:
            print("Grade 16")
        case _ if index > 16:
            print("Grade 16+")


main()