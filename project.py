from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Universe, MenuItem


#Connect to Database and create database session
engine = create_engine('sqlite:///char_universe.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#JSON APIs to view Restaurant Information
@app.route('/universe/<int:universe_id>/char/JSON')
def restaurantMenuJSON(universe_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    items = session.query(MenuItem).filter_by(universe_id = universe_id).all()
    return jsonify(UniChars=[i.serialize for i in items])


@app.route('/universe/<int:universe_id>/char/<int:char_id>/JSON')
def menuItemJSON(universe_id, char_id):
    Menu_Item = session.query((UniChar).filter_by(id = char_id).one()
    return jsonify(Uni_Char = (Uni_Char.serialize)

@app.route('/universe/JSON')
def universesJSON():
    universes = session.query(Universe).all()
    return jsonify(universes= [r.serialize for r in universes])


#Show all restaurants
@app.route('/')
@app.route('/universe/')
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
    return render_template('deleteUniverse.html', universe = universeToDelete)

#Show a restaurant menu
@app.route('/universe/<int:universe_id>/')
@app.route('/universe/<int:universe_id>/char/')
def showChar(universe_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    chars = session.query(UniChar).filter_by(universe_id = universe_id).all()
    return render_template('char.html', chars = chars, universe = universe)



#Create a new menu item
@app.route('/universe/<int:universe_id>/char/new/',methods=['GET','POST'])
def newMenuItem(universe_id):
  universe = session.query(Universe).filter_by(id = universe_id).one()
  if request.method == 'POST':
      newItem = UniChar(name = request.form['name'], description = request.form['description'], abilties = request.form['abilties'], foes = request.form['foes'], universe_id = universe_id)
      session.add(newChar)
      session.commit()
      flash('New Character %s Item Successfully Created' % (newChar.name))
      return redirect(url_for('showChar', universe_id = universe_id))
  else:
      return render_template('newmenuitem.html', universe_id = universe_id)

#Edit a menu item
@app.route('/universe/<int:universe_id>/menu/<int:char_id>/edit', methods=['GET','POST'])
def editUniChar(universe_id, char_id):

    editedChar = session.query(UniChar).filter_by(id = char_id).one()
    universe = session.query(Universe).filter_by(id = universe_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedChar.name = request.form['name']
        if request.form['description']:
            editedChar.description = request.form['description']
        if request.form['abilties']:
            editedChar.price = request.form['abilties']
        if request.form['foes']:
            editedChar.course = request.form['foes']
        session.add(editedItem)
        session.commit()
        flash('Universe Character Successfully Edited')
        return redirect(url_for('showMenu', universe_id = universe_id))
    else:
        return render_template('editmenuitem.html', universe_id = universe_id, char_id = char_id, char = editedChar)


#Delete a menu item
@app.route('/universe/<int:universe_id>/char/<int:char_id>/delete', methods = ['GET','POST'])
def deleteUniChar(universe_id,char_id):
    universe = session.query(Universe).filter_by(id = universe_id).one()
    charToDelete = session.query(UniChar).filter_by(id = char_id).one()
    if request.method == 'POST':
        session.delete(charToDelete)
        session.commit()
        flash('Universe Character Successfully Deleted')
        return redirect(url_for('showChar', universe_id = universe_id))
    else:
        return render_template('deleteUniChar.html', char = charToDelete)




if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
