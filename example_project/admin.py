from todo_app.database import Base, engine

def create_tables():
    """Create database tables for the app"""
    Base.metadata.create_all(engine)

