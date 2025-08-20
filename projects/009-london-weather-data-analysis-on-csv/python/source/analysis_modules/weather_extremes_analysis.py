from typing import Any, Dict, List, Optional

from source.analysis_modules.utilities import conversion_date, float_conversion


def weather_extremes(data: List[Dict[str, str]]) -> Dict[str, Optional[Dict[str, Any]]]:
    max_temp_record = None
    max_precipitation_record = None
    max_snow_record = None

    highest_temp = float("-inf")
    highest_precipitation = float("-inf")
    highest_snow_depth = float("-inf")

    for record in data:
        date = conversion_date(record.get("date"))
        if not date:
            continue

        # calculate date with max temperature
        max_temp = float_conversion(record.get("max_temp"))
        if max_temp > highest_temp:
            highest_temp = max_temp
            max_temp_record = {
                "date": date.strftime("%Y-%m-%d"),
                "max_temp": max_temp,
                "mean_temp": float_conversion(record.get("mean_temp")),
                "min_temp": float_conversion(record.get("min_temp")),
            }

        # calculate highest precipitation
        precipitation = float_conversion(record.get("precipitation"))
        if precipitation > highest_precipitation:
            highest_precipitation = precipitation
            max_precipitation_record = {
                "date": date.strftime("%Y-%m-%d"),
                "precipitation": precipitation,
            }

        # calculate highest snow depth
        snow_depth = float_conversion(record.get("snow_depth"))
        if snow_depth > highest_snow_depth:
            highest_snow_depth = snow_depth
            max_snow_record = {
                "date": date.strftime("%Y-%m-%d"),
                "snow_depth": snow_depth,
                "max_temp": max_temp,
            }

    return {
        "max_temp_record": max_temp_record,
        "max_precipitation_record": max_precipitation_record,
        "max_snow_record": max_snow_record,
    }
