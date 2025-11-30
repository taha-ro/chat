import streamlit as st

# Set default page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to go to another page
def go_to_done():
    st.session_state.page = "done"

# Page content
if st.session_state.page == "home":
    st.write("This is the home page")
    if st.button("Go to Done"):
        go_to_done()

elif st.session_state.page == "done":
    st.write("✅ Done!")
    if st.button("Back to Home"):
        st.session_state.page = "home"
