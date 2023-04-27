import streamlit 
import pandas 
streamlit.title ( ' Healthy Dinner  ')


streamlit.header('Breakfast Menu')
streamlit.text('  🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('  🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('  🐔 Hard-Boiled Free-Range Egg')
streamlit.text('  🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

# Display the table on the page.

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon"+ "kiwi")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
