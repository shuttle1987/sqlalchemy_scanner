"""Import some data into the app using CSV files"""
import csv
import datetime
from pathlib import Path

from app import models
from app.database import SessionLocal, engine

def import_from_file(csv_path: Path) -> None
    try:
        db = SessionLocal()

        with open(str(csv_path), "r") as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                task = models.Task(
                    title=row["title"],
                    description=row["description"],
                    due_date=row["due_date"],
                    status=models.string_to_taskstatusenum(row["status"]),
                )
                db.add(task)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    import_from_file(Path("tasks.csv"))