from weather_data import WeatherData
from weather_database import WeatherDatabase, session

def main():
    weather = WeatherData(41, 74, '08', '08', 2018) #data here can be changed to the desired location and date
    weather.get_weather_data()

    avg_temp_5yr = weather.get_mean_temp()
    if avg_temp_5yr is not None:
        print(avg_temp_5yr)

    max_wind_speed_5yr = weather.get_max_wind_speed()
    if max_wind_speed_5yr is not None:
        print(max_wind_speed_5yr)

    sum_rain_5yr = weather.get_rain_inch_sum()
    if sum_rain_5yr is not None:
        print(sum_rain_5yr)

    new_record = WeatherDatabase(
        latitude = weather.latitude,
        longitude = weather.longitude,
        month = weather.month,
        day = weather.day,
        year = weather.year,
        avg_temp_5yr = weather.avg_temp_5yr,
        min_temp_5yr = weather.min_temp_5yr,
        max_temp_5yr = weather.max_temp_5yr,
        avg_wind_speed_5yr = weather.avg_wind_speed_5yr,
        min_wind_speed_5yr = weather.min_wind_speed_5yr,
        max_wind_speed_5yr = weather.max_wind_speed_5yr,
        sum_rain_5yr = weather.get_rain_inch_sum(),
        min_rain_5yr = weather.min_rain_5yr,
        max_rain_5yr = weather.max_rain_5yr
    )

    session.add(new_record)
    session.commit()
    print('Data committed successfully')

if __name__ == '__main__':
    main()

