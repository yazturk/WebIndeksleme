from . import parse
from . import asama3, asama1

def hesapla(url1, urls):
        list1 = parse.to_wordlist(url1)
        sonuclar = []
        for url in urls:
                tree = parse.recursive_wordlist(url,2)
                sonuc = recursive_scoring(list1,tree)
                sonuclar.append(sonuc)
        siralisonuc = concat(sonuclar)
        siralisonuc.sort(reverse=True, key=sort_f)
        return (sonuclar, siralisonuc)

def concat(tree):
        dizi = []
        for (url, puan, rest) in tree:
                dizi.append((url,puan))
                dizi.extend(concat(rest))
        return dizi

def sirabul(url,siraliliste):
        sira=1
        for (url2,puan) in siraliliste:
                if url==url2:
                        return sira
                else:
                        sira+=1
        return 0 

def sort_f(pair):
        (key,value) = pair
        return value

def recursive_scoring(list1, tree2):
        (url2, list2, subs2) = tree2
        anapuan = asama3.hesapla(list1,list2)
        sonuclar = []
        for sub in subs2:
                sonuc = recursive_scoring(list1, sub)
                sonuclar.append(sonuc)
        sayac = 0
        toplam = 0
        for (url, puan, rest) in sonuclar:
                sayac += 1
                toplam += puan
        if sayac == 0:
                sonpuan = anapuan
        else:
                sonpuan = (anapuan*(5 + sayac/2) + toplam)/(5+(3*sayac)/2)
        return (url2, sonpuan, sonuclar)
