# Liste med spørsmål
spørsmål = [
    "Hva heter hovedstaden i Norge?",
    "Hva er 2 + 2?",
    "Hvilken skole går du på?",
    "Hva er Norges største innsjø?",
    "Hva heter Norges statsminister?",
    "Hva er hovedstaden i Sverige?",
    "Hva er 10 delt på 2?",
    "Hva heter fargen til himmelen på en klar dag?",
    "Hva er hovedstaden i Danmark?",
    "Hva heter planeten vi bor på?"
]

# Liste med riktige svar som matcher spørsmålene
svar = [
    "Oslo",
    "4",
    "Ingen",
    "Mjøsa",
    "Jonas Gahr Støre",
    "Stockholm",
    "5",
    "blå",
    "København",
    "Jorden"
]

# Teller for å holde styr på hvor mange riktige svar brukeren har
poeng = 0

# Gå gjennom hvert spørsmål i listen
for i in range(len(spørsmål)):
    # Vis spørsmålet til brukeren og ta imot svaret deres
    bruker_svar = input(spørsmål[i] + " ")
    
    # Sjekk om brukerens svar er det samme som det riktige svaret (case-insensitivt)
    if bruker_svar.strip().lower() == svar[i].lower():
        # Hvis riktig, øk poengsummen med 1
        poeng += 1
        print("Riktig!")
    else:
        # Hvis feil, si ifra til brukeren
        print("Feil! Riktig svar er:", svar[i])

# Etter alle spørsmål er besvart, skriv ut hvor mange poeng brukeren fikk
print("Du fikk", poeng, "poeng.")