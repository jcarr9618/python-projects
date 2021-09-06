import urllib.request

def story_func ():
    tale = urllib.request.urlopen ('http://sixty-north.com/c/t.txt')
    tale_words = []
    for line in tale:
        tale_words = line.decode('utf8').split()
        for word in tale_words:
            tale_words.append(word)
    tale.close
    for word in tale_words:
        print(word)


