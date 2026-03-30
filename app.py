import streamlit as st

st.title("📩 Spam Detection App")

msg = st.text_input("Enter your message")

if st.button("Check"):
    if "offer" in msg or "win" in msg:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Not Spam")