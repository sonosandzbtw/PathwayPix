import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from io import BytesIO
import base64

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
    </style>
""", unsafe_allow_html=True)

# === HELPER FUNCTION FOR ZOOM ===
def display_interactive_zoom(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    components.html(f"""
        <div id="zoom-container" style="width: 100%; height: 800px; overflow: auto; border: 1px solid #444;">
            <img id="zoom-img"
                src="data:image/png;base64,{img_base64}"
                style="width: 1000px; height: auto; transition: width 0.3s ease;" />
        </div>

        <script>
            setTimeout(() => {{
                const img = document.getElementById("zoom-img");
                let zoomed = false;

                img.addEventListener("click", () => {{
                    zoomed = !zoomed;
                    img.style.width = zoomed ? "2500px" : "1000px";
                }});
            }}, 100);
        </script>
    """, height=850)

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

# === MAIN PAGE ===
if pathway == "Select...":
    st.markdown("<h1>🧬 Welcome to PathwayPix</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:17px; color:#EAEAEA;'>
    <strong>Biochemistry is often taught as a subject full of pathways to memorize, enzymes to name, and cofactors to list.</strong><br>
    But to me, it never felt like that.
    </p>
    <p style='font-size:17px; color:#EAEAEA;'>
    As someone deeply obsessed with organic chemistry, I realized that biochemistry is just <strong>Orgo in motion</strong> — carbon doing what carbon does best: reacting with purpose. 
    Once I started looking at pathways through that lens, everything clicked. There’s no need to memorize when you understand the logic behind each molecular move.
    </p>
    <p style='font-size:17px; color:#EAEAEA;'>
    Textbooks rarely explain it this way. They show you what happens, but not why. The mechanisms, the regulation, the energy logic — it’s all flattened into diagrams and labels.
    </p>
    <p style='font-size:17px; color:#EAEAEA;'>
    That’s why I built PathwayPix: to make biochemistry interactive, visual, and actually fun.
    </p>

    <hr style='margin-top:40px; margin-bottom:40px; border-color:#444;'>

    <h2 style='color:#FFFFFF;'>💡 Why I Built This Webapp</h2>
    <p style='font-size:17px; color:#EAEAEA;'>
    PathwayPix isn't about memorizing pathways. It's about understanding them: how they work, why they change, and where control happens.
    </p>
    <ul style='font-size:17px; color:#EAEAEA;'>
        <li><strong>See</strong> what’s happening in each step</li>
        <li><strong>Understand</strong> how small molecular shifts serve strategic purposes</li>
        <li><strong>Follow</strong> the biochemical logic, not just the names</li>
    </ul>

    <hr style='margin-top:40px; margin-bottom:40px; border-color:#444;'>

    <h2 style='color:#FFFFFF;'>🧠 Design Philosophy</h2>

    <h3 style='color:#F5F5F5;'>1. Every isomerization happens for a reason.</h3>
    <p style='font-size:17px; color:#EAEAEA;'>
    Molecules don’t randomly shift shapes. Every change has a purpose — to enable the next step in the pathway.
    </p>
    <ul style='font-size:17px; color:#EAEAEA;'>
        <li>Preparing for cleavage</li>
        <li>Allowing redox changes</li>
        <li>Creating symmetry</li>
    </ul>

    <h3 style='color:#F5F5F5;'>2. Regulatory steps aren’t trivia — they’re turning points.</h3>
    <p style='font-size:17px; color:#EAEAEA;'>
    Don’t memorize regulation. Understand its role.
    </p>
    <ul style='font-size:17px; color:#EAEAEA;'>
        <li>Why regulate here?</li>
        <li>What’s the logic behind this control point?</li>
        <li>What would happen without it?</li>
    </ul>
    """, unsafe_allow_html=True)

# === GLYCOLYSIS PAGE ===
elif pathway == "1️⃣ Glycolysis":
    st.title("Glycolysis")
    col1, col2 = st.columns([2, 2])

    with col1:
        display_interactive_zoom("assets/glycolysis.png")

    with col2:
        st.markdown("### 🔍 Explore Steps")
        step = st.radio("Select Step", [f"Step {i}" for i in range(1, 11)], horizontal=True)
        st.write(f"Details for {step} will appear here.")

        if step == "Step 3":
            st.success("Step 3 is catalyzed by **PFK-1**, the key regulatory step committed to glycolysis.")

        st.markdown("### 🧪 Regulation")
        factors = st.multiselect("Select Conditions", ["Insulin ↑", "Glucagon ↑", "ATP ↑", "AMP ↑", "Citrate ↑", "ADP ↑"])
        if factors:
            st.markdown("#### 🧠 Logical Impact:")
            if "Insulin ↑" in factors:
                st.info("Insulin upregulates PFK-1 and increases glycolytic flux.")
            if "Glucagon ↑" in factors:
                st.warning("Glucagon activates FBPase-2 (via cAMP), lowering F2,6BP and inhibiting glycolysis.")
            if "ATP ↑" in factors:
                st.error("High ATP inhibits PFK-1 allosterically. Cell energy is sufficient.")

# === PLACEHOLDERS FOR OTHER MODULES ===
elif pathway == "2️⃣ Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "3️⃣ Krebs Cycle":
    st.title("Krebs Cycle (Coming Soon)")
    st.info("🚧 Module under construction.")

elif pathway == "4️⃣ Electron Transport Chain":
    st.title("Electron Transport Chain (Coming Soon)")
    st.info("🚧 Module under construction.")

