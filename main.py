import streamlit as st
from PIL import Image

# === Page config ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === Custom sidebar styling ===
st.markdown("""
    <style>
        /* Sidebar background color */
        [data-testid="stSidebar"] {
            background-color: #1B264F;
        }

        /* Sidebar text */
        .sidebar-content {
            color: white;
        }

        /* Remove default bullets from radio/checkbox */
        .css-10trblm, .css-1v3fvcr {
            list-style: none;
        }

        /* Sidebar headers */
        .sidebar .block-container {
            padding-top: 1rem;
        }

        .css-1d391kg {
            color: white;
        }

        /* Remove navigation heading text */
        .css-qcqlej {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar content ===
st.sidebar.markdown("## PathwayPix")
st.sidebar.markdown("#### Pathways")

pathway = st.sidebar.radio("", [
    "Glycolysis",
    "Phosphate Dehydrogenation",
    "Krebs Cycle",
    "Electron Transport Chain"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### How to Use")
st.sidebar.markdown("### About Developer")

# === Main content ===
if pathway == "Glycolysis":
    st.title("Glycolysis")
    st.markdown("Explore enzymes, regulation, and energy flow in the glycolysis pathway.")
    try:
        img = Image.open("assets/glycolysis.png")
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Please add `glycolysis.png` to the `assets/` folder.")

elif pathway == "Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("🚧 Module under construction.")
