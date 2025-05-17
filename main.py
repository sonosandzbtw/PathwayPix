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
            background-color: #020125 !important;
        }

        [data-testid="stAppViewBlockContainer"] {
            padding: 2rem 3rem;
            background-color: #020125 !important;
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
st.sidebar.markdown('<a class="custom-link" href="/" target="_self">🧬 PathwayPix</a>', unsafe_allow_html=True)

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
    st.title("🧬 Welcome to PathwayPix")
    st.markdown("""
    **Biochemistry is often taught as a subject full of pathways to memorize, enzymes to name, and cofactors to list — but to me, it’s never felt like that.**  
    As someone deeply obsessed with organic chemistry, I realized something simple:  
    **Biochemistry is just Orgo in motion** — carbon doing what carbon does best: reacting with purpose.

    Once I started looking at pathways through that lens, everything clicked.  
    There’s no need to memorize when you understand the logic behind each molecular move.

    But textbooks rarely explain it that way.  
    They show you **what** happens, but not **why** — the mechanisms, the regulation, the energy logic — it's all flattened into diagrams and labels.

    ---

    ### Why I Built This Webapp

    To make biochemistry interactive, visual, and actually **fun** — for everyone.

    I want students to:
    - **See** what’s happening,
    - **Explore** how hormones like insulin shift metabolic flow,
    - **Zoom in** to understand the organic transformations behind each step.

    If you’ve ever felt like biochem was just a wall of facts —  
    I built this to show you that it’s actually a **beautiful, logical dance of electrons**.

    > Let carbon do its thing.  
    > You’ll see.

    ---

    # 🎯 Design Philosophy Behind This Webapp

    ## 1. Every Isomerization Happens for a Reason

    Molecules don’t shift forms randomly — they adapt with purpose.  
    Whether it’s moving a carbonyl, rearranging ring structures, or converting sugar forms, each isomerization serves a strategic role:

    - To prepare for a specific cleavage  
    - To enable a redox reaction  
    - To create symmetry or enable branching  

    We don’t memorize these — we understand them.  
    This app shows why these changes aren't just chemical — they’re **logical**.

    ---

    ## 2. Regulatory Steps Turn Pathways Into Stories

    Every pathway has checkpoints — not because cells love drama,  
    but because life needs control.

    Instead of memorizing “Step 3 is regulated by F2,6-BP,” you’ll start asking:
    - Why here?  
    - Why not earlier or later?  
    - What’s the biochemical pressure at this point?

    Once you understand the logic — like how **PFK-1 commits the cell to full glycolysis** — memorization fades. A **cause-effect narrative** emerges.  
    Regulation becomes story.

    ---

    # 🧠 What This Means for You

    - You'll see structural changes as **purposeful**, not arbitrary  
    - You'll understand control points as **strategic**, not trivia  
    - You'll stop treating biochem like a **high-stakes flashcard game**,  
      and start seeing it like a **well-engineered molecular system**

    ---

    ### ✴️ Welcome to PathwayPix.  
    A new lens for the logic of life.
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

