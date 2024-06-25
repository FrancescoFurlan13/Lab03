class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, 'r') as file:
            self._dict = [line.strip().lower() for line in file]
    def printAll(self):
        for word in self._dict:
            print(word)

    @property
    def dict(self):
        return self._dict