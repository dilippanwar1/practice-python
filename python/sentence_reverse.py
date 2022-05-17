str = 'revereseme please'
word_list = str.split()
print(word_list)
reverse_list = word_list[:: -1]
print (reverse_list)
reverse_sentence = " ".join(reverse_list)
print (reverse_sentence)