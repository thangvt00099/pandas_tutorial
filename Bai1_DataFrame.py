import pandas as pd

# Tạo DataFrame đọc file csv - pd.read_csv
# df = pd.read_csv("weather_data.csv")

# Tạo DataFrame bằng dictionary - pd.DataFrame
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017',
            '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}

df = pd.DataFrame(weather_data)
print(df)
print("===============")

# In shape của DataFrame - return 1 tuple (hàng, cột)
print(df.shape)
rows, columns = df.shape
print(f"Rows DataFrame: {rows}, Columns DataFrame: {columns}")
print("===============")

# In ra 1 vài hàng đầu tiên hoặc cuối cùng - df.head(rows) | df.tail(rows)
print(df.head())
print(df.tail())
print("===============")

# Dùng list slicing python để in số hàng nhất định
print(df[2:5])
print("===============")

# df.columns -> return 1 oject chứa các cột
# In cột mong muốn
print(df.event) # df.name_column
print("===============")
print(df['event']) # df['name_col']
print("===============")

# In nhiều cột một lúc
print(df[['event', 'day', 'temperature']])
print("===============")

# In ra nhiệt độ cao nhất của cột temperature - max()
print("Max temperature: ", df['temperature'].max())
print("===============")

# In ra nhiệt độ thấp nhất của cột temperature - min()
print("Min temperature: ", df['temperature'].min())
print("===============")

# In ra độ lệch chuẩn của cột temperature - std()
print("Std temperature: ", df.temperature.std())
print("===============")

# In ra trung bình nhiệt độ của cột temperature - mean()
print("Mean temperature: ", df['temperature'].mean())
print("===============")

# In ra số liệu thống kê về tập dữ liệu đối với các cột số
print(df.describe())
print("===============")

# Chọn dữ liệu có điều kiện - chọn hàng dữ liệu có cột temperature >= 32 độ
print(df[df['temperature'] >= 32])
print("===============")

# Chọn hàng dữ liệu có cột temperature == nhiệt độ cao nhất
print(df[df['temperature'] == df['temperature'].max()])
print("===============")

# In các cột được chỉ định nhưng phải thỏa mãn điều kiện dữ liệu - VD:
# temperature >= 32
print(df[['event', 'day']][df['temperature'] >= 32])
print("===============")

# In các cột được chỉ định nhưng phải thỏa mãn điều kiện dữ liệu - VD:
# temperature == nhiệt độ cao nhất
print(df[['day', 'event']][df['temperature'] == df['temperature'].max()])
print("===============")

# Xem phạm vị index của DataFrame
print(df.index)
print("===============")

# Dùng 1 cột làm index của DataFrame - set_index(column) method -> return
# DataFrame mới, sử dụng đối số inplace=True (thay đổi ở DataFrame gốc
# VD: day
df.set_index('day', inplace=True)
print(df)
print("===============")

# Sử dụng cột được đặt làm index như index - df.loc[]
print(df.loc['1/1/2017'])
print("===============")

# Reset lại index
df.reset_index(inplace=True)
print(df)
print("===============")

# Sử dụng cột event làm index
df.set_index('event', inplace=True)
print(df)
print("===============")

# Nếu index trùng -> in ra tất cả các hàng có cùng index
print(df.loc['Snow'])



