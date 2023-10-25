

jednosci = {
    0: "",
    1: "jeden ",
    2: "dwa ",
    3: "trzy ",
    4: "cztery ",
    5: "pięć ",
    6: "sześć ",
    7: "siedem ",
    8: "osiem ",
    9: "dziewięć "
}

nascie = {
    0: "",
    1: "jedenaście ",
    2: "dwanaście ",
    3: "trzynaście ",
    4: "czternaście ",
    5: "piętnaście ",
    6: "szesnaście ",
    7: "siedemnaście ",
    8: "osiemnaście ",
    9: "dziewiętnaście ",
}

dziesiatki = {
    0: "",
    1: "dziesięć ",
    2: "dwadzieścia ",
    3: "trzydzieści ",
    4: "czterdzieści ",
    5: "pięćdziesiąt ",
    6: "sześćdziesiąt ",
    7: "siedemdziesiąt ",
    8: "osiemdziesiąt ",
    9: "dziewięćdziesiąt ",
}

setki = {
    0: "",
    1: "sto ",
    2: "dwieście ",
    3: "trzysta ",
    4: "czterysta ",
    5: "pięćset ",
    6: "sześćset ",
    7: "siedemset ",
    8: "osiemset ",
    9: "dziewięćset "
}

formy = [
        ("", "", ""),
        ("tysiąc ", "tysiące ", "tysięcy "), # 10^3
        ("milion ", "miliony ", "milionów "), # 10^6
        ("miliard ", "miliardy ", "miliardów "), # 10^9
        ("bilion ", "biliony ", "bilionów "), # 10^12
        ("biliard ", "biliardy ", "biliardów "), # 10^15
        ("trylion ", "tryliony ", "trylionów "), # 10^18
        ("tryliard  ", "tryliardy  ", "tryliardów "), # 10^21
        ("kwadrylion ", "kwadryliony ", "kwadrylionów "), # 10^24
        ("kwadryliard ", "kwadryliardy ", "kwadryliardów "), # 10^27
        ("kwintylion ", "kwintyliony ", "kwintylionów "), # 10^30
        ("kwintyliard ", "kwintyliardy ", "kwintyliardów "),  # 10^33
        ("sekstylion ", "sekstyliony ", "sekstylionów "), # 10^36
        ("sekstyliard ", "sekstyliardy ", "sekstyliardów "), # 10^39
        ("septylion ", "septyliony ", "septylionów "), # 10^42
        ("septyliard ", "septyliardy ", "septyliardów "), # 10^45
        ("oktylion ", "oktyliony ", "oktylionów "), # 10^48
        ("oktyliard ", "oktyliardy ", "oktyliardów "), # 10^51
        ("nonylion ", "nonyliony ", "nonylionów "),  # 10^54
        ("nonyliard ", "nonyliardy ", "nonyliardów "),  # 10^57
        ("decylion ", "decyliony ", "decylionów "),  # 10^60
        ("decyliard ", "decyliardy ", "decyliardów "),  # 10^63
        ("undecylion ", "undecyliony ", "undecyliono "),  # 10^66
        ("undecyliard ", "undecyliardy ", "undecyliardów "),  # 10^69
        ("duodecylion ", "duodecyliony ", "duodecylionów "),  # 10^72
        ("duodecyliard ", "duodecyliardy ", "duodecyliardów "),  # 10^75
    ]

def liczba_na_slowa(liczba: str, short: bool=True):
    liczba = int(liczba)
    g = 0
    wynik = ""
    ujemna = False
    if liczba == 0:
        return "zero "
    else:
        if liczba < 0:
            ujemna = True
            liczba = - liczba

        while liczba != 0:
            s = (liczba % 1000) // 100
            d = (liczba % 100) // 10
            j = liczba % 10
            n = 0

            if d == 1 and j > 0:
                n = j
                d = 0
                j = 0

            if j == 1 and s + d + n == 0:
                k = 0  # pierwsza forma gramatyczna
            elif 2 <= j <= 4:
                k = 1  # druga forma gramatyczna
            else:
                k = 2  # trzecia forma gramatyczna

            liczba //= 1000

            if s + d + n + j > 0:
                # short flaga robi ze zamiast napisac np: jeden milion złotych napisze poprostu milion złotych
                if liczba == 0 and j == 1 and short and liczba == 1:

                    wynik = formy[g][k] + wynik

                else:
                    wynik = setki[s] + dziesiatki[d] + nascie[n] + jednosci[j] + formy[g][k] + wynik
            g += 1

        if ujemna:
            wynik = "minus " + wynik

        return wynik

def liczba_na_pieniadze(liczba: str, short: bool =True):
    def forma_zlote(liczb: int):
        if liczb < 0:
            liczb = - liczb
        if liczb == 1:
            return "złoty "
        if (5 <= liczb <= 14) or str(liczb)[-1] in ["1", "5", "6", "7", "8", "9", "0"]:
            return "zlotych "
        return "złote "

    def forma_grosze(liczb: int):
        if liczb < 0:
            liczb = - liczb
        if liczb == 1:
            return "grosz "
        if (5 <= liczb <= 14) or str(liczb)[-1] in ["1", "5", "6", "7", "8", "9", "0"]:
            return "groszy "
        return "grosze "

    wynik = ""
    zlote, grosze = None, None
    try:
        zlote, grosze = liczba.split(",")
    except ValueError:
        zlote = liczba

    if zlote:
        wynik += liczba_na_slowa(zlote, short) + forma_zlote(int(zlote))
    if grosze:
        if len(grosze) == 1:
            grosze += "0"
        wynik += liczba_na_slowa(grosze, short) + forma_grosze(int(grosze))

    return wynik



print(liczba_na_pieniadze("69,420", False))
print(liczba_na_slowa("2137", True))


