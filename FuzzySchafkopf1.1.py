# Einleitung

print("                                                                                            ")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("        Dieses Modul bewertet wie geeignet eine Karte für einen aktuellen Stich ist.        ")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("                              Kartennamen werden so abgekürzt:                              ")
print("                                                                                            ")
print("                      Eichel -> E, Gras -> G, Herz -> H, Schelle -> S                       ")
print(" Sieben -> 7, Acht -> 8, Neun -> 9, Koenig -> K, Zehn -> 10, Ass -> A, Unter -> U, Ober -> O")
print("                                                                                            ")
print("                                                                                            ")
print(" Beispiele: Eichel Ober -> EO, Herz Ass -> HA, Schellen Koenig -> SK, Gras Sieben -> 7, ... ")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("        Der Computer ist leider nicht in der Lage einen Spielmodus selbst zu waehlen.       ")
print("            Bitte entscheide entsprechend fuer den Computer was er spielen soll.            ")
print("                                                                            - Alexandru Duca")

# Space

print()
print()
print()


# Eingabe

def intInput(min, max):
    while True:
        i = input(">>> ")
        try:
            i = int(i)
            if i < min:
                print("Ungueltige Eingabe:")
                print("Die eingegebene Zahl muss groesser oder gleich", min, "sein.")
            elif i > max:
                print("Ungueltige Eingabe:")
                print("Die eingegebene Zahl muss kleiner oder gleich", max, "sein.")
            else:
                return i
        except:
            print("Ungueltige Eingabe:")
            print("Die Eingabe ist keine natuerliche Zahl.")

def strInput(strWertemenge):
    while True:
        i = input(">>> ")
        try:
            i = str(i)
            if strWertemenge.count(i) == 0:
                print("Ungueltige Eingabe.")
                print("Die Eingabe ist kein erwarteter Wert.")
            else:
                return i
        except:
            print("Ungueltige Eingabe:")
            print("Die Eingabe ist keine Folge gueltiger Zeichen.")

Deck = []
for i in range(4):
    for j in range(8):
        if i == 3:
            farbe = "S"
        elif i == 2:
            farbe = "H"
        elif i == 1:
            farbe = "G"
        elif i == 0:
            farbe = "E"
        if j == 0:
            wert = "7"
        elif j == 1:
            wert = "8"
        elif j == 2:
            wert = "9"
        elif j == 3:
            wert = "K"
        elif j == 4:
            wert = "10"
        elif j == 5:
            wert = "A"
        elif j == 6:
            wert = "U"
        elif j == 7:
            wert = "O"
        Deck.append(farbe + wert)

Friedhof = []

# Position am Tisch
print()
print("Position am Tisch:")
print("(Links vom Geber ist Position 1)")
positionAmTisch = intInput(1, 4)

# Angabe der Handkrten
Handkarten = []
print()
print("Handkarten:")
for i in range(8):
    eingabe = strInput(Deck)
    Handkarten.append(eingabe)
    Deck.pop(Deck.index(eingabe))
    Friedhof.append(eingabe)


# -------------------------------------------------------------------------------------------------------
# Das Deck

Deck = []
Symbole = ["S", "G", "E", "H"]

for j in range(0, 4):
    for i in range(7, 10):
        Deck.append(Symbole[j] + str(i))
    Deck.append(Symbole[j] + "K")
    Deck.append(Symbole[j] + "10")
    Deck.append(Symbole[j] + "A")

Symbole = ["S", "H", "G", "E"]

for j in range(0, 4):
    Deck.append(Symbole[j] + "U")

for j in range(0, 4):
    Deck.append(Symbole[j] + "O")

Zahlen = []
for i in range(0, 32):
    Zahlen.append(i)

# nuetzliche Methoden:

def anzahlTrumpf(Blatt, farbe):
    a = 0
    if farbe == 3:  # Eichel
        for i in range(0, len(Blatt)):
            if Blatt[i] >= 18:
                a = a + 1
    if farbe == 2:  # Gras
        for i in range(0, len(Blatt)):
            if Blatt[i] >= 24 or (Blatt[i] > 11 and Blatt[i] <= 17):
                a = a + 1
    if farbe == 1:  # Herz
        for i in range(0, len(Blatt)):
            if Blatt[i] >= 24 or (Blatt[i] > 5 and Blatt[i] <= 11):
                a = a + 1
    if farbe == 0:  # Schelle
        for i in range(0, len(Blatt)):
            if Blatt[i] >= 24 or Blatt[i] <= 5:
                a = a + 1
    return a


def anzahlSau(Blatt):
    a = 0
    for i in range(0, len(Blatt)):
        if [5, 11, 17].count(Blatt[i]) == 1:
            a = a + 1
    return a


def anzahlNichtTrumpfSau(Blatt, farbe):
    a = 0
    sau = [5, 11, 17, 23]
    del sau[farbe]
    for i in range(0, len(Blatt)):
        if sau.count(Blatt[i]) == 1:
            a = a + 1
    return a


def anzahlOber(Blatt):
    a = 0
    for i in range(0, len(Blatt)):
        if [31, 30, 29, 28].count(Blatt[i]) == 1:
            a = a + 1
    return a


def anzahlUnter(Blatt):
    a = 0
    for i in range(0, len(Blatt)):
        if [27, 26, 25, 24].count(Blatt[i]) == 1:
            a = a + 1
    return a


def anzahlBrems(Blatt):
    a = 0
    for i in range(0, len(Blatt)):
        if [31, 30, 29].count(Blatt[i]) == 1:
            a = a + 1
    return a


def istFrei(Blatt):
    for i in range(0, 3):
        frei = True
        for j in range(0, 6):
            if Blatt.count(i * 6 + j):
                frei = False
        if frei == True:
            return True
    return False


def unterschiedlicheSpatzen(Blatt):
    for k in range(0, 3):
        test = False
        for j in range(0, 8):
            if [5 * k, 5 * k + 1, 5 * k + 2].count(Blatt[j]) > 0:
                test = True
        if test == False:
            return False
    return True


def anzahlSchelle(Blatt):
    a = 0
    i = 0
    while i < len(Blatt):
        if Blatt[i] >= 0 and Blatt[i] <= 5:
            a = a + 1
        i = i + 1
    return a


def anzahlGras(Blatt):
    a = 0
    i = 0
    while i < len(Blatt):
        if Blatt[i] >= 6 and Blatt[i] <= 11:
            a = a + 1
        i = i + 1
    return a


def anzahlEichel(Blatt):
    a = 0
    i = 0
    while i < len(Blatt):
        if Blatt[i] >= 12 and Blatt[i] <= 17:
            a = a + 1
        i = i + 1
    return a


def waehleSau(Blatt):
    # Nimm die Trumpf und Sau raus
    i = 0
    while i < len(Blatt):
        if Blatt[i] >= 18 or [5, 11, 17].count(Blatt[i]) == 1:
            del Blatt[i]
            i = i - 1
        i = i + 1

    # Sortiere in Farben
    s = []
    g = []
    e = []
    z = []

    i = 0
    while i < len(Blatt):
        if Blatt[i] >= 0 and Blatt[i] <= 5:
            s.append(Blatt[i])
        elif Blatt[i] >= 6 and Blatt[i] <= 11:
            g.append(Blatt[i])
        elif Blatt[i] >= 12 and Blatt[i] <= 17:
            e.append(Blatt[i])
        i = i + 1

    if len(s) <= len(g) and len(s) <= len(e) and len(s) != 0:
        z.append(s)
    if len(g) <= len(e) and len(g) <= len(s) and len(g) != 0:
        z.append(g)
    if len(e) <= len(s) and len(e) <= len(g) and len(e) != 0:
        z.append(e)

    if len(z) == 1:
        if z[0] == s:
            return 0
        elif z[0] == g:
            return 1
        elif z[0] == e:
            return 2

    if z.count(s) == 1:
        s_best = (s[len(s) - 1] + 1) % 6
    else:
        s_best = -1

    if z.count(g) == 1:
        g_best = (g[len(g) - 1] + 1) % 6
    else:
        g_best = -1

    if z.count(e) == 1:
        e_best = (e[len(e) - 1] + 1) % 6
    else:
        e_best = -1

    z = []
    if g_best >= s_best and g_best >= e_best:
        z.append(g_best)

    if e_best >= g_best and e_best >= s_best:
        z.append(e_best)

    if s_best >= g_best and s_best >= e_best:
        z.append(s_best)

    if z[0] == s_best:
        return 0
    elif z[0] == g_best:
        return 1
    elif z[0] == e_best:
        return 2


def Anfang(Blatt):
    spielbar = []
    riskant = []
    t = anzahlTrumpf(Blatt, 2)
    s = anzahlSau(Blatt)
    o = anzahlOber(Blatt)
    u = anzahlUnter(Blatt)
    b = anzahlBrems(Blatt)

    # Farbsolo?

    for farbe in range(0, 3):  # Jede Farbe testen

        trumpf = anzahlTrumpf(Blatt, farbe)

        if trumpf == 8 and (Blatt.count(31) == 1 or Blatt.count(farbe * 6 - 1) == 1 or Blatt.count(farbe * 6 - 2) == 1):
            return farbe + 3

        if trumpf == 7:
            if anzahlNichtTrumpfSau(Blatt, farbe) == 1:
                if Blatt.count(farbe * 6 - 1) == 1 or Blatt.count(farbe * 6 - 2) == 1:
                    return farbe + 3
            else:
                if o + u >= 4 and o >= 2:
                    return farbe + 3

        if trumpf == 6:
            if Blatt.count(31) == 1 and Blatt.count(30) == 1:
                return farbe + 3
            if o >= 3 and anzahlNichtTrumpfSau(Blatt, farbe) >= 1:
                return farbe + 3

        if trumpf == 5:
            if Blatt.count(31) == 1 and Blatt.count(30) == 1 and Blatt.count(29) == 1:
                if anzahlNichtTrumpfSau(Blatt, farbe) == 2 and istFrei(Blatt) == True:
                    return farbe + 3


    # Wenz kann er noch nicht...


    # Sauspiel?

    if ((t == 6 and s < 2) or (t == 7 and s < 1)):
        return waehleSau(Blatt)

    elif t == 5 and s < 3 and (s > 0 or istFrei(Blatt) == True):
        return waehleSau(Blatt)

    elif t == 5 and unterschiedlicheSpatzen(Blatt) == True and ((o >= 2 and u >= 1) or (o >= 3)) and s == 0:
        return waehleSau(Blatt)

    elif t == 4 and ((b >= 1 and u >= 1) or (b >= 1 and o >= 2)) and s == 2:
        return waehleSau(Blatt)

    else:
        return -1

# -------------------------------------------------------------------------------------------------------

Zahlen_Handkarten = []
for i in range(len(Handkarten)):
    Zahlen_Handkarten.append(Deck.index(Handkarten[i]))
gSpielmodus = Anfang( Zahlen_Handkarten )

# -1: nicht spielen
# Sauspiel:
#   0: Schellen
#   1: Gras
#   2: Eichel
# Farbsolo:
#   3: Schellen
#   4: Gras
#   5: Herz
#   6: Eichel
# 7: Wenz

print()
print("Wenn ich gefragt werde, was ich spielen soll, dann sage ich:")

if gSpielmodus == -1:
    print("Ich moechte nicht spielen.")
elif gSpielmodus == 0:
    print("Ich spiele auf die Hundsg'fickte!")
elif gSpielmodus == 1:
    print("Ich spiele auf die Blaue!")
elif gSpielmodus == 2:
    print("Ich spiele auf die Alte!")
elif gSpielmodus == 3:
    print("Ich spiele ein Schellensolo!")
elif gSpielmodus == 4:
    print("Ich spiele ein Grassolo!")
elif gSpielmodus == 5:
    print("Ich spiele ein Herzsolo!")
elif gSpielmodus == 6:
    print("Ich spiele ein Eichelsolo!")
elif gSpielmodus == 7:
    print("Ich spiele ein Wenz!")

print()

# Wahl des Spielmodus

print()
print("Spielmodus:")
print("Erlaubt sind:", ["Ramsch", "Sauspiel", "Wenz", "Schellensolo", "Herzsolo", "Grassolo", "Eichelsolo"])
spielmodus = strInput(["Ramsch", "Sauspiel", "Wenz", "Schellensolo", "Herzsolo", "Grassolo", "Eichelsolo"])

if spielmodus != "Ramsch":
    print()
    print("An welcher Position sitzt der Spieler?")
    positionDesSpielersAmTisch = intInput(1, 4)


if spielmodus == "Sauspiel":
    print()
    print("Was ist die Rufsau?")
    rufsau = strInput(["EA", "GA", "SA"])


# Space

print()
print()
print()
print()
print()

# - - - - - - - - - - - - - - - - - - - Fuzzy-Methoden - - - - - - - - - - - - - - - - - -


# Fuzzyfiziert die Punktzahl.
# Die Rueckgabe ist ein Array mit der Zugehoerigkeit der Punktzahl zu fuenf verschiedenen linguistischen Variablen.
# Genannte Variablen sind in Ihrer "Positivitaet" aufsteigend angeordnet.
def fuzzyPunkte(punkte, maximalePunktzahlImStich ,stichGehoertUns):
    # Wenn mir der Stich nicht gehoert, dann gibt es keine Punkte zu holen:
    if stichGehoertUns == False:
        # Alle linguistischen Variablen sind auf 0 bis auf die schlechteste, die auf 1 ist.
        return [1, 0, 0, 0, 0]
    # Wenn es weniger als 20 Punkte im Stich gibt, sind Punkte, die eigentlich mehr wert:
    if maximalePunktzahlImStich < 20:
        # In diesem Fall haben wir eine gestauchte Fuzzy-Akkordeonsfunktion:
        return fuzzyAkkordeonsfunktion(punkte, maximalePunktzahlImStich)
    elif maximalePunktzahlImStich >= 20:
        # In diesem Fall haben wir eine ungestauchteFuzzy-Akkordeonsfunktion über das Intervall [0, 20]:
        if punkte < 20:
            return fuzzyAkkordeonsfunktion(punkte, 20)
        # Ist die Punktzahl groesser 20, so liegen eindeutig viele Punkte im Stich:
        elif punkte >= 20:
            return [0, 0, 0, 0, 1]


# Fuzzyfiziert die Staerke einer Karte.
# Die Rueckgabe ist ein Array mit der Zugehoerigkeit der Karte zu fuenf verschiedenen linguistischen Variablen.
# Genannte Variablen sind in Ihrer "Positivitaet" aufsteigend angeordnet.
# Es ist anzumerken, dass einer Karte eine Zahl zugeordnet werden muss, die bewertet werden soll.
def fuzzyStaerke(staerke, anzahlUnterschiedlicheKarten):
    # Im Prinzip eine Fuzzy-Akkordeonsfunktion:
    return fuzzyAkkordeonsfunktion(staerke, anzahlUnterschiedlicheKarten)


# Allgemeine Fuzzy-Funktion, die abhaengig von einem Maximalwert ist und wie ein Akkordeon aussieht.
# Es werden fuenf lingusitische Variablen auf das Intervall [0, maximalwert] gestaucht.
# Die Rueckgabe ist ein Array mit der Zugehoerigkeit der Zahl x zu den fuenf verschiedenen linguistischen Variablen.
def fuzzyAkkordeonsfunktion(x, maximalwert):
    # Vorbereitung des Rueckgabe-Arrays
    Zugehoerigkeiten = [0, 0, 0, 0, 0]
    # Wir unterteilen das Intervall [0, maximalwert] in vier kleine Abschnitte
    abschnittslaenge = maximalwert / 4
    # Wir schauen uns den Peak aller fuenf linguistischen Variablen an und defenieren and diesen eine Dreiecksfunktion
    # Anschließend werfen wir unsere Punktzahl (x-Wert) gleich in genannte Funktion und speichern das Ergebnis.
    for i in range(5):
        peak = abschnittslaenge * i
        Zugehoerigkeiten[i] = dreiecksfunktion(x, peak - abschnittslaenge, peak, peak + abschnittslaenge)
    # Rueckgabe
    return Zugehoerigkeiten


# Allgemeine Dreiecksfunktion.
# Die Rueckgabe ist der y-Wert der Dreiecksfunktion
# ( fuer mich: s. DSA Skript S. 16 )
def dreiecksfunktion(x, anfangspunkt, peak, endpunkt):
    if x < anfangspunkt:
        return 0
    elif anfangspunkt <= x and x <= peak:
        return ( x - anfangspunkt ) / ( peak - anfangspunkt )
    elif peak < x and x <= endpunkt:
        return ( endpunkt - x ) / ( endpunkt - peak )
    elif x > endpunkt:
        return 0


# Allgemeine R-Funktion, erinnert an einen Hockey-Schlaeger.
# Die Rueckgabe ist der y-Wert der R-Funktion.
# ( fuer mich: s. DSA Skript S. 18 )
def R_Funktion(x, anfangswert, peak):
    if x < anfangswert:
        return 0
    elif anfangswert <= x and x < peak:
        return ( x - anfangswert ) / ( peak - anfangswert )
    elif x > peak:
        return 1


# Allgemeine L-Funktion, erinnert auch an einen Hockey-Schlaeger.
# Die Rueckgabe ist der y-Wert der L-Funktion.
# ( fuer mich: s. DSA Skript S. 20 )
def L_Funktion(x, peak, endwert):
    if x < peak:
        return 1
    elif peak <= x and x <= endwert:
        return ( endwert - x ) / ( endwert - peak )
    elif x > endwert:
        return 0


# s- und t-Norm:
# Gibt die kleinere der zwei Zahlen a und b zurueck.
def min(a, b):
    if a < b:
        return a
    else:
        return b
# Gibt die groessere der zwei Zahlen a und b zurueck.
def max(a, b):
    if a > b:
        return a
    else:
        return b


# Nach Mini-Max-Prinzip soll nun das Regelsystem aufgestellt werden.
# Die Rueckgabe ist ein Array mit den zwei Fuzzywerten "Ja" und "Nein"
def regelsystem(fuzzyPunkte, fuzzyStaerke):
    # Das Regelsystem ist eine Einheitsmatrix die bewertet, ob eine Karte gelegt werden sollte.
    # ( fuer mich: Die Digonale sagt "Ja" und alle anderen Werte sagen "Nein". )
    Ja = 0
    Nein = 0
    # x- und y-"Koordinaten" der Matrix
    for x in range(5):
        for y in range(5):
            # Diagonale:
            if x == y:
                Ja = max( Ja, min( fuzzyPunkte[x], fuzzyStaerke[y] ) )
            # Alles andere:
            elif x != y:
                Nein = max( Nein, min( fuzzyPunkte[x], fuzzyStaerke[y] ) )
    return [Ja, Nein]


# Defuzzyfizierung:
# Wir definieren zunächst die Flaeche, deren Schwerpunkt wir berechnen wollen:
def defuzzyfunktion(x, Ja, Nein):
    return max( min (Ja, R_Funktion(x, 0, 1) ), min ( Nein, L_Funktion(x, 0, 1) ) )

# Gibt den x-Wert des Schwerpunkts zurueck. (Integralannaeherung)
def berechneSchwerpunktDerDefuzzyfunktion(Ja, Nein):
    o = 0.0
    u = 0.0
    w = 1000
    for i in range(w):
        x = i / w
        o = o + x * defuzzyfunktion(x, Ja, Nein)
        u = u + defuzzyfunktion(x, Ja, Nein)
    return o / u


def fuzzy(punkte, staerke, maximalePunktzahlImStich, stichGehoertUns, anzahlUnterschiedlicheKarten):
    L = regelsystem(fuzzyPunkte(punkte, maximalePunktzahlImStich ,stichGehoertUns), fuzzyStaerke(staerke, anzahlUnterschiedlicheKarten))
    return berechneSchwerpunktDerDefuzzyfunktion( L[0], L[1] )


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# Aufarbeitung der Informationen



# Variablen:

# Deck                             # []
# Handkarten                       # []
# Stich                            # []

# spielmodus                       # String
# rufsau                           # String

# anzahlUnterschiedlicheKarten     # int
# verbliebendePunkte               # int
# maximalePunktzahlImStich         # int
# stichGehoertUns                  # boolean

# anzahlKartenImStich              # int
# KartenImStich                    # []
# anzahlSpielbareKarten            # int
# spielbareKarten                  # []

# positionAmTisch                  # int
# angespielteKarte                 # String
# zugespielteKarte                 # String
# staerksteKarteImStich            # String
# angespielteFarbe                 # String

# aktuellerSpieler                 # int
# gewinnenderSpieler               # int
# Mitspieler                       # []

# Ablagestapel                     # []
# AblageDesGewinners               # []


# Defenition der Rangordnung:

Farbordnung =  [ "7","8","9","K","10","A" ]
Rangordnung =  [ "7","8","9","K","10","A" ]

if spielmodus == "Sauspiel" or spielmodus == "Herzsolo" or spielmodus == "Ramsch":
    for i in range(6):
        Rangordnung[i] = "H" + Rangordnung[i]
    Rangordnung = Rangordnung + ["SU","HU","GU","EU","SO","HO","GO","EO"]
elif spielmodus == "Eichelsolo":
    for i in range(6):
        Rangordnung[i] = "E" + Rangordnung[i]
    Rangordnung = Rangordnung + ["SU", "HU", "GU", "EU", "SO", "HO", "GO", "EO"]
elif spielmodus == "Grassolo":
    for i in range(6):
        Rangordnung[i] = "G" + Rangordnung[i]
    Rangordnung = Rangordnung + ["SU", "HU", "GU", "EU", "SO", "HO", "GO", "EO"]
elif spielmodus == "Schellensolo":
    for i in range(6):
        Rangordnung[i] = "S" + Rangordnung[i]
    Rangordnung = Rangordnung + ["SU", "HU", "GU", "EU", "SO", "HO", "GO", "EO"]
elif spielmodus == "Wenz":
    Rangordnung = ["SU", "HU", "GU", "EU"]
    Farbordnung = [ "7","8","9","O","K","10","A" ]


# Defenition der Farben:

# Aufgedruckte Farbe
def echteFarbeEinerKarte(k):
    return k[:1]

# Spieltechnische Farbe
def farbeEinerKarte(k):
    if Rangordnung.count(k) == 1:
        return "T"
    return echteFarbeEinerKarte(k)

# Aufgedruckter Wert
def wertEinerKarte(k):
    return k[1:]


# Spieltheoretische Methoden



# Spieltechnische Methoden

def legen(k):
    Stich.append(k)
    Friedhof.append(k)
    Deck.pop(Deck.index(k))

def naechsterSpieler(aktuellerSpieler):
    aktuellerSpieler = aktuellerSpieler + 1
    if aktuellerSpieler == 5:
        aktuellerSpieler = 1
    return aktuellerSpieler

def staerkereKarte(k1, k2, angespielteFarbe):
    f1 = farbeEinerKarte(k1)
    f2 = farbeEinerKarte(k2)
    if f1 == "T" and f2 != "T":
        return k1
    elif f1 != "T" and f2 == "T":
        return k2
    elif f1 == "T" and f2 == "T":
        if Rangordnung.index(k1) > Rangordnung.index(k2):
            return k1
        if Rangordnung.index(k1) < Rangordnung.index(k2):
            return k2
    elif f1 != "T" and f2 != "T" and f1 == angespielteFarbe and f2 != angespielteFarbe:
        return k1
    elif f1 != "T" and f2 != "T" and f1 != angespielteFarbe and f2 == angespielteFarbe:
        return k2
    elif f1 != "T" and f2 != "T" and f1 == angespielteFarbe and f2 == angespielteFarbe:
        if Farbordnung.index( wertEinerKarte(k1) ) > Farbordnung.index( wertEinerKarte(k2) ):
            return k1
        if Farbordnung.index( wertEinerKarte(k1) ) < Farbordnung.index( wertEinerKarte(k2) ):
            return k2
    else:
        return k1

def punkteEinerKarte(k):
    if wertEinerKarte(k) == "U":
        return 2
    elif wertEinerKarte(k) == "O":
        return 3
    elif wertEinerKarte(k) == "K":
        return 4
    elif wertEinerKarte(k) == "10":
        return 10
    elif wertEinerKarte(k) == "A":
        return 11
    else:
        return 0

def listeUmfuellen(A, B):
    for i in range(len(A)):
        B.append(A[i])
    return B

def bestimmeSpielbareHandkarten(H, f):
    S = []
    for i in range(len(H)):
        if farbeEinerKarte(H[i]) == f:
            S.append(H[i])
    if S == []:
        return H
    else:
        return S


# Botmethoden

def bestimmePunkteImStich(S):
    s = 0
    if S == []:
        return 0
    for i in range(len(S)):
        s = s + punkteEinerKarte(S[i])
    return s

def bestimmePunkteImDeck(D):
    s = 0
    if D == []:
        return 0
    for i in range(len(D)):
        s = s + punkteEinerKarte(D[i])
    return s

def bestimmeMaximalePunkteImStich(D, H):
    PD = []
    for i in range(len(D)):
        PD.append( punkteEinerKarte( D[i] ) )
    PD.sort()
    PH = []
    for i in range(len(H)):
        PH.append( punkteEinerKarte( H[i] ) )
    PH.sort()
    return PD[len(D)-1] + PD[len(D)-2] + PD[len(D)-3] + PH[len(H)-1]

def bestimmeAnzahlunterschiedlicheKarten(D, H):
    a = 0
    W = []
    for i in range(len(D)):
        if Rangordnung.count(D[i]) == 1:
            a = a + 1
        else:
            if W.count( wertEinerKarte( D[i] ) ) == 0:
                W.append( wertEinerKarte( D[i] ) )
                a = a + 1
    for i in range(len(H)):
        if Rangordnung.count(H[i]) == 1:
            a = a + 1
        else:
            if W.count(wertEinerKarte(H[i])) == 0:
                W.append(wertEinerKarte(H[i]))
                a = a + 1
    return a


def bestimmeStaerkeEinerKarte(k, D, H):
    Werte = []
    for i in range(len(D)):
        if Rangordnung.count(D[i]) == 1:
            Werte.append(D[i])
        else:
            if Werte.count("E" + wertEinerKarte( D[i] ) ) == 0:
                Werte.append("E" + wertEinerKarte( D[i] ) )
    for i in range(len(H)):
        if Rangordnung.count(H[i]) == 1:
            Werte.append(H)
        else:
            if Werte.count("E" + wertEinerKarte(H[i])) == 0:
                Werte.append("E" + wertEinerKarte(H[i]))
    if farbeEinerKarte(k) != "T":
        k = "E" + wertEinerKarte(k)
    s = 0
    for i in range(len(Werte)):
        if staerkereKarte(k, Werte[i], "T") == k:
            s = s + 1
    return s




# Eigentliches Spiel:

Mitspieler = []
if spielmodus != "Ramsch" and spielmodus != "Sauspiel" and positionDesSpielersAmTisch != positionAmTisch:
    for i in range(1, 5):
        if positionDesSpielersAmTisch != i:
            Mitspieler.append(i)
elif spielmodus != "Ramsch" and spielmodus != "Sauspiel" and positionDesSpielersAmTisch == positionAmTisch:
    for i in range(1, 5):
        if positionAmTisch == i:
            Mitspieler.append(i)
elif spielmodus == "Sauspiel" and positionDesSpielersAmTisch != positionAmTisch:
    if Handkarten.count(rufsau) == 1:
        Mitspieler = [positionAmTisch, positionDesSpielersAmTisch]
    else:
        Mitspieler = []
elif spielmodus == "Sauspiel" and positionDesSpielersAmTisch == positionAmTisch:
    Mitspieler = [positionAmTisch]
elif spielmodus == "Ramsch":
    Mitspieler = [positionAmTisch]
Mitspieler.sort()


aktuellerSpieler = 1
Ablagestapel = [ [], [], [], [] ]

for runde in range(8):

    print()
    Stich = []
    gewinnenderSpieler = aktuellerSpieler

    for durchlauf in range(4):

        if aktuellerSpieler == positionAmTisch:
            print()
            print("Ich bin am Zug.")

            # - Bot Start -

            if durchlauf == 0:
                spielbareHandkarten = Handkarten
            else:
                if spielmodus == "Sauspiel" and angespielteFarbe == farbeEinerKarte(rufsau) and Handkarten.count(rufsau) == 1:
                    spielbareHandkarten = [rufsau]
                else:
                    spielbareHandkarten = bestimmeSpielbareHandkarten(Handkarten, angespielteFarbe)

            erwartetePunkte = bestimmePunkteImStich(Stich) + bestimmePunkteImDeck(Deck) * ( 3 - durchlauf ) / len(Deck)
            maximalePunktzahlImStich =  bestimmeMaximalePunkteImStich(Deck, Handkarten)
            anzahlUnterschiedlicheKarten = bestimmeAnzahlunterschiedlicheKarten(Deck, Handkarten)

            besteKarten = []

            for i in range(len(spielbareHandkarten)):

                if durchlauf == 0:
                    staerksteKarteImStich = spielbareHandkarten[i]
                    gewinnenderSpieler = aktuellerSpieler

                punkte = erwartetePunkte + punkteEinerKarte( spielbareHandkarten[i] )
                staerke = bestimmeStaerkeEinerKarte(spielbareHandkarten[i], Deck, Handkarten)
                if spielbareHandkarten[i] == staerksteKarteImStich:
                    stichGehoertUns = True
                elif spielbareHandkarten[i] == staerkereKarte(spielbareHandkarten[i], staerksteKarteImStich, angespielteFarbe):
                    stichGehoertUns = True
                elif Mitspieler.count(gewinnenderSpieler) > 0:
                    stichGehoertUns = True
                else:
                    stichGehoertUns = False

                l = fuzzy( punkte, staerke, maximalePunktzahlImStich, stichGehoertUns, anzahlUnterschiedlicheKarten )
                l = (l - 1/3) * 3

                if spielmodus == "Ramsch":
                    l = 1 - l

                print(spielbareHandkarten[i], ": ", l)
                besteKarten.append([ l, spielbareHandkarten[i] ])

            besteKarten.sort()
            besteKarten.reverse()
            besteKarte = besteKarten[0]

            print()
            print("Meine Wahl faellt auf", besteKarte[1])
            print()
            print()

            zugespielteKarte = besteKarte[1]
            Deck.append(zugespielteKarte)
            Handkarten.pop(Handkarten.index(zugespielteKarte))
            Stich.append(zugespielteKarte)

            # - Bot End -

        else:
            print()
            print("Spieler", aktuellerSpieler, "ist am Zug:")
            zugespielteKarte = strInput(Deck)
            legen(zugespielteKarte)

        if spielmodus == "Sauspiel" and zugespielteKarte == rufsau:
            if Mitspieler == [positionAmTisch] and positionAmTisch == positionDesSpielersAmTisch:
                Mitspieler.append(aktuellerSpieler)
            elif Mitspieler == [positionAmTisch] and positionAmTisch != positionDesSpielersAmTisch:
                for i in range(1, 5):
                    if positionAmTisch != i and positionDesSpielersAmTisch != i and aktuellerSpieler != i:
                        Mitspieler.append(i)


        if durchlauf == 0:
            angespielteKarte = zugespielteKarte
            angespielteFarbe = farbeEinerKarte(zugespielteKarte)
            staerksteKarteImStich = zugespielteKarte
            gewinnenderSpieler = aktuellerSpieler

        else:

            if staerksteKarteImStich != staerkereKarte(staerksteKarteImStich, zugespielteKarte, angespielteFarbe):
                staerksteKarteImStich = staerkereKarte(staerksteKarteImStich, zugespielteKarte, angespielteFarbe)
                gewinnenderSpieler = aktuellerSpieler

            if durchlauf == 3:
                AblageDesGewinners = Ablagestapel[gewinnenderSpieler-1]
                listeUmfuellen(Stich, AblageDesGewinners)

                print()
                print("Der Stich geht an", gewinnenderSpieler)

        if durchlauf != 3:
            aktuellerSpieler = naechsterSpieler(aktuellerSpieler)
        else:
            aktuellerSpieler = gewinnenderSpieler

print()
meinePunkte = 0
for i in range(4):
    Ablage = Ablagestapel[i]
    punktzahl = bestimmePunkteImStich(Ablage)
    print()
    print("Spieler", i+1, "hat", punktzahl, "Punkte.")
    if Mitspieler.count(i+1) == 1:
        meinePunkte = meinePunkte + punktzahl

print()
print("Meine Punkte sind", meinePunkte)
print()

print(Mitspieler)

if Mitspieler.count(positionDesSpielersAmTisch) == 1:
    if meinePunkte >= 61:
        if len(Mitspieler) == 1:
            print("Juhu, ich habe gewonnen!")
        elif len(Mitspieler) >= 1:
            print("Juhu, wir haben gewonnen!")
    else:
        if len(Mitspieler) == 1:
            print("Schade, ich haben verloren.")
        elif len(Mitspieler) >= 1:
            print("Schade, wir haben verloren.")
elif Mitspieler.count(positionDesSpielersAmTisch) != 1:
    if meinePunkte >= 60:
        if len(Mitspieler) == 1:
            print("Juhu, ich habe gewonnen!")
        elif len(Mitspieler) >= 1:
            print("Juhu, wir haben gewonnen!")
    else:
        if len(Mitspieler) == 1:
            print("Schade, ich haben verloren.")
        elif len(Mitspieler) >= 1:
            print("Schade, wir haben verloren.")