"""
mini-recipe v1 — Gelistirilmis implementasyon
Ogrenci: Merve Zeynep Beyazal (251478115)

Kapsam:
- init komutu calisir
- add komutu calisir
- list komutu implemente edildi
- search komutu implemente edildi
- portion komutu implemente edildi

V1 TASK LIST
1. Implement the list command to display all saved recipes
2. Implement the search command to find recipes by ingredient
3. Implement the portion command to calculate recipe scaling
"""

import sys
import os


def initialize():
    """Proje klasorini ve bos veri dosyasini olusturur."""
    if os.path.exists(".minirecipe"):
        return "Already initialized"

    os.mkdir(".minirecipe")
    file = open(".minirecipe/recipes.dat", "w")
    file.close()

    return "Initialized empty mini-recipe in .minirecipe/"


def add_recipe(recipe_name, ingredients, base_portions):
    """Yeni tarifi veri dosyasina ekler."""
    if not os.path.exists(".minirecipe"):
        return "Not initialized. Run: python minirecipe.py init"

    file = open(".minirecipe/recipes.dat", "r")
    content = file.read()
    file.close()

    if content == "":
        recipe_id = 1
    else:
        recipe_id = content.count("\n") + 1

    file = open(".minirecipe/recipes.dat", "a")
    file.write(str(recipe_id) + "|" + recipe_name + "|" + ingredients + "|" + base_portions + "\n")
    file.close()

    return "Added recipe #" + str(recipe_id) + ": " + recipe_name


def list_recipes():
    """Tum tarifleri listeler."""
    if not os.path.exists(".minirecipe"):
        return "Not initialized. Run: python minirecipe.py init"

    file = open(".minirecipe/recipes.dat", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        return "No recipes found."

    output = ""

    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            recipe_id = parts[0]
            name = parts[1]
            ingredients = parts[2]
            portions = parts[3]

            formatted_line = "[" + recipe_id + "] " + name + " | Portions: " + portions + " | Ingredients: " + ingredients

            if output == "":
                output = formatted_line
            else:
                output = output + "\n" + formatted_line

    return output


def search_recipes(search_term):
    """Malzeme ismine gore tarif arar."""
    if not os.path.exists(".minirecipe"):
        return "Not initialized. Run: python minirecipe.py init"

    file = open(".minirecipe/recipes.dat", "r")
    lines = file.readlines()
    file.close()

    output = ""

    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            recipe_id = parts[0]
            name = parts[1]
            ingredients = parts[2]
            portions = parts[3]

            if search_term.lower() in ingredients.lower():
                formatted_line = "[" + recipe_id + "] " + name + " | Portions: " + portions + " | Ingredients: " + ingredients

                if output == "":
                    output = formatted_line
                else:
                    output = output + "\n" + formatted_line

    if output == "":
        return "No recipes found with ingredient: " + search_term

    return output


def calculate_portion(recipe_id, target_portions):
    """Tarifin porsiyon katsayisini hesaplar."""
    if not os.path.exists(".minirecipe"):
        return "Not initialized. Run: python minirecipe.py init"

    try:
        recipe_id_number = int(recipe_id)
        target_portions_number = int(target_portions)
    except ValueError:
        return "Error: ID and Portions must be numbers."

    file = open(".minirecipe/recipes.dat", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            current_id = int(parts[0])
            name = parts[1]
            base_portions = int(parts[3])

            if current_id == recipe_id_number:
                multiplier = target_portions_number / base_portions
                return "Recipe #" + str(recipe_id_number) + " (" + name + ") scaled to " + str(target_portions_number) + " portions. Multiply all ingredients by " + str(multiplier) + "x"

    return "Recipe #" + str(recipe_id_number) + " not found."


# --- Ana program ---

if len(sys.argv) < 2:
    print("Usage: python minirecipe.py <command> [args]")

elif sys.argv[1] == "init":
    print(initialize())

elif sys.argv[1] == "add":
    if len(sys.argv) < 5:
        print('Usage: python minirecipe.py add "<recipe_name>" "<ingredients_comma_separated>" <base_portions>')
    else:
        print(add_recipe(sys.argv[2], sys.argv[3], sys.argv[4]))

elif sys.argv[1] == "list":
    print(list_recipes())

elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
        print('Usage: python minirecipe.py search "<ingredient>"')
    else:
        print(search_recipes(sys.argv[2]))

elif sys.argv[1] == "portion":
    if len(sys.argv) < 4:
        print("Usage: python minirecipe.py portion <id> <target_portions>")
    else:
        print(calculate_portion(sys.argv[2], sys.argv[3]))

else:
    print("Unknown command: " + sys.argv[1])