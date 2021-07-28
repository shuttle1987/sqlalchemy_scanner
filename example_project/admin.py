from todo_app.add import app
from todo_app.database import Base, engine

def create_tables():
    """Create database tables for the app"""
    Base.metadata.create_all(engine)

def run_dev_server(port: int=5000):
    """run the development server"""
    app.run(port=port)
