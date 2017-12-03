from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from database_setup import Category, CatChar, User, Base

engine = create_engine('sqlite:///charcatalog.db')
# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
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

# Create dummy user
user1 = User(name="Peter Simpson", email="petergns@udacity.com",
             picture='https://goo.gl/zxg5oL')
session.add(user1)
session.commit()

# Popular Marvel Universe Characters
category1 = Category(name="Popular Marvel Characters", user_id=1)

session.add(category1)
session.commit()

char1 = CatChar(name="Spiderman",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char1)
session.commit()

char2 = CatChar(name="Iron Man",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char2)
session.commit()

char3 = CatChar(name="Captain America",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char3)
session.commit()

char4 = CatChar(name="Deadpool",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char4)
session.commit()

char5 = CatChar(name="Daredevil",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char5)
session.commit()

char6 = CatChar(name="Doctor Strange",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char6)
session.commit()

char7 = CatChar(name="Hulk",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char7)
session.commit()

char8 = CatChar(name="Thor",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category1)
session.add(char8)
session.commit()

# Popular DC Universe Characters
category2 = Category(name="Popular DC Characters", user_id=1)

session.add(category2)
session.commit()

char1 = CatChar(name="Superman",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char1)
session.commit()

char2 = CatChar(name="Batman",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char2)
session.commit()

char3 = CatChar(name="Wonder Woman",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char3)
session.commit()

char4 = CatChar(name="Green Lantern",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char4)
session.commit()

char5 = CatChar(name="The Flash",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char5)
session.commit()

char6 = CatChar(name="Aquaman",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char6)
session.commit()

char7 = CatChar(name="Cyborg",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category2)
session.add(char7)
session.commit()

# Marvel Universe Factions
category3 = Category(name="Marvel Universe Teams", user_id=1)

session.add(char1)
session.commit()

char1 = CatChar(name="Avengers",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category3)
session.add(char1)
session.commit()

char2 = CatChar(name="Fantastic Four",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category3)
session.add(char2)
session.commit()

char3 = CatChar(name="Guardians of the Galaxy",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category3)
session.add(char3)
session.commit()

char4 = CatChar(name="X-Men",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category3)
session.add(char4)
session.commit()

# DC Universe Factions
category4 = Category(name="DC Universe Teams", user_id=1)

session.add(category4)
session.commit()

char1 = CatChar(name="Justice League",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category4)
session.add(char1)
session.commit()

char2 = CatChar(name="Green Lantern Corps",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category4)
session.add(char2)
session.commit()

char3 = CatChar(name="Suicide Squad",
                user_id=1,
                description="Lorem ipsum dolor sit amet, " +
                            "consectetuer adipiscing elit. " +
                            "Aenean massa. Cum sociis natoque" +
                            "penatibus et magnis " +
                            "dis parturient montes, nascetur ridiculus mus." +
                            " Donec quam felis.",
                category=category4)
session.add(char3)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
