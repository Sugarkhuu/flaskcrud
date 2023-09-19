from app import db  # Import the database object from your Flask app
from app.models import Book  # Import your SQLAlchemy model(s)

def initialize_database():
    # Create database tables
    db.create_all()

    # Insert data into the database
    book = Book(author="Ezz", title="Cleaner Python", price=0.0)
    book2 = Book(author="Ahmed", title="Python", price=10.99)

    db.session.add(book)
    db.session.add(book2)
    db.session.commit()

if __name__ == "__main__":
    initialize_database()

# db.create_all()
# 
# db.session.add(book)
# db.session.commit()
# 
# db.session.add(book2)
# db.session.commit()