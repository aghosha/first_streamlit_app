import streamlit
import pandas

streamlit.title('My first Streamlit Code')

streamlit.header('Root1')
streamlit.text('node1')
streamlit.text('node2')

streamlit.header('Root2')
streamlit.text('node1')
streamlit.text('node2')
streamlit.text('node3')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc(fruits_selected)
streamlit.dataframe(fruits_to_show)
