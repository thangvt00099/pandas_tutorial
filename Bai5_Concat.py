import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 39],
    "humidity": [80, 60, 78]
})

us_weather = pd.DataFrame({
    "city": ["new york", "chicago", "orlando"],
    "temperature": [21, 14, 35],
    "humidity": [68, 65, 75]
})

# Nối 2 data frame | ignore_index - chỉ mục có thứ tự
df = pd.concat([india_weather, us_weather], ignore_index=True)

# Nối 2 data frame | keys - phân cấp
df_2 = pd.concat([india_weather, us_weather], keys=["india", "us"])

# Truy cập riêng thời tiết ở india
print(df_2.loc["india"])
print("==========================================")

temperature_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 39],
})

windspeed_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "windspeed": [7, 12, 9],
})

# Nối 2 data frame nhưng theo chiều ngang (thêm cột) | axis=0 (thêm hàng) |
# axis=1 (thêm cột)
df_3 = pd.concat([temperature_df, windspeed_df], axis=1)
print(df_3)
print("==========================================")

# Sử dụng index để ràng buộc thứ tự các index khi xảy ra TH dữ liệu các
# DataFrame không giống thứ tự nhau
temperature_df2 = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 39],
}, index=[0, 1, 2])

windspeed_df2 = pd.DataFrame({
    "city": ["delhi", "mumbai"],
    "windspeed": [7, 12],
}, index=[1, 0])
df_4 = pd.concat([temperature_df2, windspeed_df2], axis=1)
print(df_4)
print("==========================================")

# Kết hợp 1 Data Frame với 1 Series
temperature_df3 = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 31],
})

s = pd.Series(["Humid", "Dry", "Rain"], name="event")
df_5 = pd.concat([temperature_df3, s], axis=1)
print(df_5)
