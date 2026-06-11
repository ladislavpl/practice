import string
import unicodedata
from random import choices

def generatePassword(uppercase : bool = True, digits : bool = True, specialchar : bool = True, length : int = 10) -> str:
    allowedchars = string.ascii_lowercase
    if uppercase:
        allowedchars += string.ascii_uppercase
    if digits:
        allowedchars += string.digits
    if specialchar:
        allowedchars += string.punctuation
    return ''.join(choices(allowedchars, k = length))

def generateMail(fname : str, lname : str, domain : str = "firma.cz"):
    fname_normal = unicodedata.normalize('NFKD', fname)
    fname_final = "".join([c for c in fname_normal if unicodedata.category(c) != 'Mn']).strip().lower()

    lname_normal = unicodedata.normalize('NFKD', lname)
    lname_final = "".join([c for c in lname_normal if unicodedata.category(c) != 'Mn']).strip().lower()

    if "." in domain:
        return f"{fname_final}.{lname_final}@{domain.lower().strip()}"
    else:
        raise Exception("Invalid domain entered!")

if __name__ == "__main__":
    arr = ["Jan Novák;IT", "Petr Černý;Management"]
    fnames = []
    lnames = []
    positions = []
    for data in arr:
        positions.append(data.split(";")[1])
        fnames.append(data.split(";")[0].split(" ")[0])
        lnames.append(data.split(";")[0].split(" ")[1])
    for i in range(len(lnames)):
        print(f"Jméno: {fnames[i]} {lnames[i]} [{positions[i]}] -> E-mail: {generateMail(fnames[i], lnames[i])} | Heslo: {generatePassword()}")