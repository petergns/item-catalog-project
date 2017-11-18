from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Universe, Base, UniChar

engine = create_engine('sqlite:///char_universe.db')
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
universe1 = Universe(name = "DC Good Characters")

session.add(universe1)
session.commit()


uniChar1 = UniChar(name = "Batman", description = "Test  0", abilities = "A", foes= "Appetizer", universe = universe1)

session.add(uniChar1)
session.commit()

uniChar2 = UniChar(name = "Superman", description = "Test 1", abilities = "B", foes = "Entree", universe = universe1)

session.add(uniChar2)
session.commit()

uniChar3 = UniChar(name = "Wonder Woman", description = "Test 2", abilities = "C", foes = "Dessert", universe = universe1)

session.add(uniChar3)
session.commit()


#Good Characters for Marvel
universe2 = Universe(name = "Marvel Good Characters")

session.add(universe2)
session.commit()


uniChar1 = UniChar(name = "Iron Man", description = "Test 3", abilities = "D", foes = "Appetizer", universe = universe2)

session.add(uniChar1)
session.commit()

uniChar2 = UniChar(name = "Spiderman", description = "Test 4", abilities = "E", foes = "Entree", universe = universe2)

session.add(uniChar2)
session.commit()

uniChar3 = UniChar(name = "Star-Lord", description = "Star-Lord aka Peter Jason Quill", abilities = "F", foes = "Dessert", universe = universe2)

session.add(uniChar3)
session.commit()


print "added menu items!"
