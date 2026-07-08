import pandas as pd

# Read CSV file - skiprows (để bỏ qua hàng) | header=n (hàng bắt đầu làm tiêu
# đề -> n bắt đầu từ 0) | nrows - đọc số hàng mong muốn | na_values - đưa các
# giá trị invalid -> NaN (sử dụng list hoặc dict)
df = pd.read_csv("data_file/stock_data.csv", header=1, na_values={
    'eps': ["not available", "n.a."],
    'revenue': ["not available", "n.a.", -1],
    'people': ["not available", "n.a."],
    'price': ["not available", "n.a.", -1]
})
print(df)
print("======================")

# TH: không có hàng tiêu đề | header=None (tiêu đề default từ 0)
# df = pd.read_csv("data_file/stock_data.csv", header=None, names=["tickers",
#                                                                  "eps",
#                                                                  "revenue",
#                                                                  "price",
#                                                                  "people"])

# Save new file CSV - index (Loại bỏ index hàng khi lưu)
df.to_csv("data_file/new_stocks_data.csv", index=False)
# Save new file CSV with columns specified
df.to_csv("data_file/new_stocks_data.csv", index=False, columns=['tickers',
                                                                 'eps'])
# Save new file CSV omit header
df.to_csv("data_file/new_stocks_data.csv", index=False, header=False)

# Với excel cần viết hàm xử lí giá trị không hợp lệ
def convert_people_cell(cell):
    if cell == 'n.a.':
        return None
    return cell

def convert_eps_cell(cell):
    if cell in ["not available", -1]:
        return None
    return cell



# Read Excel file to DataFrame - converters - xử lí giá trị ko hợp lệ
df_excel = pd.read_excel("data_file/stock_data.xlsx", "Sheet1", converters={
    'people': convert_people_cell,
    'eps': convert_eps_cell
})
print(df_excel)
print("======================")

# Save new file Excel
df_excel.to_excel("data_file/new_stock_data.xlsx", index=False,
                  sheet_name="stock")

# Lưu nhiều DataFrame vào 1 trang Excel nhưng ở các sheet khác nhau
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 75, 88],
    'pe': [30.13, 12.3, 2.5],
    'eps': [29.5, 4.53, 2.14]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017', '2/1/2018', '3/1/2019'],
    'temperature': [32, 34, 38],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('data_file/stock_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name='stocks', index=False)
    df_weather.to_excel(writer, sheet_name='weather', index=False)
