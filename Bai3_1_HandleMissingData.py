import pandas as pd
import numpy as np

df = pd.read_csv("data_file/weather_data_2.csv")

# Sử dụng method replace để thay thế các validate value
# new_df = df.replace([-99999, -88888], np.nan)

# Sử dụng dict thay đổi các validate value thành 1 giá trị hợp lệ được chỉ định
# new_df = df.replace({
#     'temperature': -99999,
#     'windspeed': -99999,
#     'event': '0'
# }, np.nan)

# Sử dụng dict thay đổi validate value ở từng cột thành từng giá trị mà mình
# mong muốn ở cột đó
# new_df = df.replace({
#     -99999: np.nan,
#     'No event': 'Sunny'
# })

# Sử dụng regex để xử lí validate value
new_df = df.replace({
    'temperature': '[a-zA-Z]',
    'windspeed': '[a-zA-Z]'
}, '', regex=True)

df_2 = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average',
              'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

# Thay thế 1 list
new_df_2 = df_2.replace(['poor', 'average', 'good', 'exceptional'],
                        [1, 2, 3, 4])
print(new_df_2)