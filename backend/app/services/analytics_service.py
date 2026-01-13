from app.db.database import SessionLocal
from app.db.models import LoadHistory

def get_national_load_series(limit=500):
    db = SessionLocal()
    rows = (
        db.query(LoadHistory)
        .order_by(LoadHistory.timestamp.desc())
        .limit(limit)
        .all()
    )
    db.close()

    return [{"t": r.timestamp.isoformat(), "load": r.load, "city": r.city} for r in reversed(rows)]


def get_regional_load_series(city, limit=500):
    db = SessionLocal()
    rows = (
        db.query(LoadHistory)
        .filter(LoadHistory.city.ilike(city))
        .order_by(LoadHistory.timestamp.desc())
        .limit(limit)
        .all()
    )
    db.close()

    if not rows:
        return {"error": f"No data found for city '{city}'"}

    return [{"t": r.timestamp.isoformat(), "load": r.load} for r in reversed(rows)]
