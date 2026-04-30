import string
import sys
from random import choices

def generatePassword(uppercase : bool = True, digits : bool = True, specialchar : bool = True, length : int = 14) -> str:
    allowedchars = string.ascii_lowercase
    if uppercase:
        allowedchars += string.ascii_uppercase
    if digits:
        allowedchars += string.digits
    if specialchar:
        allowedchars += string.punctuation
    return ''.join(choices(allowedchars, k = length))
    

def validatePassword(password : str) -> bool:
    if len(password) >= 8 and any(c in password for c in string.ascii_uppercase) and any(n in password for n in string.digits) and any(p in password for p in string.punctuation):
        return True
    else:
        return False

def caesar(text : str, offset : int = 3) -> str:
    alphabet = string.ascii_lowercase
    textlower = text.lower()
    toArray = list(textlower)
    tempArray = []
    for i in range(len(toArray)):
        try:
            temp = alphabet.index(toArray[i])
        except ValueError:
            tempArray.append(toArray[i])
            continue
        temp += offset
        while temp > 25:
            temp -= 26
        while temp < 0:
            temp += 26
        tempArray.append(alphabet[temp])
    return "".join(tempArray)

if __name__ == "__main__":
    print("Generátor a validátor hesel\n")
    try:
        while True:
            option = input("Vyberte možnost (generate, validate, encrypt): ")
            match option.lower():

                case "generate":

                    while True:
                        upper = input("Chcete mít v hesle velká písmena (y/n): ")
                        if upper == "y":
                            uppercase = True
                            break
                        elif upper == "n":
                            uppercase = False
                            break
                        else:
                            print("Invalidní vstup!\n")

                    while True:
                        nums = input("Chcete mít v hesle čísla (y/n): ")
                        if nums == "y":
                            digits = True
                            break
                        elif nums == "n":
                            digits = False
                            break
                        else:
                            print("Invalidní vstup!\n")

                    while True:
                        special = input("Chcete mít v hesle speciální znaky (y/n): ")
                        if special == "y":
                            specialchar = True
                            break
                        elif special == "n":
                            specialchar = False
                            break
                        else:
                            print("Invalidní vstup!\n")

                    while True:
                        try:
                            length = int(input("Zadejte délku hesla: "))
                            break
                        except ValueError:
                            print("Invalidní vstup!\n")
                            continue

                    print(f"Vaše heslo: {generatePassword(uppercase, digits, specialchar, length)}\n")

                case "validate":
                    password = input("Zadejte vaše heslo: ")

                    if validatePassword(password):
                        print("Vaše heslo je bezpečné!\n")
                    else:
                        print("Vaše heslo není bezpečné!\n")

                case "encrypt":
                    password = input("Zadejte heslo k zašifrování: ")
                    while True:
                        try:
                            offset = int(input("Zadejte offset: "))
                            break
                        except ValueError:
                            print("Invalidní vstup!\n")
                            continue

                    print(f"Vaše heslo: {caesar(password, offset)}\n")

                case _:
                    print("Neznámá volba!\n")
    except KeyboardInterrupt:
        sys.exit(0)