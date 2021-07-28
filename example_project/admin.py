import argparse

from todo_app.app import app
from todo_app.database import Base, engine

def create_tables():
    """Create database tables for the app"""
    print("Creating database tables using SQLAlchemy ORM")
    Base.metadata.create_all(engine)
    print("Done creating tables")

def drop_tables():
    """Dropping database tables for the app"""
    print("Dropping database tables using SQLAlchemy ORM")
    Base.metadata.drop_all(engine)
    print("Done dropping tables")

def run_dev_server(port: int=5000):
    """run the development server"""
    app.run(port=port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5000, type=int)

    parser.add_argument(
        '--run-dev-server',
        dest='run_dev',
        action='store_true',
        default=False,
        help="Run the flask development server",
    )
    parser.add_argument(
        '--create-tables',
        dest='create_tables',
        action='store_true',
        default=False,
        help="Create the database tables",
    )

    parser.add_argument(
        '--drop-tables',
        dest='drop_tables',
        action='store_true',
        default=False,
        help="Drop the database tables. WARNING data may be destroyed with this command.",
    )


    args = parser.parse_args()

    if args.drop_tables:
        drop_tables()

    if args.create_tables:
        create_tables()

    if args.run_dev:
        port_arg = args.port
        run_dev_server(port=port_arg)
