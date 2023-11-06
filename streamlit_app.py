import streamlit as st

# Sample product data (you would typically use a database)
products = [
    {"name": "T-shirt", "price": 20.0, "image": "tshirt.jpg"},
    {"name": "Dress", "price": 40.0, "image": "dress.jpg"},
    # Add more products here
]

st.title("Clothing Design Store")

for product in products:
    st.write(f"**{product['name']}**")
    st.image(product['image'])
    st.write(f"Price: ${product['price']}")

# Add more Streamlit components as needed

