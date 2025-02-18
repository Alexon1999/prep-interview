def three_sum(lst, target):
    """
    Trouve trois indices d'éléments dans lst qui additionnés donnent target.
    Retourne une liste avec les trois indices ou None si pas trouvé.
    """
    # 💡 Implémente ta solution ici !
    pass  # Remplace "pass" par ton code

# 🔍 Tests automatiques
test_cases = [
    ([1, 2, 3, 4, 5], 9, [0, 2, 3]),
    ([2, 7, 4, 0, 9], 13, [0, 1, 2]),
    ([3, 1, 4, 6, 5], 10, [1, 2, 4]),
    ([1, 1, 1, 1], 10, None),
]

# 🛠 Vérification des résultats
def test_function():
    for i, (lst, target, expected) in enumerate(test_cases):
        result = three_sum(lst, target)
        if result == expected:
            print(f"✅ Test {i+1} réussi !")
        else:
            print(f"❌ Test {i+1} échoué : attendu {expected}, obtenu {result}")

# 🔥 Exécute les tests
if __name__ == "__main__":
    test_function()
