import dictionary as d
import richWord as rw

class MultiDictionary:
    def __init__(self):
        self.dictionaries = {
            'italian': d.Dictionary(),
            'english': d.Dictionary(),
            'spanish': d.Dictionary()
        }

    def loadDictionaries(self):
        self.dictionaries['italian'].loadDictionary('resources/Italian.txt')
        self.dictionaries['english'].loadDictionary('resources/English.txt')
        self.dictionaries['spanish'].loadDictionary('resources/Spanish.txt')

    def printDic(self, language):
        if language in self.dictionaries:
            self.dictionaries[language].printAll()
        else:
            print("Dizionario non disponibile per la lingua selezionata")

    def searchWordLinear(self, words, language):
        if language not in self.dictionaries:
            return []

        dict_words = self.dictionaries[language].dict
        rich_words = []
        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.corretta = word in dict_words
            rich_words.append(rich_word)
        return rich_words

    def searchWordDichotomic(self, words, language):
        if language not in self.dictionaries:
            return []

        dict_words = sorted(self.dictionaries[language].dict)
        rich_words = []
        for word in words:
            rich_word = rw.RichWord(word)
            rich_word.corretta = self.binary_search(dict_words, word)
            rich_words.append(rich_word)
        return rich_words

    def binary_search(self, data, target):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == target:
                return True
            elif data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
