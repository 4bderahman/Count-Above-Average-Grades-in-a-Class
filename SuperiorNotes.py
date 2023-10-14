
notes = [0.0] * 10
somme = 0.0 

for i in range(10):
    notes[i] = float(input(f"Entrez la note de l'étudiant {i + 1} : "))
    somme += notes[i]

moyenne = somme / 10
print("la moyenne de class est:", moyenne)

c = 0 

for i in range(10):
    if note[i] > moyenne:
        c += 1

print(f"Le nombre de notes supérieures à la moyenne est : {c}")
