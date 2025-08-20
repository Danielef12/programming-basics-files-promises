from source.analysis_modules.general_analysis import general_analysis
from source.analysis_modules.seasonal_analysis import seasonal_analysis
from source.analysis_modules.weather_extremes_analysis import weather_extremes


def print_analysis(data):
    try:
        general_results = general_analysis(data)
        extreme_results = weather_extremes(data)

        seasonal_results = seasonal_analysis(data)

        print("Analysis completed successfully!")

        if general_results:
            print("\n#### GENERAL ANALYSIS ####")
            print(
                f"- Average maximum temperature of entire dataset: {general_results['avg_max_temp']:.2f}°C"
            )
            print(
                f"    Date with highest sunshine: {general_results['max_sunshine_date']} ({general_results['max_sunshine_hours']} hours)"
            )
            print(
                f"    Total precipitation in August 2023: {general_results['aug_2023_precipitation']:.2f}mm "
            )
            print(
                f"    Percentage of Days with cloud cover > 0.5: {general_results['high_cloud_percentage']:.1f}"
            )

        max_temp_record = extreme_results.get("max_temp_record")
        if max_temp_record:
            print("\n#### WEATHER EXTREMES ANALYSIS ####")
            print(f"Highest temperature: {max_temp_record['date']}")
            print(f"    Max temp: {max_temp_record['max_temp']}")
            print(f"    Min temp: {max_temp_record['min_temp']}")
            print(f"    Mean temp: {max_temp_record['mean_temp']}")

        max_precipitation_record = extreme_results.get("max_precipitation_record")
        if max_precipitation_record:
            print(f"\nHighest precipitation: {max_precipitation_record['date']}")
            print(f"   Total: {max_precipitation_record['precipitation']} mm")

        max_snow_record = extreme_results.get("max_snow_record")
        if max_snow_record:
            print(f"\nGreatest snow depth: {max_snow_record['date']}")
            print(f"   Snow Depth: {max_snow_record['snow_depth']} cm")
            print(f"   Max temp: {max_snow_record['max_temp']}°C")

        if seasonal_results:
            print(f"\n#### SEASONAL ANALYSIS SUMMARY ####")
            print(f"    Total months analyzed: {len(seasonal_results)}")


            if seasonal_results:
                max_temp_month = max(
                    seasonal_results.items(), key=lambda x: x[1]["avg_max_temp"]
                )
                min_temp_month = min(
                    seasonal_results.items(), key=lambda x: x[1]["avg_max_temp"]
                )

                print(
                    f"    Warmest month: {max_temp_month[0]} ({max_temp_month[1]['avg_max_temp']:.2f}°C)"
                )
                print(
                    f"    Coolest month: {min_temp_month[0]} ({min_temp_month[1]['avg_max_temp']:.2f}°C)"
                )


                max_precip_month = max(
                    seasonal_results.items(), key=lambda x: x[1]["avg_precipitation"]
                )
                print(
                    f"    Wettest month: {max_precip_month[0]} ({max_precip_month[1]['avg_precipitation']:.2f}mm)"
                )

    except Exception as e:
        print(f"Error during analysis: {e}")
