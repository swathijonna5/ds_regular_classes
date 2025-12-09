import streamlit as st
import pandas as pd 
import plotly.express as px

df= pd.read_csv("/Users/swath/OneDrive/Desktop/ds_regular_classes.py/amazon_product_dataset.csv")

st.title('Charts & Insights based on amazon product dataset')

def get_top_states(df):
  top_states = df.groupby('State')['Total_Sales_INR'].sum().sort_values(ascending=True).head(10)
  fig = px.bar(top_states, x=top_states.index, y=top_states.values, title='Top 10 states by Sales')
  return fig

def get_top_states(df):
  top_states = df.groupby('State')['Total_Sales_INR'].sum().sort_values(ascending=False).head(10)
  fig = px.bar(top_states, x=top_states.index, y=top_states.values, title='Top 10 states by Sales')
  return fig

  #SEGMENT ANALYSIS
def get_product_category(df):
  df = df.groupby('Product_Category')['Quantity'].sum().reset_index().head(5)
  fig = px.bar(df, x='Product_Category', y='Quantity', title='Product_Category by Quantity')
  return fig

#time series analysis
def get_total_sales(df):
  df = df.groupby(['Date'])['Total_Sales_INR'].sum().reset_index()
  fig = px.line(df, x = 'Date', y='Total_Sales_INR', title='Monthly Total_Sales_INRTrend by Date')
  return fig

def get_product_sales_by_names(df):
  fig = px.bar(df,x='Product_Name',y='Total_Sales_INR',title="product sales by names")
  return fig


def get_quantity_share_by_category(df):
  fig = px.pie(df, values="Quantity", names="Product_Category", title="Quantity share by Category")
  return fig

def get_quantity_share_by_Name(df):
  fig = px.pie(df, values="Quantity", names="Product_Name", title="Quantity share by Name")
  return fig

def get_review_rating(df):
  fig = px.pie(df, values="Review_Rating", names="Product_Name", title="Review rating of the products")
  return fig

def get_quantity_ordered_by_delivery(df):
  fig = px.pie(df, values="Quantity", names="Delivery_Status", title="Quantity ordered by delivery")
  return fig

def get_unit_price(df):
  fig = px.scatter(df, x="Unit_Price_INR", y="Quantity", size='Total_Sales_INR', title="Unit_Price_INR vs Quantity")
  return fig

def get_most_sold_products(df):
  fig = px.bar(df, x="Product_Name", y="Quantity", title="the most sold product")
  return fig


def get_total_orders(df):
  fig = px.box(df, x='State', y='Total_Sales_INR', title='Order Totals by State')
  return fig

def get_total_amount_distributiom(df):
  fig = px.histogram(df, x="Total_Sales_INR", nbins = 6, title="Order Total Amount Distribution")
  return fig

st.plotly_chart(get_top_states(df))
st.write('''  Insights:\n
              Observation: Odisha has the lowest sales compared to top 10 states.\n
              Reason:reason behind the lowest sales can be low urbanization and limited awareness in that particular state .\n
              Impact:Low urbanization can limit economic growth, access to services, and technological advancements, while contributing to social isolation and environmental challenges.\n
              Recommendation:more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_product_category(df))
st.write(''' Insights:\n
              Observation: Home&Kitchen products are less in Category wise.\n
              Reason:reason of low quantity sale can be poor product quality , high prices , weak marketing.\n
              Impact:this low sales volume can include reduced profits, excess inventory, lower brand visibility, and difficulty sustaining business growth.\n
              Recommendation:more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_total_sales(df))
# st.write(''' Insights:\n
              # Observation: Vaccum cleaner product is less sold amongst all products.\n
              # Reason:reason of less selling can be less demand of the product and not a frequent purchased item.\n
              # Impact:impact can be reduced revenue and profit.
              # Recommendation:this product can be taken away from the products section or can be put less quantity of stock.''')

st.plotly_chart(get_product_sales_by_names(df))
st.write(''' Insights:\n
              Observation: Home&Kitchen products are less in Quantity wise.\n
              Reason:reason of low quantity sale can be poor product quality , high prices , weak marketing.\n
              Impact:this low sales volume can include reduced profits, excess inventory, lower brand visibility, and difficulty sustaining business growth.\n
              Recommendation:more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_quantity_share_by_category(df))
st.write(''' Insights:\n
             Observation: Vaccum cleaner product is less quantity sold amongst all products.\n
             Reason:reason of less selling can be less demand of the product and not a frequent purchased item.\n
             Impact:impact can be reduced revenue and profit.\n
             Recommendation:this product can be taken away from the products section or can be put less quantity of stock.\n''')

st.plotly_chart(get_quantity_share_by_Name(df))
st.write(''' Insights:\n
              Observation: Vaccum cleaner product is less sold amongst all products.\n
              Reason: reason for low quantity sale can be poor product quality , high prices , weak marketing.\n
              Impact: this low sales volume can include reduced profits, excess inventory, lower brand visibility, and difficulty sustaining business growth.\n
              Recommendation: more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_review_rating(df))
st.write(''' Insights:\n
              Observation: Hair drier is the product that has less review rating.\n
              Reason: Reason for less reviews can be poor quality of the product or highest price less time warrenty.\n
              Impact: Impact can be on the products revenue and total amount of sales.\n
              Recommendation: Recommendation is the good quality product can be replaced with the poor quality products and can be put discounts for that product or price can be reduced according to MRP.\n''')

st.plotly_chart(get_quantity_ordered_by_delivery(df))
st.write(''' Insights:\n
              Observation: Returned products are almost reachable as same as delivered products.\n
              Reason: Reason for this can be wrong products delivery and delivered item and recieved item are not same or poor quality of the product.\n
              Impact: This can show more impact on their business because of wrong deliveries , less review ratings and bad delivery service.\n
              Recommendation: Must improve delivery services on time to time .\n''')

st.plotly_chart(get_unit_price(df))
#st.write(''' Insights:\n
              # Observation: Home&Kitchen products are less in Quantity.\n
              # Reason:reason for low quantity sale can be poor product quality , high prices , weak marketing.\n
              # Impact:this low sales volume can include reduced profits, excess inventory, lower brand visibility, and difficulty sustaining business growth.\n
              # Recommendation:more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_most_sold_products(df))
st.write(''' Insights:\n
              Observation: Perfume is the most sold product amongst all.\n
              Reason:reason for most sold product can be of more discount & offers and more trending brand.\n
              Impact:there is no impact and get more profits.\n
              Recommendation:more stock can be purchase of that product(perfume).\n''')

st.plotly_chart(get_total_orders(df))
# st.write(''' Insights:\n
              # Observation: Home&Kitchen products are less in Quantity.\n
              # Reason:reason for low quantity sale can be poor product quality , high prices , weak marketing.\n
              # Impact:this low sales volume can include reduced profits, excess inventory, lower brand visibility, and difficulty sustaining business growth.\n
              # Recommendation:more awareness about sales and promotions can lead to rise of the sales.\n''')

st.plotly_chart(get_total_amount_distributiom(df))
st.write(''' Insights:\n
              Observation: count between 200k to 250k are having less sales count.\n
              Reason:reason for less sales can be high price.\n
              Impact:this can be show impact on total revenue.\n
              Recommendation:increasing and putting disounts wherever needed and increasing more brand products.\n''')