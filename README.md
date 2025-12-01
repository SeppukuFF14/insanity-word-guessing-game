# Insanity Word Guessing Game

Et lite Python spill jeg laget i forbindelse med et eksamensprosjekt.

## Kort om spillet

- Leser ord fra `words.txt`
- Lar bruker velge vanskelighetsgrad (lett / medium / hard)
- Velger et hemmelig ord basert på valgte nivå
- Spilleren gjetter bokstaver til ordet er løst eller forsøkene er brukt opp
- Holder styr på gjettede bokstaver, feil og historikk for spillrundene
- Har et hint-system som kan avsløre en bokstav når spilleren nærmer seg å tape

Spillet er skrevet i ren Python og bruker blant annet:
- filhåndtering (åpne/lese tekstfil)
- lister og sets
- løkker og betingelser
- enkel state-håndtering for spillstatus
- `random`-modulen for å velge ord og hintposisjon
