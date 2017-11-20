from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Universe, CatChar


#Connect to Database and create database session
engine = create_engine('sqlite:///universecat.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#JSON APIs to view Restaurant Information
@app.route('/universe/<int:universe_id>/cat/JSON')
def universeCatJSON(universe_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    chars = session.query(CatChar).filter_by(universe_id = universe_id).all()
    return jsonify(CatChars=[i.serialize for i in chars])


@app.route('/universe/<int:universe_id>/cat/<int:cat_id>/JSON')
def catCharJSON(universe_id, cat_id):
    Cat_Char = session.query(CatChar).filter_by(id = cat_id).one()
    return jsonify(Cat_Char = Cat_Char.serialize)

@app.route('/universe/JSON')
def universesJSON():
    universes = session.query(Universe).all()
    return jsonify(universes= [r.serialize for r in universes])


#Show all restaurants
@app.route('/')
@app.route('/universes/')
def showUniverses():
  universes = session.query(Universe).order_by(asc(Universe.name))
  return render_template('universes.html', universes = universes)

#Create a new restaurant
@app.route('/universe/new/', methods=['GET','POST'])
def newUniverse():
  if request.method == 'POST':
      newUniverse = Universe(name = request.form['name'])
      session.add(newUniverse)
      flash('New Universe %s Successfully Created' % newUniverse.name)
      session.commit()
      return redirect(url_for('showUniverses'))
  else:
      return render_template('newUniverse.html')

#Edit a restaurant
@app.route('/universe/<int:universe_id>/edit/', methods = ['GET', 'POST'])
def editUniverse(universe_id):
  editedUniverse = session.query(Universe).filter_by(id = universe_id).one()
  if request.method == 'POST':
      if request.form['name']:
        editedUniverse.name = request.form['name']
        flash('Universe Successfully Edited %s' % editedUniverse.name)
        return redirect(url_for('showUniverses'))
  else:
    return render_template('editUniverse.html', universe = editedUniverse)


#Delete a restaurant
@app.route('/universe/<int:universe_id>/delete/', methods = ['GET','POST'])
def deleteUniverse(universe_id):
  universeToDelete = session.query(Universe).filter_by(id = universe_id).one()
  if request.method == 'POST':
    session.delete(universeToDelete)
    flash('%s Successfully Deleted' % universeToDelete.name)
    session.commit()
    return redirect(url_for('showUniverses', universe_id = universe_id))
  else:
    return render_template('deleteUniverse.html',universe = universeToDelete)

#Show a restaurant menu
@app.route('/universe/<int:universe_id>/')
@app.route('/universe/<int:universe_id>/cat/')
def showCat(universe_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    chars = session.query(CatChar).filter_by(universe_id = universe_id).all()
    return render_template('cat.html', chars = chars, universe = universe)



#Create a new menu item
@app.route('/universe/<int:universe_id>/cat/new/',methods=['GET','POST'])
def newCatChar(universe_id):
  universe = session.query(Universe).filter_by(id = universe_id).one()
  if request.method == 'POST':
      newChar = CatChar(name = request.form['name'], description = request.form['description'], abilities = request.form['abilities'], alignment = request.form['alignment'], universe_id = universe_id)
      session.add(newChar)
      session.commit()
      flash('New Category %s Character Successfully Created' % (newChar.name))
      return redirect(url_for('showCat', universe_id = universe_id))
  else:
      return render_template('newcatchar.html', universe_id = universe_id)

#Edit a menu item
@app.route('/universe/<int:universe_id>/cat/<int:cat_id>/edit', methods=['GET','POST'])
def editCatChar(universe_id, cat_id):

    editedChar = session.query(CatChar).filter_by(id = cat_id).one()
    universe = session.query(Universe).filter_by(id = universe_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedChar.name = request.form['name']
        if request.form['description']:
            editedChar.description = request.form['description']
        if request.form['abilities']:
            editedChar.abilities = request.form['abilities']
        if request.form['alignment']:
            editedChar.alignment = request.form['alignment']
        session.add(editedChar)
        session.commit()
        flash('Category Character Successfully Edited')
        return redirect(url_for('showCat', universe_id = universe_id))
    else:
        return render_template('editcatchar.html', universe_id = universe_id, cat_id = cat_id, char = editedChar)


#Delete a category character
@app.route('/universe/<int:universe_id>/cat/<int:cat_id>/delete', methods = ['GET','POST'])
def deleteCatChar(universe_id,cat_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    charToDelete = session.query(CatChar).filter_by(id = cat_id).one()
    if request.method == 'POST':
        session.delete(charToDelete)
        session.commit()
        flash('Category Character Successfully Deleted')
        return redirect(url_for('showCat', universe_id = universe_id))
    else:
        return render_template('deleteCatChar.html', char = charToDelete)




if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
