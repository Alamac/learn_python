

with open('referat.txt', 'r', encoding='utf-8') as referat:

    file_string = referat.read()

    file_list = file_string.split()

    wordcount = len(file_list)

    file_string = file_string.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as referat2:
    referat2.write(file_string)

print(wordcount)

