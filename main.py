def two_sum(lst, target):
    """
    Trouve deux indices d'éléments dans lst qui additionnés donnent target.
    Retourne une liste avec les deux indices ou None si pas trouvé.
    """
    # 💡 Complète cette fonction en suivant la méthode en 5 étapes.
    print(lst, target)
    # parcours la liste
    for i, value_left in enumerate(lst):
        print(value_left)
        for j, value_right in enumerate(lst[i+1:]):
            if value_left + value_right == target:
                return [i, i+j+1]
    return None


# 🔍 Tests automatiques
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3], 7, None),
    ([1, 5, 3, 7], 8, [0, 3]),
]

# 🛠 Vérification des résultats
def test_function():
    for i, (lst, target, expected) in enumerate(test_cases):
        result = two_sum(lst, target)
        if result == expected:
            print(f"✅ Test {i+1} réussi !")
        else:
            print(f"❌ Test {i+1} échoué : attendu {expected}, obtenu {result}")

# 🔥 Exécute les tests
if __name__ == "__main__":
    test_function()
