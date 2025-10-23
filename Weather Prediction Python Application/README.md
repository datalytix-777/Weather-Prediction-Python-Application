Weather Data Collection Program

- Commands needed to run - 
  - 
  - 1.) Clone the appropriate repository branch
        
        git clone --branch weather-prediction-python-application https://gitlab.com/wgu-gitlab-environment/student-repos/chil657/d493-scripting-and-programming-applications.git
  
  - 2.) Go to new directory
  - 
        cd d493-scripting-and-programming-applications

    3.) Install dependencies via requirements.txt
  -  
        pip install -r requirements.txt
  
    4.) Run the program that queries the database
  - 
        python database_query.py

-------------------------------------------------------------------
Inputs:
-
    Latitude: the latitude of the desired locale (e.g., 30)

    Longitude: the longitude of the desired locale (e.g., 98)

    Date: The date that you want weather data for input as month, day, year.

-------------------------------------------------------------------
Outputs:
  -
    Weather data for the past 5 years
    
    Queried data from the SQLite database

-------------------------------------------------------------------
Example of Usage:
-
Querying the SQLite DB for an existing record:
    
    from database_query import query_weather_data

    query_weather_data(30, 98)

Get the Mean temperature for a given day:

    from weather_data import WeatherData

    weather = WeatherData(30, 98, '08', '08', 2018)
    weather.get_weather_data()

    print(weather.get_mean_temp())

Add a record to the Database:
    
    from weather_data import WeatherData
    from weather_database import WeatherDatabase, session

    weather = WeatherData(50, 50, '10', '10', 2010) #Change to the desired Lat/Long and Date
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




