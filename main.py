import streamlit as st
from PIL import Image

st.set_page_config(page_title="PathwayPix", layout="wide")

# === SIDEBAR ===
st.sidebar.markdown("## PathwayPix")
st.sidebar.markdown("#### Pathways")

# Clean selectbox for pathway selection — no icons, no bullets
pathway = st.sidebar.selectbox("Select a pathway", [
    "Glycolysis",
    "Phosphate Dehydrogenation",
    "Krebs Cycle",
    "Electron Transport Chain"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("[How to Use](pages/How_to_use.py)")
st.sidebar.markdown("[About Developer](pages/About.py)")

# === MAIN CONTENT ===
if pathway == "Glycolysis":
    st.title("Glycolysis Explorer")
    st.markdown("Explore the steps, enzymes, and energy flow of glycolysis.")

    try:
        img = Image.open("assets/glycolysis.png")
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Pathway image not found. Please place `glycolysis.png` inside the `assets/` folder.")

elif pathway == "Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("🚧 This module is under construction.")

elif pathway == "Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("🚧 This module is under construction.")

elif pathway == "Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("🚧 This module is under construction.")
