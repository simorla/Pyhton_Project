from urllib.request import urlopen
def fect_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    store_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
	        store_words.append(word)
    story.close()
    for words in store_words:
        print(words)




