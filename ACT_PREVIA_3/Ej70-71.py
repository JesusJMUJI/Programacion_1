txtInput = input("Escribe una letra: ")

if txtInput.isnumeric():
    print(txtInput + " no es una letra")
elif txtInput.isupper():
    print(txtInput + " es una mayuscula")
elif txtInput.islower():
    print(txtInput + " es una minuscula")
