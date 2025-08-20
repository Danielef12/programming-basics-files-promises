from collections import defaultdict
from typing import Dict, List, Tuple

from source.analysis_modules.utilities import conversion_date, float_conversion


def seasonal_analysis(data: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    # Dictionary to store monthly data: {(year, month): {'max_temps': [], 'precip': []}}
    monthly_data: Dict[Tuple[int, int], Dict[str, List[float]]] = defaultdict(
        lambda: {"max_temps": [], "precip": []}
    )

    for record in data:
        date = conversion_date(record.get("date", ""))
        if not date:
            continue

        year_month = (date.year, date.month)

        max_temp = float_conversion(record.get("max_temp", ""))
        if max_temp is not None:
            monthly_data[year_month]["max_temps"].append(max_temp)

        precip = float_conversion(record.get("precipitation", ""))
        if precip is not None:
            monthly_data[year_month]["precip"].append(precip)

    # Calculate averages for each month
    monthly_averages: Dict[str, Dict[str, float]] = {}
    month_names = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    print(f"{'Month':<12} {'Avg Max Temp':<15} {'Avg Precipitation':<18}")
    print("-" * 50)

    for (year, month), values in sorted(monthly_data.items()):
        avg_max_temp = (
            sum(values["max_temps"]) / len(values["max_temps"])
            if values["max_temps"]
            else 0
        )
        avg_precip = (
            sum(values["precip"]) / len(values["precip"]) if values["precip"] else 0
        )

        month_key = f"{year}-{month:02d}"
        monthly_averages[month_key] = {
            "avg_max_temp": avg_max_temp,
            "avg_precipitation": avg_precip,
        }

        month_name = f"{month_names[month - 1]} {year}"
        print(f"{month_name:<12} {avg_max_temp:<15.2f} {avg_precip:<18.2f}")

    return monthly_averages
