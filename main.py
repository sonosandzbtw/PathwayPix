import streamlit as st
from PIL import Image

# === Page config ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === Sidebar Styling ===
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1B264F;
        }
        .css-1v3fvcr, .css-10trblm, .css-qcqlej {
            list-style-type: none;
            padding-left: 0;
        }
        .css-qcqlej { display: none; }
    </style>
""", unsafe_allow_html=True)

# === Sidebar ===
st.sidebar.markdown("## PathwayPix")
st.sidebar.markdown("#### Pathways")

# Use selectbox to avoid bullet-style radio buttons
pathway = st.sidebar.selectbox("Select a Pathway", [
    "1\ufe0f\u20e3 Glycolysis",
    "2\ufe0f\u20e3 Phosphate Dehydrogenation",
    "3\ufe0f\u20e3 Krebs Cycle",
    "4\ufe0f\u20e3 Electron Transport Chain"
])

st.sidebar.markdown("---")
st.sidebar.markdown("[How to Use](pages/How_to_use.py)")
st.sidebar.markdown("[About Developer](pages/About.py)")

# === Main Page View ===
st.title("Welcome to PathwayPix")
st.markdown("""
This is your molecular logic visualization tool.
Choose a pathway from the left to begin.
""")

# === Pathway Views ===
if pathway == "1\ufe0f\u20e3 Glycolysis":
    st.title("Glycolysis")
    try:
        img = Image.open("assets/glycolysis.png")
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning("\u26a0\ufe0f Please add 'glycolysis.png' to the 'assets/' folder.")

elif pathway == "2\ufe0f\u20e3 Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("\ud83d\udea7 Module under construction.")

elif pathway == "3\ufe0f\u20e3 Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("\ud83d\udea7 Module under construction.")

elif pathway == "4\ufe0f\u20e3 Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("\ud83d\udea7 Module under construction.")
