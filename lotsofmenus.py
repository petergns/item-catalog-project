from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Good Characters for DC
restaurant1 = Restaurant(name = "DC Good Characters")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Batman", description = "Test  0", price = "A", course = "Appetizer", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Superman", description = "Test 1", price = "B", course = "Entree", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Wonder Woman", description = "Test 2", price = "C", course = "Dessert", restaurant = restaurant1)

session.add(menuItem3)
session.commit()


#Good Characters for Marvel
restaurant2 = Restaurant(name = "Marvel Good Characters")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Iron Man", description = "Test 3", price = "D", course = "Appetizer", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Spiderman", description = "Test 4", price = "E", course = "Entree", restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Star-Lord", description = "Star-Lord aka Peter Jason Quill", price = "F", course = "Dessert", restaurant = restaurant2)

session.add(menuItem3)
session.commit()


print "added menu items!"
