import time
import multiDictionary as md


class SpellChecker:
    def __init__(self):
        self.multiDictionary = md.MultiDictionary()
        self.multiDictionary.loadDictionaries()

    def handleSentence(self, txtIn, language):
        # Pulizia del testo
        cleaned_text = replaceChars(txtIn.lower())
        words = cleaned_text.split()

        # Ricerca lineare
        start_time = time.time()
        rich_words_linear = self.multiDictionary.searchWordLinear(words, language)
        elapsed_time_linear = time.time() - start_time

        # Ricerca dicotomica
        start_time = time.time()
        rich_words_dichotomic = self.multiDictionary.searchWordDichotomic(words, language)
        elapsed_time_dichotomic = time.time() - start_time

        # Stampa i risultati per la ricerca lineare
        print("-----------------------------")
        print("Usando la ricerca lineare")
        for word in rich_words_linear:
            if not word.corretta:
                print(word)
        print(f"Numero di parole errate: {sum(1 for word in rich_words_linear if not word.corretta)}")
        print(f"Tempo impiegato: {elapsed_time_linear} secondi")
        print("-----------------------------")

        # Stampa i risultati per la ricerca dicotomica
        print("Usando la ricerca dicotomica")
        for word in rich_words_dichotomic:
            if not word.corretta:
                print(word)
        print(f"Numero di parole errate: {sum(1 for word in rich_words_dichotomic if not word.corretta)}")
        print(f"Tempo impiegato: {elapsed_time_dichotomic} secondi")
        print("-----------------------------")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\\"*{}[]()><#?!.,-!$%^&*;:_~"
    for c in chars:
        text = text.replace(c, "")
    return text
