from weather_data import WeatherData
from weather_database import WeatherDatabase, session

#ensures an error-code and error message are generated for an invalid query
def test_invalid_query():
    weather = WeatherData(999, 999, '99', '99', 9999)
    weather.get_weather_data()

#if the request fails, a second failsafe check confirms the data was not populated
    if weather.get_mean_temp() is not None:
        print('\nTest 1: Fail\n') #fail
    else:
        print('\nTest 1: Pass\n') #pass


#attempts to insert new data into the database and then queries the database to make sure it was successful
def test_data_insertion():
    weather = WeatherData(50, 50, '10', '10', 2010)
    weather.get_weather_data()

    new_record = WeatherDatabase(
        latitude=weather.latitude,
        longitude=weather.longitude,
        month=weather.month,
        day=weather.day,
        year=weather.year,
        avg_temp_5yr=weather.avg_temp_5yr,
        min_temp_5yr=weather.min_temp_5yr,
        max_temp_5yr=weather.max_temp_5yr,
        avg_wind_speed_5yr=weather.avg_wind_speed_5yr,
        min_wind_speed_5yr=weather.min_wind_speed_5yr,
        max_wind_speed_5yr=weather.max_wind_speed_5yr,
        sum_rain_5yr=weather.get_rain_inch_sum(),
        min_rain_5yr=weather.min_rain_5yr,
        max_rain_5yr=weather.max_rain_5yr
    )

    session.add(new_record)
    session.commit()

    results = session.query(WeatherDatabase).filter_by(
        latitude=50,
        longitude=50
    ).first()

    if results:
        assert results.latitude == 50
        assert results.longitude == 50
        print('\nTest 2: Pass')#pass
    else:
        print('\nTest 2: Fail')#fail


#test confirms that the function get_mean_temp is generating the correct data type (float)
def test_get_mean_temp():
    weather = WeatherData(50, 50, '10', '10', 2010)
    weather.get_weather_data()
    if isinstance(weather.get_mean_temp(), float):
        print('\nTest 3: Pass')#pass
    else:
        print('\nTest 3: Fail')#fail


if __name__ == '__main__':
    test_invalid_query()
    test_data_insertion()
    test_get_mean_temp()