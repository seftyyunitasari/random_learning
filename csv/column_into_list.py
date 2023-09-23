from pandas import *

# reading a csv file
data = read_csv("./company_sales_data.csv")

# converting column in the data into list
month = data["month_number"].tolist()

print(month)
