from project import db
from project.sql import BlogPost

# create the database
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("postgresql", "hello this is the first time I use postgresql!"))


# commit the changes
db.session.commit()
