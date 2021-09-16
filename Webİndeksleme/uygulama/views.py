from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import *
from . import asama1,asama2,asama3,asama4

# Create your views here.


def anasayfa(request):
    return render(request, "sablon.html", {"sayfalar": sayfalar, "name": "anasayfa"})

def frekans(request):
    content = tekURL 
    return render(request, "form.html", {"sayfalar": sayfalar, "name": "frekans", "targeturl": "/frekans/sonuclar", "content": content})

def anahtar(request):
    content = tekURL 
    return render(request, "form.html", {"sayfalar": sayfalar, "name": "anahtar", "targeturl": "/anahtar/sonuclar", "content": content})

def benzerlik(request):
    content = ikiURL
    return render(request, "form.html", {"sayfalar": sayfalar, "name": "benzerlik", "targeturl": "benzerlik/sonuclar", "content": content})


def indeksleme(request):
    content = cokURL  
    return render(request, "form.html", {"sayfalar": sayfalar, "name": "indeksleme", "targeturl": "/indeksleme/sonuclar", "content": content})


def semantik(request):
    content = cokURL 
    return render(request, "form.html", {"sayfalar": sayfalar, "name": "semantik", "targeturl": "/semantik/sonuclar", "content": content})


def frekans_s(request):
    sonuc = asama1.hesapla(request.POST["url1"])
    content = "<h2>Kelimelerin Frekansları:</h2><ul>"
    for (kelime,freq) in sonuc:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul>"
    return render(request, "sonuc.html", {"sayfalar": sayfalar, "name": "frekans", "content": content})


def anahtar_s(request):
    sonuc = asama2.hesapla(request.POST["url1"])[:10]
    content = "<h2>Anahtar kelimeler:</h2><ul>"
    for (kelime,freq) in sonuc:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul>"
    return render(request, "sonuc.html", {"sayfalar": sayfalar, "name": "anahtar", "content": content})


def benzerlik_s(request):
    url1 = asama2.hesapla(request.POST["url1"])
    url2 = asama2.hesapla(request.POST["url2"])
    sonuc = asama3.hesapla(url1, url2)
    content = "<h2>Benzerlik puanı: " + str(sonuc) + "</h2>"
    content += "<div style='float:left; width: 50%;'><h2>1. URL kelime frekansları</h2><ul>"
    for (kelime,freq) in url1:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul></div><div style='float:left; width: 50%;'><h2>2. URL kelime frekansları</h2><ul>"
    for (kelime,freq) in url2:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul></div>"
    return render(request, "sonuc.html", {"sayfalar": sayfalar, "name": "benzerlik", "content": content})


def indeksleme_s(request):
    url1 = request.POST["url1"]
    url1kws = asama2.hesapla(url1)[:10]
    urls = []
    for url in request.POST["urls"].split():
        urls.append(url)
    (sonuclar, siraliliste) = asama4.hesapla(url1, urls)
    content = "<h2>Ana URL için anahtar kelimeler</h2>"
    content += "<i>" + url1 + "</i>"
    for (kelime,freq) in url1kws:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul>"
    content += "<h2>Benzerlik puanına göre sayfalar:</h2>"
    content += agac_yazdir(sonuclar,siraliliste)
    return render(request, "sonuc.html", {"sayfalar": sayfalar, "name": "indeksleme", "content": content})

def agac_yazdir(agac, liste):
        sonuc = "<ul>"
        for (url, puan, agac2) in agac:
                sira = asama4.sirabul(url, liste)
                kws = asama2.hesapla(url)[:10]
                sonuc += "<li><b>" + str(sira) + ".</b> " + url +": <b>" + str(puan) + "</b><br>("
                for (kw,freq) in kws:
                        sonuc += "<i>" + kw + "</i>:" + str(freq) + " "
                sonuc += ")</li>"
                sonuc += agac_yazdir(agac2, liste)
        sonuc += "</ul>"
        return sonuc

def semantik_s(request):
    sonuc = asama1.hesapla(request.POST["url1"])
    content = "<h2>Kelimelerin Frekansları:</h2><ul>"
    for (kelime,freq) in sonuc:
        content += "<li> " + kelime + ": " + freq.__str__() + "</li>"
    content += "</ul>"
    return render(request, "sonuc.html", {"sayfalar": sayfalar, "name": "frekans", "content": content})


