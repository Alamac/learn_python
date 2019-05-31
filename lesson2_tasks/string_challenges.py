# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
last_digit = word[-1]
print (last_digit)

# Вывести количество букв а в слове
word = 'Архангельск'
# ???
lenght = len(word)
print(lenght)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = ['а', 'е', 'ё', 'и', 'у', 'о', 'э', 'ю', 'я', 'ы']
vowel_letters = 0
word = word.lower()
for letter in word:
    if letter in vowels:
        vowel_letters += 1
print(vowel_letters)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
words_count = sentence.split()
print(len(words_count))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
split_sentence = sentence.split()
for word in split_sentence:
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
split_sentence = sentence.split()
letters_count = []
for word in split_sentence:
    letters_count.append(len(word))

avg_letters_in_sentence = sum(letters_count) / len(letters_count)

print(avg_letters_in_sentence)