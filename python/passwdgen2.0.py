import string
import sys
import secrets

def generatePassword(uppercase : bool = True, digits : bool = True, specialchar : bool = True, length : int = 14) -> str:
    required_sets = [string.ascii_lowercase]
    
    if uppercase:
        required_sets.append(string.ascii_uppercase)
    if digits:
        required_sets.append(string.digits)
    if specialchar:
        required_sets.append("!@#&.,-_")

    if length < len(required_sets):
        raise ValueError("length is too short to include every required character type")

    allowedchars = "".join(required_sets)

    while True:
        password = "".join(secrets.choice(allowedchars) for _ in range(length))
        if all(any(c in charset for c in password) for charset in required_sets):
            return password

def validatePassword(password : str) -> bool:
    if len(password) >= 8 and any(c in password for c in string.ascii_uppercase) and any(n in password for n in string.digits) and any(p in password for p in string.punctuation):
        return True
    else:
        return False

if __name__ == "__main__":
    print("Generátor a validátor hesel\n")
    try:
        while True:
            option = input("Vyberte možnost (generate, validate, exit): ")
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

                case "exit":
                    sys.exit(0)

                case _:
                    print("Neznámá volba!\n")
    except KeyboardInterrupt:
        sys.exit(0)