import pytest
# On importe les 3 fonctions testables depuis ton fichier project.py
from project import valider_montant, calculer_rendement_reel_net, calculer_evolution


# --- TEST DE LA FONCTION DE VALIDATION ---
def test_valider_montant():
    """Vérifie que la fonction distingue correctement les montants valides des invalides."""
    # Un capital ou une durée positive doit retourner True
    assert valider_montant("100000") is True
    assert valider_montant("0") is True
    assert valider_montant("15.5") is True

    # Un montant négatif ou du texte doit retourner False
    assert valider_montant("-500") is False
    assert valider_montant("texte_invalide") is False


# --- TEST DE LA FORMULE DE L'EFFET FISHER ---
def test_calculer_rendement_reel_net():
    """Vérifie l'exactitude du calcul du taux de rendement réel net (Effet Fisher)."""
    # Cas 1 : Si l'intérêt (5%) équivaut exactement à l'inflation (5%), le rendement réel net est de 0%
    assert round(calculer_rendement_reel_net(0.05, 0.05), 4) == 0.0

    # Cas 2 : Si l'intérêt est de 10% et qu'il n'y a aucune inflation (0%), le rendement réel est de 10%
    assert round(calculer_rendement_reel_net(0.10, 0.0), 4) == 0.10

    # Cas 3 : Calcul standard (Ex: Intérêt 8%, Inflation 3%)
    # (1 + 0.08) / (1 + 0.03) - 1 = 1.08 / 1.03 - 1 = 0.04854
    assert round(calculer_rendement_reel_net(0.08, 0.03), 4) == 0.0485


# --- TEST DE LA SIMULATION TEMPORELLE ---
def test_calculer_evolution():
    """Vérifie que les listes de trajectoires nominales et réelles sont correctement générées."""
    # Simulation sur 1 an : Capital de 1000 FCFA, Intérêt de 10%, Inflation de 0%
    nominal, reel = calculer_evolution(1000, 0.10, 0.0, 1)

    # À l'année 0 : le capital doit être le capital initial (1000)
    # À l'année 1 : 1000 * 1.10 = 1100
    assert nominal == [1000.0, 1100.0]
    assert reel == [1000.0, 1100.0]
