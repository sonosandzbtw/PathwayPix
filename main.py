import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# === PAGE CONFIG ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === CUSTOM CSS ===
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #121212 !important;
        }

        [data-testid="stAppViewBlockContainer"] {
            background-color: #121212 !important;
            color: #EAEAEA !important;
            padding: 2rem 3rem;
        }

        [data-testid="stSidebar"] {
            background-color: #1E1E1E !important;
            padding-top: 1.5rem;
        }

        .custom-link {
            color: #EAEAEA !important;
            text-decoration: none !important;
            font-weight: 500;
            font-size: 16px;
            display: block;
            margin-bottom: 0.3rem;
        }

        .custom-link:hover {
            color: #A9D2FF !important;
        }

        h1, h2, h3 {
            color: #FFFFFF !important;
        }

        div[data-baseweb="select"] {
            background-color: #2C2C2C !important;
            color: #EAEAEA !important;
            border-radius: 8px;
            border: 1px solid #444;
        }

        .zoom-img {
            width: 100%;
            max-width: 800px;
            transition: transform 0.2s ease-in-out;
            cursor: zoom-in;
        }

        .zoom-img:hover {
            transform: scale(1.7);
            z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# === SIDEBAR ===
st.sidebar.markdown("<h2 class='custom-link'>🧬 <a href='/' style='text-decoration: none; color: inherit;'>PathwayPix</a></h2>", unsafe_allow_html=True)
st.sidebar.markdown('<a class="custom-link" href="/How_to_use" target="_self">🛠 How to Use</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a class="custom-link" href="/About" target="_self">👤 About Developer</a>', unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("#### Select a Pathway", unsafe_allow_html=True)

pathway = st.sidebar.selectbox("", [
    "Select...",
    "1️⃣ Glycolysis",
    "2️⃣ Phosphate Dehydrogenation",
    "3️⃣ Krebs Cycle",
    "4️⃣ Electron Transport Chain"
])

# === HELPER FUNCTION ===
def display_zoomable_image(image_path):
    try:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        zoom_html = f"""
        <div style="text-align:center;">
            <img class="zoom-img" src="data:image/png;base64,{img_base64}" />
        </div>
        """
        st.markdown(zoom_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ Please add '{image_path}' to the 'assets/' folder.")

# === PAGE CONTENT ===
if pathway == "Select...":
    st.markdown("<h1>🧬 Welcome to PathwayPix</h1>", unsafe_allow_html=True)
    st.markdown("""[... your welcome message content remains unchanged ...]""", unsafe_allow_html=True)

elif pathway == "1️⃣ Glycolysis":
    st.title("Glycolysis")
    display_zoomable_image("assets/glycolysis.png")

elif pathway == "2️⃣ Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "3️⃣ Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "4️⃣ Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("🚧 Module under construction.")
