import streamlit as st
from PIL import Image

# === Page config ===
st.set_page_config(page_title="PathwayPix", layout="wide")
st.markdown("""
    <style>
        :root {
            --main-bg-color: #121212;
            --sidebar-bg-color: #1E1E1E;
            --text-color: #EAEAEA;
            --accent-color: #9F7AEA;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--main-bg-color) !important;
            color: var(--text-color) !important;
        }

        [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg-color) !important;
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            border-right: 1px solid #333;
        }

        [data-testid="stSidebar"] .css-1v0mbdj {
            padding: 0 !important;
        }

        h1, h2, h3, h4, h5 {
            color: var(--text-color) !important;
        }

        /* Selectbox customization */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #1E1E1E !important;
            color: #EAEAEA !important;
            border: 1px solid #444 !important;
            border-radius: 8px;
            padding: 0.5rem;
        }

        .css-1kyxreq {
            color: var(--text-color) !important;
        }

        .custom-link {
            color: var(--text-color) !important;
            font-weight: 500;
            text-decoration: none;
            display: block;
            margin-bottom: 1rem;
            padding: 0.5rem 0.75rem;
            border-radius: 8px;
            background-color: transparent;
            transition: all 0.2s ease-in-out;
        }

        .custom-link:hover {
            background-color: #292929;
            color: var(--accent-color) !important;
        }
    </style>
""", unsafe_allow_html=True)

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
st.sidebar.markdown("<h2 style='color:#EAEAEA;'>📌 PathwayPix</h2>", unsafe_allow_html=True)

st.sidebar.markdown('<a class="custom-link" href="/" target="_self">🏠 Home</a>', unsafe_allow_html=True)
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

# === Main content ===
if pathway == "Select...":
    st.markdown("""
<h1 style='color:#FFFFFF;'>🧬 Welcome to PathwayPix</h1>

<p style='font-size:17px; color:#E2E2E2;'>
<strong>Biochemistry is often taught as a subject full of pathways to memorize, enzymes to name, and cofactors to list.</strong>  
But to me, it never felt like that.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
As someone deeply obsessed with organic chemistry, I realized that biochemistry is just <strong>Orgo in motion</strong> — carbon doing what carbon does best: reacting with purpose.  
Once I started looking at pathways through that lens, everything clicked. There’s no need to memorize when you understand the logic behind each molecular move.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
Textbooks rarely explain it this way. They show you what happens, but not why. The mechanisms, the regulation, the energy logic — it’s all flattened into diagrams and labels.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
That’s why I built PathwayPix: to make biochemistry interactive, visual, and actually fun.  
I want students to explore what’s happening, understand how hormones like insulin change the flow of metabolism, and zoom in to see the organic transformations behind each reaction.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
If you’ve ever felt like biochemistry was just a wall of facts, I built this to show you that it’s actually a beautiful, logical dance of electrons.  
Let carbon do its thing — you’ll see.
</p>

<hr style='margin-top:40px; margin-bottom:40px; border-color:#444;'>

<h2 style='color:#FFFFFF;'>💡 Why I Built This Webapp</h2>

<p style='font-size:17px; color:#E2E2E2;'>
PathwayPix isn't about memorizing pathways. It's about understanding them — how they work, why they change, and where control happens.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
This platform helps you:<br>
<strong>See</strong> what’s happening in each step<br>
<strong>Understand</strong> how small molecular shifts serve strategic purposes<br>
<strong>Follow</strong> the biochemical logic, not just the names
</p>

<p style='font-size:17px; color:#E2E2E2;'>
When you grasp the “why,” the “what” becomes obvious.
</p>

<hr style='margin-top:40px; margin-bottom:40px; border-color:#444;'>

<h2 style='color:#FFFFFF;'>🧠 Design Philosophy</h2>

<h3 style='color:#F5F5F5;'>1. Every isomerization happens for a reason.</h3>
<p style='font-size:17px; color:#E2E2E2;'>
Molecules don’t randomly shift shapes. Whether it’s a carbonyl repositioning, a ring opening, or a sugar flipping forms — there’s always a strategy.
Each isomerization supports a specific goal:
</p>

<ul style='font-size:17px; color:#E2E2E2;'>
<li>Preparing a molecule for cleavage</li>
<li>Enabling a redox reaction</li>
<li>Creating symmetry for branching</li>
</ul>

<p style='font-size:17px; color:#E2E2E2;'>
You’ll see how structure dictates strategy — and how elegant it all becomes when you look at it through an organic chemistry lens.
</p>

<h3 style='color:#F5F5F5;'>2. Regulatory steps aren’t trivia — they’re turning points.</h3>
<p style='font-size:17px; color:#E2E2E2;'>
Control points in metabolism aren’t just facts to memorize. They’re where the story shifts.
</p>

<p style='font-size:17px; color:#E2E2E2;'>
Rather than just labeling PFK-1 as “regulated,” we ask:
</p>

<ul style='font-size:17px; color:#E2E2E2;'>
<li>Why is regulation here?</li>
<li>What changes before and after this step?</li>
<li>What is the cell trying to achieve?</li>
</ul>

<p style='font-size:17px; color:#E2E2E2;'>
When you understand regulation as narrative pressure — not just static control — the logic comes alive.
</p>
""", unsafe_allow_html=True)

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

