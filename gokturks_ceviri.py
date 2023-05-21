alphabet = {
    "a": "𐰀",
    "b": "𐰋",
    "c": "𐰲",
    "ç": "𐰲",
    "d": "𐰑",
    "e": "𐰀",
    "f": "𐰯",
    "g": "𐰍",
    "ğ": "𐰍",
    "h": "𐰴",
    "i": "𐰃",
    "j": "𐰖",
    "k": "𐰴",
    "l": "𐰞",
    "m": "𐰢",
    "n": "𐰣",
    "o": "𐰆",
    "ö": "𐰇",
    "p": "𐰯",
    "q": "𐰴",
    "r": "𐰺",
    "s": "𐰽",
    "ş": "𐱁",
    "t": "𐱃",
    "u": "𐰆",
    "ü": "𐰇",
    "v": "𐰉",
    "x": "𐰴",
    "y": "𐰖",
    "z": "𐰔",

    " ":":",

    "A": "𐰀",
    "B": "𐰋",
    "C": "𐰲",
    "Ç": "𐰲",
    "D": "𐰑",
    "E": "𐰀",
    "F": "𐰯",
    "G": "𐰍",
    "Ğ": "𐰍",
    "H": "𐰴",
    "I": "𐰃",
    "İ": "𐰃",
    "J": "𐰖",
    "K": "𐰴",
    "L": "𐰞",
    "M": "𐰢",
    "N": "𐰣",
    "O": "𐰆",
    "Ö": "𐰇",
    "P": "𐰯",
    "Q": "𐰴",
    "R": "𐰺",
    "S": "𐰽",
    "Ş": "𐱁",
    "T": "𐱃",
    "U": "𐰆",
    "Ü": "𐰇",
    "V": "𐰉",
    "X": "𐰴",
    "Y": "𐰖",
    "Z": "𐰔",

}

while True:

    kelime = input("Çevirmek istediğin kelimeyi gir: ")

    s = " "
    for harf in kelime:
        if harf.lower() in alphabet:
            s += alphabet[harf.lower()]
    else:
        s += harf
    print("{} / {}".format(s, kelime))

    if (kelime == "é"):
       print("işlem sonlandırılıyor....")
       break