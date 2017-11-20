from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Universe, Base, CatChar

engine = create_engine('sqlite:///universecat.db')
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


catChar1 = CatChar(name = "Batman", description = "Test  0", abilities = "A", alignment= "Good", universe = universe1)

session.add(catChar1)
session.commit()

catChar2 = CatChar(name = "Superman", description = "Test 1", abilities = "B", alignment = "Neutral", universe = universe1)

session.add(catChar2)
session.commit()

catChar3 = CatChar(name = "Wonder Woman", description = "Test 2", abilities = "C", alignment = "Fluid", universe = universe1)

session.add(catChar3)
session.commit()


#Good Characters for Marvel
universe2 = Universe(name = "Marvel Good Characters")

session.add(universe2)
session.commit()


catChar1 = CatChar(name = "Iron Man", description = "Test 3", abilities = "D", alignment = "Good", universe = universe2)

session.add(catChar1)
session.commit()

catChar2 = CatChar(name = "Spiderman", description = "Test 4", abilities = "E", alignment = "Neutral", universe = universe2)

session.add(catChar2)
session.commit()

catChar3 = CatChar(name = "Star-Lord", description = "Star-Lord aka Peter Jason Quill", abilities = "F", alignment = "Fluid", universe = universe2)

session.add(catChar3)
session.commit()


print "added universe characters!"
