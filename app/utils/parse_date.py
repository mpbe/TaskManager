from datetime import datetime, date

def parse_date(value: str):
    return datetime.strptime(value, "%Y-%m-%d").date()
