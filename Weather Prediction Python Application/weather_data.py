import requests

# class that gets and stores weather data for a specified location and date
class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.avg_temp_5yr = None
        self.min_temp_5yr = None
        self.max_temp_5yr = None
        self.avg_wind_speed_5yr = None
        self.min_wind_speed_5yr = None
        self.max_wind_speed_5yr = None
        self.sum_rain_5yr = None
        self.min_rain_5yr = None
        self.max_rain_5yr = None
        self.weather_data = []


    def get_weather_data(self):

# sets the API URL and prepares parameters for the 5 request (1 per year)
        for year in range(self.year - 4, self.year + 1):
            url = "https://archive-api.open-meteo.com/v1/archive"
            params = {
                'latitude': self.latitude,
                'longitude': self.longitude,
                'start_date': f'{year}-{self.month}-{self.day}',
                'end_date': f'{year}-{self.month}-{self.day}',
                'daily': 'wind_speed_10m_max,precipitation_sum',
                'hourly': 'temperature_2m',
                'temperature_unit': 'fahrenheit',
                'wind_speed_unit': 'mph',
                'precipitation_unit': 'inch',
                'timezone': 'America/New_York'
            }

# makes an HTTP GET request and processes the data
            myResponse = requests.get(url, params=params)
            if myResponse.ok:
                # adds the retrieved data to the weather_data list
                data = myResponse.json()
                self.weather_data.append(data)
            else:
                print(f'Error:', myResponse.status_code, '-', myResponse.reason) #if the GET request fails the status code and reason are printed to the console
                return None

        return self.weather_data


# method used to calculate the mean, max, and min temperatures in Fahrenheit
    def get_mean_temp(self):
        master_temp_list = []

        for year_data in self.weather_data:
            if 'hourly' in year_data and 'temperature_2m' in year_data['hourly']:
                temp_list = [float(temps) for temps in year_data['hourly']['temperature_2m']]
                master_temp_list.extend(temp_list)

        if master_temp_list:
            #print(master_temp_list) # - test used to ensure the correct data was aggregated
            self.avg_temp_5yr = round(sum(master_temp_list) / len(master_temp_list), 1)
            self.min_temp_5yr = min(master_temp_list)
            self.max_temp_5yr = max(master_temp_list)
            ##print(self.min_temp_5yr, self.max_temp_5yr, mean_temp)
            return self.min_temp_5yr and self.max_temp_5yr and self.avg_temp_5yr


# method used to calculate the maximum, min, and sum wind speeds in miles per hour (mph)
    def get_max_wind_speed(self):
        master_wind_list = []
        for year_data in self.weather_data:
            if 'daily' in year_data and 'wind_speed_10m_max' in year_data['daily']:
                wind_speed_list = [(wind_speed) for wind_speed in year_data['daily']['wind_speed_10m_max']]
                master_wind_list.extend(wind_speed_list)

        if master_wind_list:
            #print(master_wind_list) # - test used to ensure the correct data was aggregated
            self.avg_wind_speed_5yr = sum(master_wind_list) / len(master_wind_list)
            self.min_wind_speed_5yr = min(master_wind_list)
            self.max_wind_speed_5yr = max(master_wind_list)
            return self.avg_wind_speed_5yr and self.min_wind_speed_5yr and self.max_wind_speed_5yr


 #method used to calculate the precipitation sum, max, and min in inches
    def get_rain_inch_sum(self):
        master_sum_rain_list = []
        for year_data in self.weather_data:
            if 'daily' in year_data and 'precipitation_sum' in year_data['daily']:
                rain_list = [(rain) for rain in year_data['daily']['precipitation_sum']]
                master_sum_rain_list.extend(rain_list)

        if master_sum_rain_list:
            #print(master_sum_rain_list)  # - test used to ensure the correct data was aggregated
            self.sum_rain_5yr = sum(master_sum_rain_list)
            self.min_rain_5yr = min(master_sum_rain_list)
            self.max_rain_5yr = max(master_sum_rain_list)
            return self.min_rain_5yr and self.max_rain_5yr and self.sum_rain_5yr


#test data that will only be executed when the weather_data.py is run directly
#if __name__ == "__main__":
#    weather = WeatherData(30, 98, '08', '08', 2018)
#    test = weather.get_weather_data()
#    if test: #only prints if the test contains data from a successful API call
#       print(test)

    #test data used to ensure the methods for parsing the vars are accurate
    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

    #print(weather.get_mean_temp())
    #print(weather.get_max_wind_speed())
    #print(weather.get_rain_inch_sum())

    #\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/