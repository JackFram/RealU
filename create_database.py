from RealU import db
from sql import BlogPost

# create the database
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))


# commit the changes
db.session.commit()
