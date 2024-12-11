# # tall1 = 8
# # tall2 = 4
# # print (tall1 + tall2)
# # print ("TAll1 + TAll2 = ", tall1 + tall2)
# # print(tall1, "+", tall2, "=", (tall1 + tall2))

# # tall = 20
# # if tall > 15:
# #     print ("Tall", tall, "er et positivt tall")
# # elif tall < 0 ("Tall", tall, "er et negativt tall")
# # else: 
# #     print ("Tall", tall, "tall er bare 0")
    
# # for x in range (1, 20, 5):
# #     print(x)
    
# #! Oppgave 1 Kalkulator

# def kalkulator():
#     print("Velg operasjon:")
#     print("1. Addisjon")
#     print("2. Subtraksjon")
#     print("3. Multiplikasjon")
#     print("4. Divisjon")

#     valg = input("Tast inn valg (1/2/3/4): ")
#     tall1 = float(input("Tast inn første tall: "))
#     tall2 = float(input("Tast inn andre tall: "))

#     if valg == '1':
#         print(f"Resultat: {tall1} + {tall2} = {tall1 + tall2}")
#     elif valg == '2':
#         print(f"Resultat: {tall1} - {tall2} = {tall1 - tall2}")
#     elif valg == '3':
#         print(f"Resultat: {tall1} * {tall2} = {tall1 * tall2}")
#     elif valg == '4':
#         if tall2 != 0:
#             print(f"Resultat: {tall1} / {tall2} = {tall1 / tall2}")
#         else:
#             print("Feil: Kan ikke dele med null.")
#     else:
#         print("Ugyldig valg.")

# kalkulator()

#! Forskjellen mellom js og py:

#? Python bruker input og print for interaksjon og JavaScript bruker prompt og console.log

#? Syntaks: Python har en enklere og mer lesbar syntaks for nye, mens JavaScript bruker switch-blokker

#? Error Handling: Python gir en feilmelding direkte hvis du deler med null, mens JavaScript krever en sjekk i koden.

#! Oppgave 2 Geometri 

# lengde = 6
# bredde = 8
# areal = lengde * bredde
# print(f"Arealet av rektangelet er {areal} kvadratmeter.")

#! Forskjellen mellom js og py:

#? Variabler: Python bruker dynamiske variabler uten deklarasjon. JavaScript bruker const for konstant variabler. 

#? Syntaks: JavaScript krever semikolon for å avslutte linjer ikke python.

#! Oppgave 3 Interaktiv

# navn = input("Hva heter du? ")
# alder = int(input("Hvor gammel er du? "))
# år_til_100 = 100 - alder
# print(f"Hei {navn}, du fyller 100 år om {år_til_100} år.")

#! Forskjellen mellom js og py:

#? Datatyper: Python bruker int for konvertering, JavaScript bruker parseInt

#? Brukerinput: Python bruker input og antar, JavaScript krever eksplisitt konvertering.

#! Oppgave 4 Positiv/Negativ kontroll

# nummer = float(input("Tast inn et tall: "))

# if nummer > 0:
#     print("Tallet er positivt.")
# elif nummer < 0:
#     print("Tallet er negativt.")
# else:
#     print("Tallet er null.")
    
#! Forskjellen mellom js og py:

#? Nummer: Python bruker number mens javascript på skrive const nummer

#? Python bruker if, elif og else, mens JavaScript bruker if, else if og else

#? Begge språkene bruker print() og console.log() for å vise

#! Oppgave 5 SUM

# n = int(input("Tast inn et tall: "))
# sum_tall = sum(range(1, n + 1))
# print(f"Summen av tallene fra 1 til {n} er {sum_tall}.")

#! Forskjellen mellom js og py:

#? Python bruker innebygd sum for enkel summering, mens JavaScript krever en eksplisitt løkke.

#! Oppgave 6 Listebehandling

# navn_liste = []
# navn_liste.append(input("Tast inn navn 1: "))
# navn_liste.append(input("Tast inn navn 2: "))
# navn_liste.append(input("Tast inn navn 3: "))
# navn_liste.append(input("Tast inn navn 4: "))
# navn_liste.append(input("Tast inn navn 5: "))
# print(f"Navnelisten: {navn_liste}")

#! Forskjellen mellom js og py:

#? Python bruker lister mens javascript må bruke array

#! Oppgave 7 Listebehandling 2

# navn_liste = []
# for i in range(5):
#     navn = input(f"Tast inn navn {i+1}: ")
#     navn_liste.append(navn)
# print(f"Navnelisten: {navn_liste}")

#! Forskjellen mellom js og py:

#? Python bruker for i in range, mens JavaScript bruker for

#! Oppgave 8 Funksjonsbruk

# def sorter_og_beregn_gjennomsnitt(liste):
#     liste.sort()
#     gjennomsnitt = sum(liste) / len(liste)
#     return gjennomsnitt

# resultat = sorter_og_beregn_gjennomsnitt([4, 1, 7, 3, 9])
# print(f"Gjennomsnittet er {resultat}")

#! Forskjellen mellom js og py

#? Python bruker def mens JavaScript bruker function

#! Oppgave 9 Snurr

# liste = [1, 2, 3, 4, 5]
# snudd_liste = liste[::-1]
# print(f"Den snudde listen: {snudd_liste}")

#! Forskjellen mellom js og py

#? Python bruker slicing, mens JavaScript bruker reverse() jeg syns java er lettere å lese her