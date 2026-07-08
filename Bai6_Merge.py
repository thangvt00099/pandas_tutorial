import pandas as pd

df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "baltimore"],
    "temperature": [21, 12, 36, 32]
})

df2 = pd.DataFrame({
    "city": ["chicago", "new york", "orlando", "san francisco"],
    "humidity": [65, 58, 67, 55]
})

# InnerJoin trong SQL - merge các trường dữ liệu có khóa chung (primary key)
df_merged_inner = pd.merge(df1, df2, on="city")

# OuterJoin - merge tất cả lại với nhau | indicator=True - xem dữ liệu ở dataframe nào
df_merged_outer = pd.merge(df1, df2, on="city", how="outer", indicator=True)

# LeftJoin - merge lấy phần giao và dữ liệu dataframe bên trái
df_merged_left = pd.merge(df1, df2, on="city", how="left")

# RightJoin - merge lấy phần giao và dữ liệu dataframe bên phải
df_merged_right = pd.merge(df1, df2, on="city", how="right")
print("======================================================")

# Nếu dữ liệu các key trùng khác nhau ở 2 frame -> suffixes (hậu tố) để phân biệt
df3 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "baltimore"],
    "temperature": [21, 14, 35, 38],
    "humidity": [65, 68, 71, 75],
})

df4 = pd.DataFrame({
    "city": ["chicago", "new york", "san diego"],
    "temperature": [21, 14, 35],
    "humidity": [65, 68, 71],
})

print(pd.merge(df3, df4, on="city", suffixes=["_left", "_right"]))