import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from collections import Counter
from . import stopwords

symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

def to_stringlist(url):
   source_code = requests.get(url).text
   soup = BeautifulSoup(source_code, 'html.parser')
   while soup.style:
        soup.style.extract()
   while soup.script:
        soup.script.extract()
   strings = [s for s in soup.strings]
   stringlist = []
   for s in strings:
        for symbol in symbols:
                s = s.replace(symbol, ' ')
        stringlist.append(s)
   return stringlist

def to_wordlist(url, remove_stopwords=False):
        wordlist = []
        strs = to_stringlist(url)
        for s in strs:
                words = s.lower().split()
                for w in words:
                        if (not remove_stopwords) or (not w in stopwords.english):
                                        wordlist.append(w)
        c = Counter(wordlist)
        return c.most_common()

def recursive_wordlist(url,derinlik):
   try:
        source_code = requests.get(url).text
        soup = BeautifulSoup(source_code, 'html.parser')
   except:
        return (url, [], [])
   else:
        while soup.style:
                soup.style.extract()
        while soup.script:
                soup.script.extract()
        suburlresults = []
        if derinlik > 1:
                for a in soup.find_all('a'):
                        newurl = a.get('href')
                        if newurl:
                                newurl = urljoin(url, newurl)
                                if newurl.startswith('http'):
                                    newres = recursive_wordlist(newurl,derinlik-1)
                                    suburlresults.append(newres)
        strings = [s for s in soup.strings]
        stringlist = []
        wordlist = []
        for s in strings:
                for symbol in symbols:
                        s = s.replace(symbol, ' ')
                stringlist.append(s)
                words = s.lower().split()
                for w in words:
                        if not w in stopwords.english:
                                wordlist.append(w)
        c = Counter(wordlist)
        print("Bitti: " + url)
        return (url, c.most_common(), suburlresults)
        
