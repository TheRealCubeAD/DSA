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



                if i == 0:
                    besterWert = l
                    besteSpielbareKarte = spielbareHandkarten[i]
                    besteKarten.append(besteSpielbareKarte)
                else:
                    if l == besterWert:
                        besteKarten.append(besteSpielbareKarte)
                    elif l > besterWert:
                        besteKarten = []
                        besteKarten.append(besteSpielbareKarte)
                        besterWert = l
                        besteSpielbareKarte = spielbareHandkarten[i]

                if i == len(spielbareHandkarten) - 1:

                    besteSpielbareKarte = besteKarten[0]
                    for i in range(1, len(besteKarten)):
                        if bestimmeStaerkeEinerKarte(besteSpielbareKarte, Deck, Handkarten) >= bestimmeStaerkeEinerKarte(besteKarten[i], Deck, Handkarten):
                            besteSpielbareKarte = besteKarten[i]

                    print()
                    print("Meine Wahl faellt auf", besteSpielbareKarte)
                    print()
                    print()

                    zugespielteKarte = besteSpielbareKarte
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