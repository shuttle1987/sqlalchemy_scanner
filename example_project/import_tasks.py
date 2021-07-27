"""Import some data into the app using CSV files"""

import csv
import datetime

from app import models
from app.database import SessionLocal, engine

if __name__ == "__main__":
    try:
        db = SessionLocal()

        with open("tasks.csv", "r") as f:
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