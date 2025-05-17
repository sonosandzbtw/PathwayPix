import streamlit as st
from PIL import Image

st.set_page_config(page_title="PathwayPix", layout="wide")

# Custom CSS for Zoomcamp-style layout and dark theme
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
            color: #f1f5f9;
        }
        .css-1d391kg, .css-18e3th9 {
            background-color: #0f172a !important;
        }
        .css-10trblm {
            color: #f1f5f9;
        }
        .block-container {
            padding: 3rem 2rem 2rem 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #0f172a;
        }
        a {
            color: #38bdf8 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🧬 PathwayPix")
    selected_pathway = st.selectbox(
        "Select a Pathway",
        ["Select...", "Glycolysis", "Phosphate Dehydrogenation", "Krebs Cycle", "Electron Transport Chain"],
        index=0
    )
    st.markdown("---")
    st.page_link("pages/how_to_use.py", label="How to Use")
    st.page_link("pages/about.py", label="About Developer")

# Main Content
if selected_pathway == "Glycolysis":
    st.title("Glycolysis")
    try:
        st.image("assets/glycolysis.png", use_container_width=True)
    except:
        st.warning("Please add 'glycolysis.png' to the 'assets/' folder.")

elif selected_pathway == "Phosphate Dehydrogenation":
    st.title("Phosphate Dehydrogenation")
    st.warning("Coming soon!")

elif selected_pathway == "Krebs Cycle":
    st.title("Krebs Cycle")
    st.warning("Coming soon!")

elif selected_pathway == "Electron Transport Chain":
    st.title("Electron Transport Chain")
    st.warning("Coming soon!")

else:
    st.title("🧬 Welcome to PathwayPix")

    st.markdown("""
Biochemistry is usually taught as a list of things to memorize: pathways, enzymes, cofactors, and control steps. But for me, it was never about memorization.

I’ve always been in love with organic chemistry. And one day it just clicked—biochemistry is organic chemistry in motion. It's not random, it's not arbitrary. Carbon atoms are reacting, adapting, and creating logic with every step. That’s when I stopped seeing it as content to study and started seeing it as a system to understand.

Textbooks don’t help with that. They show you what happens, but not why it happens. They flatten the story into static diagrams and bullet points. So I made this.

PathwayPix is for anyone who wants to see biochemistry as a logical, visual, moving system. Where structure changes make sense. Where enzymes don’t just do things—they have reasons.

---

### Why I Made This

I want people to see what's really going on.

Instead of flipping flashcards, you’ll be tracing reaction paths. You'll see how glucose gets trapped inside a cell, how a phosphate group sets up a molecular ambush, how ATP investment pays off downstream.

And most importantly, you’ll learn the why behind every shift. Why isomerization happens before cleavage. Why regulation hits that step and not the next one. Why the same carbon framework flows one way in a fed state and the opposite way in a fasted state.

---

### Design Philosophy

Every isomerization has a reason. It’s not a coincidence. It’s chemistry working for strategy—whether it’s about making a bond breakable, setting up redox, or preparing symmetry.

Regulation tells a story. It’s not just “this step is inhibited.” It’s about commitment points, metabolic pressure, and the system adapting to context. The story of glycolysis changes depending on insulin, glucagon, or ATP levels. That’s what makes it fascinating.

---

### What You’ll Get Out of This

You’ll stop memorizing.
You’ll start understanding.

You’ll begin to see pathways not as walls of facts, but as beautifully engineered systems—where carbon, electrons, and enzymes are just doing what they do best.

Let carbon do its thing. You’ll see.
""")

