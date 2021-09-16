
def hesapla(list1, list2):
        point = 0
        for (word1,freq1) in list1:
                for (word2,freq2) in list2:
                        if word1 == word2:
                                point += freq1 * freq2
        return point/(total(list1) + total(list2))

def total(list):
        result = 0
        for (word,freq) in list:
                result += freq
        return result

