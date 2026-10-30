import csv
import sys
import matplotlib.pyplot as plt


def main():
    # Vérification : l'utilisateur doit obligatoirement passer le fichier CSV en argument dans le terminal
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py scenarios.csv")

    # Récupération du nom du fichier CSV depuis les arguments de la ligne de commande
    fichier = sys.argv[1]

    # Chargement et extraction des données du fichier CSV
    scenarios = lire_scenarios(fichier)

    # Liste pour stocker les résultats calculés de chaque scénario
    donnees = []

    # Boucle pour traiter chaque scénario extrait du fichier CSV
    for scenario in scenarios:
        # Appel de la fonction pour calculer les trajectoires nominales et réelles
        nominal, reel = calculer_evolution(
            scenario["capital"],
            scenario["taux_interet"],
            scenario["taux_inflation"],
            scenario["duree"],
        )
        # Ajout des trajectoires calculées dans notre liste de données globales
        donnees.append({
            "nom": scenario["nom"],
            "nominal": nominal,
            "reel": reel,
        })

    # Génération et affichage du graphique comparatif final
    tracer_graphique(donnees)


def lire_scenarios(fichier):
    """Lit le fichier CSV et extrait une liste de dictionnaires contenant les scénarios."""
    scenarios = []
    try:
        # Ouverture sécurisée du fichier en mode lecture ('r')
        with open(fichier, "r") as file:
            # Utilisation de DictReader pour lier automatiquement la première ligne aux clés des dictionnaires
            reader = csv.DictReader(file)
            for row in reader:
                # Validation technique des données numériques avant de les charger
                if valider_montant(row["capital"]) and valider_montant(row["duree"]):
                    scenarios.append({
                        "nom": row["nom"],
                        "capital": float(row["capital"]),
                        "taux_interet": float(row["taux_interet"]),
                        "taux_inflation": float(row["taux_inflation"]),
                        "duree": int(row["duree"]),
                    })

    except FileNotFoundError:
        # Erreur si le fichier spécifié n'existe pas dans le répertoire courant
        sys.exit(f"Erreur : le fichier {fichier} n'existe pas")
    except KeyError:
        # Erreur si les entêtes de colonnes du fichier CSV sont mal orthographiées
        sys.exit("Erreur : le CSV doit contenir les colonnes nom,capital,taux_interet,taux_inflation,duree")

    # Si le fichier CSV est vide ou ne contient aucune ligne valide, on arrête le programme
    if not scenarios:
        sys.exit("Erreur : aucun scénario valide trouvé dans le fichier")

    return scenarios



def valider_montant(valeur):
    """Vérifie si une valeur (chaîne de caractères ou nombre) est convertible en numérique et positive."""
    try:
        return float(valeur) >= 0
    except ValueError:
        return False



def calculer_rendement_reel_net(taux_interet, taux_inflation):
    """Calcule le taux de rendement réel net exact d'un placement selon la formule économique de l'effet Fisher."""
    return (1 + taux_interet) / (1 + taux_inflation) - 1

def calculer_evolution(capital_initial, taux_interet, taux_inflation, duree):
    """
    Calcule année par année (de 0 à duree) la progression nominale (intérêts composés)
    et la valeur réelle ajustée de la perte de pouvoir d'achat due à l'inflation.
    """
    valeurs_nominales = []
    valeurs_reelles = []

    # Boucle pour simuler l'évolution financière année après année
    for annee in range(duree + 1):
        # Formule mathématique standard des intérêts composés pour la valeur nominale
        capital_nominal = capital_initial * (1 + taux_interet) ** annee

        # Récupération du taux réel via l'effet Fisher pour modéliser le pouvoir d'achat réel
        taux_reel = calculer_rendement_reel_net(taux_interet, taux_inflation)
        capital_reel = capital_initial * (1 + taux_reel) ** annee

        # Ajout des valeurs arrondies à 2 décimales dans leurs listes respectives
        valeurs_nominales.append(round(capital_nominal, 2))
        valeurs_reelles.append(round(capital_reel, 2))

    return valeurs_nominales, valeurs_reelles


def tracer_graphique(donnees):
    """Génère un graphique de synthèse comparant les évolutions nominales et réelles, puis l'enregistre en PNG."""
    # Définition des dimensions de la fenêtre du graphique (Largeur=10 pouces, Hauteur=6 pouces)
    plt.figure(figsize=(10, 6))

    # Palette de couleurs automatiques et distinctes fournie par matplotlib
    couleurs = plt.cm.tab10.colors

    # Boucle pour tracer les courbes de chaque scénario financier disponible
    for i, scenario in enumerate(donnees):
        annees = range(len(scenario["nominal"]))
        couleur = couleurs[i % len(couleurs)]

        # Tracé de la courbe nominale (Ligne pleine '-')
        plt.plot(annees, scenario["nominal"],
                 label=f"{scenario['nom']} - nominal",
                 color=couleur, linestyle="-")

        # Tracé de la courbe réelle ajustée de l'inflation (Ligne pointillée '--')
        plt.plot(annees, scenario["reel"],
                 label=f"{scenario['nom']} - réel (pouvoir d'achat)",
                 color=couleur, linestyle="--")

    # Habillage macroéconomique et légendes du graphique
    plt.title("Évolution du capital : nominal vs réel (ajusté inflation)")
    plt.xlabel("Années")
    plt.ylabel("Capital (FCFA)")
    plt.legend()
    plt.grid(True, alpha=0.3)  # Ajout d'une grille fine en arrière-plan pour faciliter la lecture des ordonnées
    plt.tight_layout()         # Ajustement automatique des marges pour éviter la coupure des légendes

    # Sauvegarde automatique du graphique généré sous forme d'image PNG
    plt.savefig("evolution_capital.png")
    print("Graphique sauvegardé avec succès dans 'evolution_capital.png'")

    # Affichage du graphique interactif à l'écran
    plt.show()


# Point d'entrée standard du script Python
if __name__ == "__main__":
    main()
