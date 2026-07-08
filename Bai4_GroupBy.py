import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data_file/weather_by_cities.csv")

# Nhóm dữ liệu dựa trên cột city
g = df.groupby('city')
# Hiển thị dữ liệu đã được nhóm theo cột city
# for city, city_df in g:
#     print(city)
#     print(city_df)
#     print("===")
# truy cập vào 1 group cụ thể
# print(g.get_group('mumbai'))

# Lấy ra dữ liệu max của từng cột của từng nhóm
# print(g.max())

# Tính trung bình các cột theo group - numeric_only=True loại bỏ cột string
print(g.mean(numeric_only=True))
g.plot()
plt.show()

# Xem đầy đủ thông tin mô tả về dữ liệu theo nhóm
# print(g.describe())