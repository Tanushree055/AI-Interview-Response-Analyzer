import streamlit as st
from analyzer import analyze_answer,check_keywords
from audio import get_voice_input

st.title("AI Interview Response Analyzer")

if "explanation" not in st.session_state:
    st.session_state.explanation=""

topic = st.text_input("Enter Topic")

st.caption("💡 Tip: Try explaining like you're in a real interview")

if st.button("🎤 Speak Answer"):
    spoken=get_voice_input()
    st.session_state.explanation=spoken
    st.write("You said:", spoken)

if st.button("Analyze"):
    if not topic or not st.session_state.explanation:
        st.warning("Please enter both topic and speak your answer")
    
    else:
        result = analyze_answer(topic, st.session_state.explanation)

        sections=result.split("\n\n")
        
        for section in sections:
            if "Score" in section:
                st.subheader("📊 Score")
                st.success(section)

            elif "Missing Concepts" in section:
                st.subheader("❌ Missing Concepts")
                st.warning(section)

            elif "Mistakes" in section:
                st.subheader("⚠️ Mistakes")
                st.error(section)

            elif "Fact Check" in section:
                st.subheader("🔍 Fact Check")
                st.info(section)

            elif "Missing Keywords" in section:
                st.subheader("🧠 Missing Keywords")
                st.warning(section)

            elif "Improved Answer" in section:
                st.subheader("✅ Improved Answer")
                st.success(section)

            elif "Follow-up Questions" in section:
                st.subheader("🎤 Follow-up Questions")
                st.info(section)
        
        missing_keywords=check_keywords(topic,st.session_state.explanation)
        
        if missing_keywords:
            st.subheader("⚙️ Missing Keywords (System Check)")
            st.error(", ".join(missing_keywords))
    
