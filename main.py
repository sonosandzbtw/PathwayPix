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
    I want students to explore what’s happening, understand how hormones like insulin change the flow of metabolism, and zoom in to see the organic transformations behind each reaction.
    </p>

    <p style='font-size:17px; color:#EAEAEA;'>
    If you’ve ever felt like biochemistry was just a wall of facts, I built this to show you that it’s actually a beautiful, logical dance of electrons. 
    Let carbon do its thing. You’ll see.
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

    <p style='font-size:17px; color:#EAEAEA;'>
    When you grasp the “why,” the “what” becomes obvious.
    </p>

    <hr style='margin-top:40px; margin-bottom:40px; border-color:#444;'>

    <h2 style='color:#FFFFFF;'>🧠 Design Philosophy</h2>

    <h3 style='color:#F5F5F5;'>1. Every isomerization happens for a reason.</h3>
    <p style='font-size:17px; color:#EAEAEA;'>
    Molecules don’t randomly shift shapes. Whether it’s a carbonyl repositioning, a ring opening, or a sugar flipping forms — there’s always a strategy. 
    Each isomerization supports a specific goal:
    </p>

    <ul style='font-size:17px; color:#EAEAEA;'>
        <li>Preparing a molecule for cleavage</li>
        <li>Enabling a redox reaction</li>
        <li>Creating symmetry for branching</li>
    </ul>

    <h3 style='color:#F5F5F5;'>2. Regulatory steps aren’t trivia — they’re turning points.</h3>
    <p style='font-size:17px; color:#EAEAEA;'>
    Control points in metabolism aren’t just facts to memorize. They’re where the story shifts.
    </p>

    <ul style='font-size:17px; color:#EAEAEA;'>
        <li>Why is regulation here?</li>
        <li>What changes before and after this step?</li>
        <li>What is the cell trying to achieve?</li>
    </ul>
    """, unsafe_allow_html=True)

# === GLYCOLYSIS PAGE ===
elif pathway == "1️⃣ Glycolysis":
    st.title("Glycolysis")

    col1, col2 = st.columns([2, 2])

    with col1:
        display_zoomable_image("assets/glycolysis.png")

    with col2:
        st.markdown("### 🔍 Explore Steps")
        step = st.radio("Select Step", [f"Step {i}" for i in range(1, 11)], horizontal=True)
        st.write(f"Details for {step} will appear here.")
        # You can customize this part further for each step logic
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
            # Add more logic as desired

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
