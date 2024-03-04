import streamlit as st

st.set_page_config(
    page_title="Main",
    page_icon="📄")
st.title("Exercise and Food Calorie Tracker")

# Check if 'user_data' is already in session state, if not initialize it
if 'user_data' not in st.session_state:
    st.session_state.user_data = {'age': None, 'weight': None, 'height': None}
col1, col2, col3 = st.columns(3)


with col1:
    age = st.number_input("Insert your age", value=st.session_state.user_data['age'], format="%.f", placeholder="Type a number...")
with col2:
    weight = st.number_input("How much do you weigh? (in Kg)", value=st.session_state.user_data['weight'], format="%.f", placeholder="Type a number...")
with col3: 
    height = st.number_input("How tall are you? (in Cm)", value=st.session_state.user_data['height'], format="%.f", placeholder="Type a number...")

# Update session state with the latest user input
st.session_state.user_data['age'] = age
st.session_state.user_data['weight'] = weight
st.session_state.user_data['height'] = height

# Display the user data
st.write("The current information is: ")
st.write(f"Age: {age} ")
st.write(f"Weight: {weight} ")
st.write(f"Height: {height} ")
