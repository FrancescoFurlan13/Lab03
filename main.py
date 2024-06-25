import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input().strip()
    if not txtIn.isdigit() or not (1 <= int(txtIn) <= 4):
        print("Opzione non valida. Riprova.")
        continue

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn, "italian")
    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn, "english")
    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn, "spanish")
    elif int(txtIn) == 4:
        print("Uscita dal programma.")
        break
