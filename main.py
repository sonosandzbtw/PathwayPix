import streamlit as st
from PIL import Image

# === Page config ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === Custom styling ===
st.markdown("""
    <style>
        :root {
            --sidebar-bg-color: #1E2A47;
            --link-color: #E3E9F0;
            --link-hover-color: #7FC8F8;
        }

        [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg-color) !important;
        }

        [data-testid="stAppViewContainer"] {
            background-color: #020030 !important;
        }

        [data-testid="stAppViewBlockContainer"] {
            padding: 2rem 3rem;
            background-color: #020030 !important;
            color: #E3E9F0;
        }

        .custom-link {
            color: #E3E9F0 !important;
            text-decoration: none !important;
            font-weight: 500;
            font-size: 16px;
            margin: 0.5rem 0;
            display: inline-block;
            transition: color 0.2s ease;
        }

        .custom-link:hover {
            color: #A0D7F7 !important;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar content ===
st.sidebar.markdown("## 🧬 PathwayPix")

st.sidebar.markdown("#### Pathways")

pathway = st.sidebar.selectbox("Select a Pathway", [
    "Select...",
    "1️⃣ Glycolysis",
    "2️⃣ Phosphate Dehydrogenation",
    "3️⃣ Krebs Cycle",
    "4️⃣ Electron Transport Chain"
])

st.sidebar.markdown("---")
st.sidebar.markdown('<a class="custom-link" href="/How_to_use" target="_self">🛠 How to Use</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a class="custom-link" href="/About" target="_self">👤 About Developer</a>', unsafe_allow_html=True)

# === Main content ===
if pathway == "Select...":
    st.title("Welcome to PathwayPix")
    st.markdown("""
    This is your molecular logic visualization tool.
    Choose a pathway from the left to begin.
    """)

elif pathway == "1️⃣ Glycolysis":
    st.title("Glycolysis")
    try:
        img = Image.open("assets/glycolysis.png")
        st.image(img, use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Please add 'glycolysis.png' to the 'assets/' folder.")

elif pathway == "2️⃣ Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "3️⃣ Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "4️⃣ Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("🚧 Module under construction.")

