import streamlit as st

# Set page configuration with a light theme
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="💡", layout="centered")

# Custom CSS Styles
st.markdown("""
    <style>
        body {
            background-color: #f0f9ff;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            color: #0f172a;
            font-weight: bold;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }
        .intro-text {
            text-align: center;
            font-size: 18px;
            color: #334155;
            margin-bottom: 30px;
        }
        .section-title {
            font-size: 28px;
            color: #0ea5e9;
            font-weight: bold;
            border-bottom: 2px solid #0ea5e9;
            padding-bottom: 5px;
        }
        .quote-box {
            background: linear-gradient(135deg, #3b82f6, #06b6d4);
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
            box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        }
        .quiz-box {
            background: #ecfeff;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .response-box {
            background-color: #e0f7fa;
            padding: 12px;
            border-radius: 8px;
            margin-top: 10px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        }
        .commit-btn {
            background-color: #0ea5e9;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            width: 100%;
            text-align: center;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
            transition: 0.3s;
        }
        .commit-btn:hover {
            background-color: #0284c7;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<h1 class="main-title">🌱 Growth Mindset Challenge</h1>', unsafe_allow_html=True)
st.markdown('<p class="intro-text">A growth mindset is the belief that abilities and intelligence can be developed through effort, learning, and persistence.</p>', unsafe_allow_html=True)

# Section 1: What is a Growth Mindset?
st.markdown('<h2 class="section-title">📖 What is a Growth Mindset?</h2>', unsafe_allow_html=True)
st.write("A growth mindset means believing that you can improve your skills with effort and learning. Unlike a fixed mindset, which assumes intelligence and abilities are static, a growth mindset embraces challenges as opportunities to grow.")

# Section 2: Benefits of a Growth Mindset
st.markdown('<h2 class="section-title"> Why Adopt a Growth Mindset?</h2>', unsafe_allow_html=True)
benefits = [
    "🌟 Embrace challenges as learning opportunities",
    "🔄 Learn from mistakes instead of fearing them",
    "💪 Stay determined even when things get tough",
    "🎉 Celebrate effort, not just results",
    "🧐 Keep an open mind and stay curious",
]
st.markdown("\n".join([f"- {b}" for b in benefits]))

# Interactive Section: Growth Mindset Quiz
st.markdown('<h2 class="section-title">🧠 Growth Mindset Quiz</h2>', unsafe_allow_html=True)
quiz_question = "What challenge are you currently facing?"
user_response = st.text_area("Your Answer:")

# Display user response with styling
if user_response:
    st.markdown(
        f"""
        <div class="response-box">
            <p style="color: #0288d1; font-weight: bold;">Spectacular! <span style="font-weight: normal">You're working on:</span> "{user_response}"</p>
            <p style="color: #00796b;">Challenges help us grow. Keep striving! 🚀</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Motivational Quote Section
st.markdown('<h2 class="section-title"> Stay Motivated!</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="quote-box">
        “Success is not final, failure is not fatal: it is the courage to continue that counts.” - Winston Churchill
    </div>
    """,
    unsafe_allow_html=True
)

# Call to Action
st.markdown('<h2 class="section-title"> Start Your Growth Journey</h2>', unsafe_allow_html=True)
st.write("Adopting a growth mindset is a lifelong journey. Keep challenging yourself and embracing new learning experiences!")

if st.button("I Commit to a Growth Mindset! 🎯", key="commit"):
    st.snow()
    st.success("Awesome! Keep pushing forward with a growth mindset!")

# Footer
st.write("Made with ❤️ using Streamlit")
