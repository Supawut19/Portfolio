# covert order date and shipdate
import pandas as pd

df = pd.read_csv('work/sample-store.csv')

df.head()

df['convertdate'] = pd.to_datetime(df['Order Date'])

df['convertdate'].head()

df['convertdate'] = df['convertdate'].dt.strftime('%Y/%m/%d')

df['Order Date'] = df['convertdate']

df['Order Date'].head()

df['convertshipdate'] = pd.to_datetime(df['Ship Date'])
df['convertshipdate'] = df['convertshipdate'].dt.strftime('%Y/%m/%d')
df['Ship Date'] = df['convertshipdate']
df['Ship Date'].head()

del df['convertdate']
del df['convertshipdate']

# count nan in postal code column
df['Postal Code'].isna().sum()

# filter rows with missing value
df[df['Postal Code'].isna()]

# how many colums, rows in this dataset
df.shape

# is there any missing value?, if there is, which column? how many nan values?
df.isna().sum()

# your friend ask for 'California' data, filter it and export csv for him
df_california = df.query('State == "California"')

df_california.to_csv("work/california_data.csv")

# your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
df_2017 = df[pd.to_datetime(df['Order Date']).dt.to_period('Y') == '2017']

df_california_texas = df_2017.query('State == "California" | State == "Texas"')

df_california_texas.to_csv("work/california_texas_data.csv")

# how much total sales, average sales, and standard deviation of sales your company make in 2017
df_2017['Sales'].agg(['sum', 'mean', 'std'])

# which Segment has the highest profit in 2018
df_2018 = df[pd.to_datetime(df['Order Date']).dt.to_period('Y') == '2018']

df_2018.groupby(['Segment'])['Profit'].sum() # highest profit is Consumer

# which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df['Order Date'] = pd.to_datetime(df['Order Date'])

df_m4_m12 = df[(df['Order Date'] > '2019-04-15') & (df['Order Date'] < '2019-12-31')]

result = df_m4_m12.groupby(['State'])['Sales'].sum().reset_index()

# top 5 least total sales 
result.sort_values(by=['Sales'])[0:5]

# what is the proportion of total sales (%) in West + Central in 2019 e.g. 25%
df_2019 = df[df['Order Date'].dt.to_period('Y') == '2019']

df_west_cen_2019 = df_2019.query('Region == "West" | Region == "Central"')

result_2019 = df_west_cen_2019.groupby(['Region'])['Sales'].sum()
central = result_2019[0]
west = result_2019[1]

sales2019_all = df_2019['Sales'].sum()

percent = ((central + west)/ sales2019_all) * 100

print(percent)

# find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
df_1920 = df[(df['Order Date'] >= '2019') & (df['Order Date'] <= '2020')]
product_s = df_1920.groupby(['Product Name', 'Quantity'])['Sales'].sum().reset_index()
product_s.sort_values(['Sales'], ascending = False)[0:10]


