from datetime import datetime
from typing import Optional


def conversion_date(date_str: str) -> Optional[datetime]:
    try:
        return datetime.strptime(date_str, "%Y%m%d")
    except ValueError:
        return None


def float_conversion(value_str: str) -> float:
    try:
        return float(value_str) if value_str.strip() != "" else 0
    except (ValueError, AttributeError):
        return 0
