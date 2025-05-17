import streamlit as st
from PIL import Image

# === PAGE CONFIG ===
st.set_page_config(page_title="PathwayPix", layout="wide")

# === CUSTOM CSS ===
st.markdown("""
    <style>
        /* Main background */
        [data-testid="stAppViewContainer"] {
            background-color: #121212 !important;
        }

        [data-testid="stAppViewBlockContainer"] {
            background-color: #121212 !important;
            color: #EAEAEA !important;
            padding: 2rem 3rem;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #1E1E1E !important;
            padding-top: 1.5rem;
        }

        /* Link styling */
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

        /* Headers */
        h1, h2, h3 {
            color: #FFFFFF !important;
        }

        /* Selectbox */
        div[data-baseweb="select"] {
            background-color: #2C2C2C !important;
            color: #EAEAEA !important;
            border-radius: 8px;
            border: 1px solid #444;
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

# === MAIN PAGE LOGIC ===
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

    <p style='font-size:17px; color:#EAEAEA;'>
    This platform helps you:
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

    <p style='font-size:17px; color:#EAEAEA;'>
    You'll see how structure dictates strategy — and how elegant it becomes when you look at it through an organic chemistry lens.
    </p>

    <h3 style='color:#F5F5F5;'>2. Regulatory steps aren’t trivia — they’re turning points.</h3>
    <p style='font-size:17px; color:#EAEAEA;'>
    Control points in metabolism aren’t just facts to memorize. They’re where the story shifts.
    </p>

    <p style='font-size:17px; color:#EAEAEA;'>
    Rather than just labeling PFK-1 as “regulated,” we ask:
    </p>

    <ul style='font-size:17px; color:#EAEAEA;'>
        <li>Why is regulation here?</li>
        <li>What changes before and after this step?</li>
        <li>What is the cell trying to achieve?</li>
    </ul>

    <p style='font-size:17px; color:#EAEAEA;'>
    When you understand regulation as narrative pressure — not just static control — the logic comes alive.
    </p>
    """, unsafe_allow_html=True)

# === PATHWAY LOGIC ===
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
