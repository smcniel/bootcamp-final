from models import Email, db
import datetime
db.create_all()

# Seed database
mom = Email('111', 'howdy', 'daughter', 'mom', datetime.datetime.now(), 'hi')
dad = Email('111', 'hey', 'daughter', 'dad', datetime.datetime.now(), 'hiya')
dog = Email('2', 'bones', 'owner', 'doggy', datetime.datetime.now(), 'woof')

db.session.add(mom)
db.session.add(dad)
db.session.add(dog)
db.session.commit()

print('Database created')
print('Query all seed emails', Email.query.all())
