import streamlit as st

# Page setup
st.set_page_config(page_title="Maya Bot - Motivation & Nurture", page_icon="💜", layout="centered")

# Branding
st.image("Upgraded logo 3-13-24 black letters sports on road.png", width=200)
st.markdown("### *When It’s Quiet, Stay Ready.*")

# Button style
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

# Title
st.title("💜 Maya Bot: The Game Changer")
st.subheader("Motivation & Nurture Specialist")
st.markdown("**Style of Play:** Impactful, strategic, leadership-focused")

st.markdown("""
Maya keeps you engaged when the process gets quiet. 
She checks in with you, sends messages that lift your mindset, and reminds you why you started.

> "When the process feels quiet, Maya reminds you why you started—and how to stay ready."
""")

# Step 1: How Are You Feeling?
st.header("Step 1: Emotional Check-In")
feeling = st.selectbox("How are you feeling about recruiting right now?", [
    "Frustrated",
    "Unmotivated",
    "Overwhelmed",
    "Hopeful",
    "Focused",
    "Discouraged"
])

# Step 2: Message or Resource
st.header("Step 2: Maya’s Message to You")
if feeling == "Frustrated":
    st.warning("You’re closer than you think. Sometimes silence means they're watching.")
elif feeling == "Unmotivated":
    st.info("Remember why you started. Your discipline will outlast your mood.")
elif feeling == "Overwhelmed":
    st.info("Take one step today. You don’t need to have it all figured out.")
elif feeling == "Hopeful":
    st.success("Hope is fuel. Let’s channel that into action.")
elif feeling == "Focused":
    st.success("Locked in. Stay ready so you don’t have to get ready.")
elif feeling == "Discouraged":
    st.warning("Discouragement means you care. That’s your edge. Keep going.")

# Step 3: Daily Affirmation
st.header("Step 3: Daily Affirmation")
st.markdown("""
> *"I will not let silence define my story. I am seen. I am preparing. I am enough."*
""")

# Step 4: Optional Journal Entry
st.header("Step 4: Reflection Journal")
journal = st.text_area("Write a few thoughts. What are you proud of today? What will you do next?")

# Step 5: Delivery Method
st.header("Step 5: Stay Connected")
delivery = st.selectbox("Where should Maya check in with you?", ["Email", "SMS", "Just in this app"])
contact = st.text_input(f"Enter your {delivery}:")

# Summary
if st.button("Save and Reset"):
    st.success("📝 Entry Saved")
    st.markdown(f"""
    **Mood:** {feeling}  
    **Delivery Preference:** {delivery} → {contact}  
    **Reflection:** {journal if journal else 'No notes today'}
    """)
    st.info("Maya says: Keep going. Coaches notice what others overlook.")
    st.balloons()
