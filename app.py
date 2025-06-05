import streamlit as st

# Page configuration
st.set_page_config(page_title="Maya Bot - The Game Changer", page_icon="💜", layout="centered")

# Branding and Header
st.markdown("### *When It’s Quiet, Stay Ready.*")

# Custom button styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #800080;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Title and Overview
st.title("💜 Maya Bot: The Game Changer")
st.subheader("Motivation & Nurture Specialist")

st.markdown("**Style of Play:** Impactful, strategic, leadership-focused")

st.markdown("""
Maya keeps you engaged during the quiet moments of the recruiting process.  
She delivers motivational check-ins, reflections, and reminders to help you stay mentally strong.

> “When the process feels quiet, Maya reminds you why you started—and how to stay ready.”
""")

# Step 1: Emotional Check-In
st.header("Step 1: Emotional Check-In")
mood = st.selectbox("How are you feeling right now?", [
    "Frustrated", "Unmotivated", "Overwhelmed", "Hopeful", "Focused", "Discouraged"
])

# Step 2: Maya’s Motivational Message
st.header("Step 2: Maya’s Message to You")
if mood == "Frustrated":
    st.warning("You’re closer than you think. Silence often means you’re being watched.")
elif mood == "Unmotivated":
    st.info("Discipline outlasts motivation. Stick with your plan.")
elif mood == "Overwhelmed":
    st.info("Take one step at a time. Progress is progress.")
elif mood == "Hopeful":
    st.success("That hope is your fuel. Keep moving forward.")
elif mood == "Focused":
    st.success("Stay sharp. Consistency compounds results.")
elif mood == "Discouraged":
    st.warning("If it were easy, everyone would do it. You’re built different.")

# Step 3: Reflection Journal
st.header("Step 3: Journal Entry")
journal = st.text_area("What are you thinking right now? Reflect, reset, and reframe.")

# Step 4: Delivery Preference
st.header("Step 4: Delivery Method")
contact_method = st.selectbox("Where should Maya send future check-ins?", ["Email", "SMS", "Just in this App"])
contact_info = st.text_input(f"Enter your {contact_method}:")

# Step 5: Submission Summary
if st.button("Save Check-In"):
    st.success("✅ Check-In Submitted")
    st.markdown(f"""
    **Mood:** {mood}  
    **Reflection:** {journal if journal else 'No journal entry provided'}  
    **Delivery:** {contact_method} → {contact_info}
    """)
    st.info("Maya says: Stay ready. You’re not alone in this process.")
    st.balloons()
