from flask import (
	Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
	)

import firebase_admin
from firebase_admin import db

if (not len(firebase_admin._apps)):
	firebase_admin.initialize_app(options={
		'databaseURL' : 'https://misohungry-96a55.firebaseio.com/'
		})

RECIPE = db.reference("recipes")

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def list_recipe():
	materials = request.form.getlist('material')
	materials[:] = [x for x in materials if x!='']


	list_of_recipe = []
	#Here is the query algorithm, but it is pretty slow
	#TODO: faster algorithm needed
	for recipe in RECIPE.get():
		try:
			ing = recipe['ingredients']
			ing = ' '.join(ing)
			ct = 0
			for m in materials:
				if m in ing or m.lower() in ing:
					ct+=1
			if len(materials) == ct:
				list_of_recipe.append(recipe)
		except:
			pass

	return render_template('recipes.html', list_of_recipe = list_of_recipe)

@app.route('/<recipe>')
def displayRecipe(recipe):
	for r in RECIPE.get():
		if r['title'] == recipe:
			recipe = r
			break
	return render_template('display_recipe.html', recipe = recipe)
