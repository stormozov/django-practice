from django.shortcuts import render

from calculator.data.recipes_data import RECIPES


def index(request):
    return render(
        request,
        'calculator/index.html',
        {'recipes': list(RECIPES.keys())}
    )


def recipe_handler(request, recipe_name):
    servings = request.GET.get('servings', 1)
    servings = int(servings)
    unknown_recipe = 'Такого рецепта не знаю :('
    recipe_ingredients = RECIPES.get(recipe_name, unknown_recipe)

    context = {
        'recipe_title': recipe_name,
        'recipe_ingredients': {
            ingredient: round(amount * servings, 1) if servings != 1 else amount
            for ingredient, amount in recipe_ingredients.items()
        },
        'portion_amount': servings
    }

    return render(request, 'calculator/recipes_inner.html', context)
