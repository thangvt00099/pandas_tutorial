import pandas as pd
from matplotlib import rcParams

df = pd.read_csv(r"data_file/weather_data.csv", parse_dates=["day"])
df.set_index('day', inplace=True)

# fillna(value) - thay các missing value = giá trị được chỉ định
# new_df = df.fillna(0)

# Truyền dict để xử lí missing value theo cột
# new_df = df.fillna({
#     'temperature': 0,
#     'windspeed': 0,
#     'event': 'no event'
# })
# print(new_df)

# df.ffill()-> lấy giá trị của hàng trên gán xuống hàng bị
# missing value
# new_df = df.ffill()
# print(new_df)

# df.bfill() -> ngược với ffill()
# new_df = df.bfill()
# print(new_df)

# df.interpolate() - xử lí missing value bằng cách nội suy (linear
# interpolation)

# num_df = df[['temperature', 'windspeed']].interpolate()
# print(num_df)
#
# string_df = df[['event']].ffill()
# print(string_df)

# df.dropna(how='any') - loại bỏ những hàng có ít nhất 1 missing value
# đối số how='all' - loại bỏ những hàng giá trị các cột chỉ là missing value
# new_df = df.dropna(how='any')
# print(new_df)

# Chèn những ngày còn thiếu
dt = pd.date_range("01-01-2017", "01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)

print(df)