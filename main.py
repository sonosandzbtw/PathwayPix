import streamlit as st
from PIL import Image

st.set_page_config(page_title="PathwayPix", layout="wide")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Pathway Viewer", "How to Use", "About Developer"])

if page == "Pathway Viewer":
    st.title("🧬 PathwayPix")
    st.write("Visualizing glycolysis with logic, color, and clarity.")
    img = Image.open("assets/glycolysis.png")
    st.image(img, use_column_width=True)
    # Add toggles here (ATP, NADH, regulation, etc.)

elif page == "How to Use":
    with open("docs/how_to_use.md", "r") as f:
        st.markdown(f.read())

elif page == "About Developer":
    with open("docs/about.md", "r") as f:
        st.markdown(f.read())
