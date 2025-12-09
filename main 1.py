import pandas as pd
import plotly.express as px
 
 
 
df= pd.read_csv("/Users/Arvin/OneDrive/Desktop/data simu/data-simu/amazon_product_dataset.csv")
#PILIMINARY EXPLORATORY DATA ANALYSIS
#print(df.head(15))  
#we get the set of first 15*15 (as per the value given in our scenerio 15)rows & columns of the df
#print(df.info())
#data types of the df
#print(df.describe())  
# stat values of df  
print(df.isnull().sum())
# the sum of null value ONLY in the case colums of df
print(df.duplicated().sum())
#the sum of duplicates of df
 
#EXPLORARY DATA ANALYSIS
print(df.drop_duplicates())
#drops the partical row(s) which are repeated
 
#S1NORMALIZATION
df['Date']=df['Date'].astype(str).str.replace(':','-')
#print(df['Date'])
 
#S2CONVERSION
#conclusion:conversion not needed the df is pretty clean
 
#S3HANDELING MISSING DATA VALUES
df=df.fillna('cutie')
df.to_csv('dummy.csv',index=False)
 
#s4CLEANING CATEGORIAL COLUMS
df['State']=df['State'].str.strip()
df['State']=df['State'].str.title()
 
#S5 outliner detection & removal
Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['Quantity'] >= lower) & (df['Quantity'] <= upper)]
#print(df)
 
#S6 create own business columns
df['Quantity'] = df['Quantity'].apply(lambda x: 1 if x > 0.3 else 0)
#print(df['Quantity'])
#therefore we conclude that all the products have decent amount of sales
 
#df['region']=df['state'].apply(lambda x: 'west' if x in ['california','oregon','washington'] else ('midwest' if x in['illinois','indiana','iowa','kanasas','michiga'] else( 'south' if x in ['alabama','arkansas','florida','georgia'] else 'northeast')))
 
 
df['Stat e'] = df['State'].str.strip().str.title()
 
#FAILED TO CREATE A NEW COLUMN BASED ON REGION
#f["region"] = df["State"].map(region_map)
#rint(df['region_map'])
 
#TOP BOTTOM ANALYSIS
top_states = df.groupby('State')['Total_Sales_INR'].sum().sort_values(ascending=False).head()
fig = px.bar(top_states, x=top_states.index, y=top_states.values, title='Top 10 states by Sales')
fig.show()
#onclusion: skkim has the highest sales amongest other states
#disha has least sales comparitively to other states
#e observed that states with larger populations tend to have higher sales figures.
##te impact of seasonal trend on sales is significat,as certain months show higher sales.
 
 
#FAILED TO DO SEGMENT ANALYSIS
# df = df.groupby('Product_Category')['Quantity'].sum().reset_index()
# fig = px.bar(df, x='Product_Category', y='Quantity', title='Product_CategorybyQuantity')
# fig.show()
 
 
#time series analysis
#df = df.groupby(['Date'])['Total_Sales_INR'].sum().reset_index()
#fig = px.line(df, x = 'Date', y='Total_Sales_INR', title='Monthly Total_Sales_INRTrend by Date')
#fig.show()
#conclusion: (26-5-2025) we have a peak in sales on this date
#in the month of april(2-4-2025) we have a the least amt of sales taken place
# the avg sales per month is between 2.5M to 3M INR
 
# since the data is insufficient we can't frame a conculsion on profitability insights
 
 
#PROVIDED DATASET IS INSEFICIENT FOR MORE ACCURATE ANALYSIS
 
df['Date'] = pd.to_datetime(df['Date'],format='mixed',errors='coerce',dayfirst=True)
df['month']=df['Date'].dt.month.astype(str)
# print(df['month'])
# print(df)
 
#LINE CHART for daily revenue(1)
df_monthly = df.groupby('month')['Total_Sales_INR'].sum().reset_index()
df_monthly['month'] = df_monthly['month'].astype(int)
df_monthly = df_monthly.sort_values('month')
fig = px.line(df_monthly, x="month", y="Total_Sales_INR",
              title='Monthly Revenue Trend',
              markers=True,
              labels={'Total_Sales_INR': 'Revenue (INR)', 'month': 'Month'})
fig.update_layout(hovermode='x unified', height=600)
fig.show()
 
#LINE CHART for daily revenue(2)
df_monthly = df.groupby('month')['Unit_Price_INR'].sum().reset_index()
df_monthly['month'] = df_monthly['month'].astype(int)
df_monthly = df_monthly.sort_values('month')
fig = px.line(df_monthly, x="month", y="Unit_Price_INR",
              title='Monthly Revenue Trend',
              markers=True,
              labels={'Unit_Price_INR': 'Revenue (INR)', 'month': 'Month'})
fig.update_layout(hovermode='x unified', height=600)
fig.show()
#PIE CHART(1)
#fig = px.pie(df, values="Quantity", names="Product_Name", title="Quantity with respective to Category")
#fig.show()
 
#PIE CHART(2)
#fig = px.pie(df, values="Review_Rating", names="State", title="Review rating by customers")
#fig.show()
 
#PIE chat(3)  
#fig = px.pie(df, values="Review_Rating", names="Product_Name", title="rating of the products")
#fig.show()
#df['Date'] = pd.to_datetime(df['Date'],format='mixed',errors='coerce',dayfirst=True)
#df['month']=df['Date'].dt.month
#fig = px.line(df, x="Date", y="Total_Sales_INR", title='Daily revenue', markers=False)
#fig.show()
df.to_csv("amazon_product_dataset.csv", index=False)
 