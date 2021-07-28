import argparse

from todo_app.app import app
from todo_app.database import Base, engine

def create_tables():
    """Create database tables for the app"""
    Base.metadata.create_all(engine)

def run_dev_server(port: int=5000):
    """run the development server"""
    app.run(port=port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5000, type=int)

    parser.add_argument('--run-dev-server', dest='run_dev', action='store_true', default=False)

    args = parser.parse_args()

    if args.run_dev:
        port_arg = args.port
        run_dev_server(port=port_arg)
