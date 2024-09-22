
import random
import csv

def lire_scores():
    try:
        with open('score.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            scores = {row[0]: int(row[1]) for row in reader}
            return scores
    except FileNotFoundError:
        return {}

def enregistrer_score(scores):
    with open('score.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for nom, score in sorted (scores.items(), key=lambda item: item[1])[:3]:
            writer.writerow([nom, score])

def reinitialiser_scores():
    with open('score.csv', 'w', newline='') as csvfile:
        pass

scores = lire_scores()

while True:
    choix = input('''
    --------------------------
    | 1. Jouer               |
    | 2. Afficher les scores |
    | 3. Réinitialiser       |
    | 4. Quitter             |
    --------------------------
    Choix : ''')

    if choix == '1':
        print("Debut du jeu")
        i = random.randint(1, 100)
        score = 0

        nom_joueur = input("Entrez votre nom : ")

        while True:
            joueur = input("Entrez une valeur entre 1 et 100 (ou 'q' pour quitter) : ")
            if joueur.lower() == 'q':
                print("Fin du jeu")
                break

            if not joueur.isdigit() or not 1 <= int(joueur) <= 100:
                print("Erreur : Entrez un nombre entre 1 et 100.")
                continue

            joueur = int(joueur)
            score += 1

            if joueur == i:
                print('Bravo, vous avez trouvé le nombre mystère en', score, 'tentatives !')
                scores[nom_joueur] = score
                enregistrer_score(scores)
                break
            elif joueur < i:
                print("Plus grand !")
            else:
                print("Plus petit !")

    elif choix == '2':
        if scores:
            print("Meilleurs scores :")
            for j,(nom, score) in enumerate(sorted(scores.items(), key=lambda item: item[1]), start=1):
                print(f"{j}. {nom} : {score}")
        else:
            print("Pas de scores enregistrés.")

    elif choix == '3':
        reinitialiser_scores()
        scores = []
        print("Scores réinitialisés avec succès.")

    elif choix == '4':
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Veuillez saisir un nombre entre 1 et 4.")