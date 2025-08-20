from typing import Any, Dict, List

from source.analysis_modules.utilities import conversion_date, float_conversion


def general_analysis(data: List[Dict[str, str]]) -> Dict[str, Any]:
    max_temps = []
    sunshine_date = []
    cloud_cover_data = []

    for record in data:
        # Calculate max temperature of entire dataset
        max_temp = float_conversion(record.get("max_temp"))
        if max_temp:
            max_temps.append(max_temp)

        # Calculate day of max sunshine hours
        sunshine = float_conversion(record.get("sunshine"))
        date = conversion_date(record.get("date"))
        if sunshine and date:
            sunshine_date.append((date, sunshine, record.get("date")))

        # Calculate cloud cover
        cloud_cover = float_conversion(record.get("cloud_cover"))
        if cloud_cover:
            cloud_cover_data.append(cloud_cover)

    avg_max_temp = sum(max_temps) / len(max_temps) if max_temps else 0

    # Calculate date with max sunshine hours
    max_sunshine_date = None
    max_sunshine_hours = None
    if sunshine_date:
        max_sunshine_entry = max(sunshine_date, key=lambda x: x[1])
        max_sunshine_date = max_sunshine_entry[0].strftime("%Y-%m-%d")
        max_sunshine_hours = max_sunshine_entry[1]

    # Calculate total precipitation for August 2023
    aug_2023_precipitation = 0
    for record in data:
        date = conversion_date(record.get("date"))
        if date and date.year == 2023 and date.month == 8:
            precipitation = float_conversion(record.get("precipitation"))
            if precipitation:
                aug_2023_precipitation += precipitation

    # Calculate percentage of days with cloud cover > 0.5
    high_cloud_day = sum(1 for cc in cloud_cover_data if cc > 0.5)
    cloud_percentage = (high_cloud_day / len(data)) * 100

    return {
        "avg_max_temp": avg_max_temp,
        "max_sunshine_date": max_sunshine_date,
        "max_sunshine_hours": max_sunshine_hours,
        "aug_2023_precipitation": aug_2023_precipitation,
        "high_cloud_percentage": cloud_percentage,
    }
