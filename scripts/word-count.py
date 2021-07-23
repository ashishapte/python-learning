"""string toeknizing and finding out unique words with their count """

my_text = ('this text has several words and each word may appear in one or more times '
            'this is second line for my text of several words')

# print(my_text.split())
word_count = {}

for word in my_text.split():
    if word not in word_count:
        word_count[word] = 1 # inserting new key/value pair
    else:
        word_count[word] += 1 # incrementing word count.

print(f'{"word":12}count')
for word, count in sorted(word_count.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words: ', len(word_count))
