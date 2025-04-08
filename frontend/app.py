import streamlit as st
from components.api_caller import fetch_api
from config.settings import API_BASE_URL

st.title("FastAPI UUID & Cat API Explorer")
st.write("Use the buttons below to test the API endpoints. Make sure the FastAPI server is running at http://localhost:8000!")

# Handle UUID API request
if st.button("Get UUID"):
    with st.spinner("Fetching UUID..."):
        result, exec_time, error = fetch_api("/uuid")
        if error:
            st.error(f"Error: {error}")
        else:
            st.subheader("Response")
            st.json(result)
            st.write(f"Execution Time: {exec_time:.3f} seconds")

# Handle Async UUID API request (with intentional delay)
if st.button("Get Async UUID (3s delay)"):
    with st.spinner("Fetching Async UUID (takes at least 3 seconds)..."):
        result, exec_time, error = fetch_api("/async-uuid")
        if error:
            st.error(f"Error: {error}")
        else:
            st.subheader("Response")
            st.json(result)
            st.write(f"Execution Time: {exec_time:.3f} seconds")

# Handle Random Cat Image API request
if st.button("Get Random Cat Image"):
    with st.spinner("Fetching cat image..."):
        # Clear previous image to avoid overlapping renders
        placeholder = st.empty()
        result, exec_time, error = fetch_api("/cat")
        if error:
            st.error(f"Error: {error}")
        else:
            with placeholder.container():
                st.subheader("Response")
                st.json(result)
                st.write(f"Execution Time: {exec_time:.3f} seconds")
                st.subheader("Cat Image")
                cat_url = result["cat_image_url"]
                st.image(cat_url, caption="Random cat image", use_container_width=True)
