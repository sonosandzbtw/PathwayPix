import streamlit as st
from PIL import Image

# === Page config ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === Custom sidebar styling ===
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
        .custom-link {
            color: white;
            text-decoration: none;
            font-weight: 500;
            display: block;
            margin-top: 0.5rem;
        }
        .custom-link:hover {
            color: #7FC8F8;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar content ===
if st.sidebar.button("🏠 PathwayPix Home"):
    st.session_state["pathway"] = ""

st.sidebar.markdown("#### Pathways")
pathway = st.sidebar.selectbox("Select a Pathway", [
    "",  # blank option for main page
    "1\ufe0f\u20e3 Glycolysis",
    "2\ufe0f\u20e3 Phosphate Dehydrogenation",
    "3\ufe0f\u20e3 Krebs Cycle",
    "4\ufe0f\u20e3 Electron Transport Chain"
])

st.sidebar.markdown("---")
st.sidebar.markdown('<a class="custom-link" href="/How_to_use" target="_self">How to Use</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a class="custom-link" href="/About" target="_self">About Developer</a>', unsafe_allow_html=True)

# === Main Page View ===
if pathway == "":
    st.title("Welcome to PathwayPix")
    st.markdown("""
    This is your molecular logic visualization tool.
    Choose a pathway from the left to begin.
    """)

elif pathway == "1\ufe0f\u20e3 Glycolysis":
    st.title("Glycolysis")
    try:
        img = Image.open("assets/glycolysis.png")
        st.image(img, use_container_width=True)
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
