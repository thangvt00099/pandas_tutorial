import pandas as pd

# Read CSV file into a DataFrame
df_csv = pd.read_csv("weather_data.csv")
print(df_csv)
print("===================")

# Read Excel file into a DataFrame
df_excel = pd.read_excel("weather_data.xlsx", "Sheet1")
print(df_excel)
print("===================")

# Using Python Dictionary to create DataFrame
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
    'temperature': [32, 35, 38],
    'windspeed': [6, 7, 2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df_dict = pd.DataFrame(weather_data)
print(df_dict)
print("===================")

# Using Python List Tuple to create DataFrame
weather_data_tuple = [
    ('1/1/2017', 32, 6, 'Rain'),
    ('2/1/2017', 35, 7, 'Sunny'),
    ('3/1/2017', 38, 2, 'Snow')
]

df_list_tuple = pd.DataFrame(weather_data_tuple, columns=['day',
                                                          'temperature',
                                                          'windspeed', 'event'])
print(df_list_tuple)
print("===================")

# Using Python List (Dict is element) to create DataFrame
weather_data_dict = [
    {'day': '1/1/2017', 'temperature': 36, 'windspeed': 6, 'event': 'Rain'},
    {'day': '3/1/2018', 'temperature': 32, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '5/1/2019', 'temperature': 38, 'windspeed': 5, 'event': 'Snow'}
]

df_list_dict = pd.DataFrame(weather_data_dict)
print(df_list_dict)
