"""
mini-recipe SPEC test scenarios
Ogrenci: Merve Zeynep Beyazal (251478115)
Proje: mini-recipe
"""

import subprocess
import os
import shutil


def run_cmd(args):
    """Komutu calistirir ve stdout dondurur."""
    result = subprocess.run(
        ["python", "solution_v1.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def setup_function(function):
    """Her testten once temiz baslangic saglar."""
    if os.path.exists(".minirecipe"):
        shutil.rmtree(".minirecipe")


# --- init testleri ---

def test_init_creates_directory():
    output = run_cmd(["init"])
    assert os.path.exists(".minirecipe")
    assert os.path.exists(".minirecipe/recipes.dat")
    assert "Initialized empty mini-recipe in .minirecipe/" in output


def test_init_already_exists():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output


# --- add testleri ---

def test_add_single_recipe():
    run_cmd(["init"])
    output = run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    assert "Added recipe #1: Pancakes" in output


def test_add_second_recipe():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    output = run_cmd(["add", "Omelette", "Eggs,Cheese,Butter", "2"])
    assert "Added recipe #2: Omelette" in output


def test_add_before_init():
    output = run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    assert "Not initialized. Run: python minirecipe.py init" in output


def test_add_missing_arguments():
    run_cmd(["init"])
    output = run_cmd(["add", "Pancakes"])
    assert 'Usage: python minirecipe.py add "<recipe_name>" "<ingredients_comma_separated>" <base_portions>' in output


# --- list testleri ---

def test_list_empty():
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "No recipes found." in output


def test_list_shows_recipes():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    output = run_cmd(["list"])
    assert "[1] Pancakes" in output
    assert "Portions: 4" in output
    assert "Ingredients: Flour,Milk,Eggs" in output


# --- search testleri ---

def test_search_finds_recipe():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    run_cmd(["add", "Omelette", "Eggs,Cheese,Butter", "2"])
    output = run_cmd(["search", "Eggs"])
    assert "[1] Pancakes" in output
    assert "[2] Omelette" in output


def test_search_case_insensitive():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    output = run_cmd(["search", "eggs"])
    assert "[1] Pancakes" in output


def test_search_no_match():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    output = run_cmd(["search", "Chicken"])
    assert "No recipes found with ingredient: Chicken" in output


def test_search_missing_argument():
    run_cmd(["init"])
    output = run_cmd(["search"])
    assert 'Usage: python minirecipe.py search "<ingredient>"' in output


# --- portion testleri ---

def test_portion_existing_recipe():
    run_cmd(["init"])
    run_cmd(["add", "Pancakes", "Flour,Milk,Eggs", "4"])
    output = run_cmd(["portion", "1", "8"])
    assert "Recipe #1 (Pancakes) scaled to 8 portions. Multiply all ingredients by 2.0x" in output


def test_portion_nonexistent_recipe():
    run_cmd(["init"])
    output = run_cmd(["portion", "99", "8"])
    assert "Recipe #99 not found." in output


def test_portion_missing_argument():
    run_cmd(["init"])
    output = run_cmd(["portion", "1"])
    assert "Usage: python minirecipe.py portion <id> <target_portions>" in output


# --- genel hata testleri ---

def test_unknown_command():
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command: fly" in output


def test_missing_command():
    output = run_cmd([])
    assert "Usage: python minirecipe.py <command> [args]" in output