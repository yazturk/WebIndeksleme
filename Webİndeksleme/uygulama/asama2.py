from . import parse, stopwords

def hesapla(url):
        stringlist = parse.to_stringlist(url)
        points = {}
        for string in stringlist:
                words = string.lower().split()
                frequencies = {}
                total = 0
                for word in words:
                        if not word in stopwords.english and not word[0].isdigit():
                                total += 1
                                increase(frequencies, word, 1)
                update(points, frequencies, total)
        p = list(points.items()) #sıralamak için listeye çevir
        p.sort(reverse=True, key=sort_f)
        return p

def increase(dictionary, key, point):
        if key in dictionary.keys():
                dictionary[key] += point
        else:
                dictionary[key] = point

def update(points, freqs, total):
        for word in freqs.keys():
                point = freqs[word] * freqs[word]
                increase(points, word, point)
                
def sort_f(pair):
        (key, value) = pair
        return value
