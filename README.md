# Capital Growth Simulator: Nominal vs Real

#### Vidéo de démonstration : https://youtu.be/BKwP1U4B12A

## Description
Ce projet est un simulateur financier et macroéconomique développé en Python. Son objectif principal est de permettre aux utilisateurs (analystes, étudiants en économie ou investisseurs) d'analyser et de comparer l'évolution théorique d'un capital dans le temps selon deux indicateurs cruciaux : la valeur nominale et la valeur réelle (ajustée du taux d'inflation).

En économie, se fier uniquement à la valeur nominale d'un placement peut être trompeur. Ce programme met en évidence l'érosion du pouvoir d'achat provoquée par l'inflation à long terme. Pour cela, il s'appuie sur la formule rigoureuse de l'effet Fisher afin de calculer le rendement réel net d'un investissement. L'application extrait ses données depuis un fichier CSV, valide les montants, applique les modèles d'intérêts composés et génère automatiquement un graphique de synthèse clair sous forme d'image PNG grâce à la bibliothèque Matplotlib.

## Fonctionnalités
- **Lecture et Parsing CSV** : Extraction automatisée de différents scénarios d'investissements à partir d'un fichier source externe.
- **Validation stricte des données** : Filtrage automatique pour s'assurer que les montants des capitaux et les durées d'investissement sont valides et positifs avant tout calcul.
- **Modélisation Financière** : Calcul simultané des intérêts composés nominaux et de la dépréciation réelle basée sur l'effet Fisher.
- **Visualisation graphique de données** : Génération d'une courbe pleine pour l'évolution nominale et d'une courbe en pointillés pour l'évolution réelle, facilitant la comparaison visuelle immédiate.
- **Sauvegarde Automatique** : Exportation du graphique final directement dans le répertoire courant sous le nom `evolution_capital.png`.

## Structure des Fichiers du Projet
- **`project.py`** : C'est le script principal de l'application. Il contient la fonction principale `main()` qui orchestre le chargement, les calculs et la création du graphique. Il intègre également les trois fonctions requises et testables (`valider_montant`, `calculer_rendement_reel_net` et `calculer_evolution`).
- **`test_project.py`** : Ce fichier contient l'ensemble des tests unitaires automatisés destinés à être exécutés par la suite `pytest`. Il valide la robustesse de la fonction de tri des montants, l'exactitude de la formule de Fisher et la cohérence des listes générées lors des simulations temporelles.
- **`scenarios.csv`** : Ce fichier sert de base de données d'entrée. Il est structuré avec des en-têtes obligatoires (`nom`, `capital`, `taux_interet`, `taux_inflation`, `duree`) et permet de tester plusieurs simulations financières en une seule exécution.
- **`README.md`** : Ce document présent, écrit au format Markdown, décrivant en détail le but, les spécifications techniques et le mode d'emploi du projet.

## Instructions d'installation et d'utilisation
Pour exécuter ce projet localement, vous devez disposer de Python 3 et installer la bibliothèque de visualisation de données :

```bash
pip install matplotlib
