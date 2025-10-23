from weather_database import WeatherDatabase, session

# function that queries the database using lat and long
def query_weather_data(latitude, longitude):
    results = session.query(WeatherDatabase).filter_by(
        latitude = latitude,
        longitude = longitude
    ).all()

# if a record is found, loop through each record and print the information
    if results:
        for record in results:
            print(f"\nID: {record.id}")
            print(f"Latitude: {record.latitude}, Longitude: {record.longitude}")
            print(f"Date: {record.month}-{record.day}-{record.year}\n")
            print(f"{'Avg Temp - 5 Yr:':<{25}} {record.avg_temp_5yr:.1f} F°")
            print(f"{'Min Temp - 5 Yr:':<{25}} {record.min_temp_5yr:.1f} F°")
            print(f"{'Max Temp - 5 Yr:':<{25}} {record.max_temp_5yr:.1f} F°")
            print(f"{'Avg Wind Speed - 5 Yr:':<{25}} {record.avg_wind_speed_5yr:.1f} MPH")
            print(f"{'Min Wind Speed - 5 Yr:':<{25}} {record.min_wind_speed_5yr:.1f} MPH")
            print(f"{'Max Wind Speed - 5 Yr:':<{25}} {record.max_wind_speed_5yr:.1f} MPH")
            print(f"{'Sum Rain - 5 Yr:':<{25}} {record.sum_rain_5yr:.3f} inch(s)")
            print(f"{'Min Rain - 5 Yr:':<{25}} {record.min_rain_5yr:.3f} inch(s)")
            print(f"{'Max Rain - 5 Yr:':<{25}} {record.max_rain_5yr:.3f} inch(s)")
    else:
        print("No weather data found.")

if __name__ == "__main__":
    query_weather_data(99, 98) #test query that only activates if the database_query script is run as main
