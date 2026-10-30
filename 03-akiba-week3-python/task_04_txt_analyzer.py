
text = input("Enter text: ")

def clean_text(text):
    punctuation = ".,!?;:'\"()-"

    for char in punctuation:
        text = text.replace(char, "")

    return text


def count_words(text):
    number_of_words = len(text.split())
    return number_of_words


def count_character(text):
    count_char = 0
    punctuation = ".,!?;:'\"()-"

    for char in text:
        if char.isspace() or char in punctuation:
            continue
        else:
            count_char += 1

    return count_char


def count_vowel_consonant(text):
    count_vowel = 0
    count_consonant = 0
    vowels = ["a", "e", "i", "o", "u"]

    for char in text.lower():
        if char in vowels:
            count_vowel += 1
        elif char.isalpha():
            count_consonant += 1

    return count_vowel, count_consonant


def longest_word(text):
    words = clean_text(text).split()

    if not words:
        return "No words found"

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def repeated_words(text):
    words = clean_text(text).lower().split()
    number_of_repeated = []

    for word in words:
        count = 0

        for txt in words:
            if word == txt:
                count += 1

        already_counted = False

        for repeated in number_of_repeated:
            if word == repeated[0]:
                already_counted = True
                break

        if count > 1 and not already_counted:
            number_of_repeated.append([word, count])

    return number_of_repeated


def most_frequent_words(text):
    words = clean_text(text).lower().split()
    results = []

    for word in words:
        count = 0

        for txt in words:
            if word == txt:
                count += 1

        already_counted = False

        for item in results:
            if word == item[0]:
                already_counted = True
                break

        if not already_counted:
            results.append([word, count])

    results.sort(key=lambda item: item[1], reverse=True)

    return results[:5]


print("WORDS:", count_words(text))
print("CHARACTERS (excluding whitespace and punctuation):",
      count_character(text))

vowels, consonants = count_vowel_consonant(text)
print("VOWELS:", vowels)
print("CONSONANTS:", consonants)

print("LONGEST WORD:", longest_word(text))
print("REPEATED WORDS:", repeated_words(text))

print("FIVE MOST FREQUENT WORDS:")
for item in most_frequent_words(text):
    print("Word:", item[0], "| Number of appearances:", item[1])
