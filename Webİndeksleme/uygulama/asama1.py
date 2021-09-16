from . import parse

def hesapla(url):
    return parse.to_wordlist(url,remove_stopwords=True)
