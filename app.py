import streamlit as st

# Page configuration
st.set_page_config(
    page_title="College Student Support",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 AI Chatbot for College Student Support")
st.write("Ask me questions about college, courses, exams, fees, hostel and scholarships.")

# College information
college_info = {
    "courses": "Our college offers B.Tech programs in CSE, ECE, EEE, Mechanical and Civil Engineering.",
    
    "exam": "Exam schedules are usually announced by the examination department. Students should check college notices regularly.",
    
    "fees": "For information about tuition fees and other charges, please contact the college administration office.",
    
    "scholarship": "Students can contact the scholarship section for information about eligibility, required documents and application status.",
    
    "hostel": "The college hostel provides accommodation and basic facilities for students. Contact the hostel office for availability and rules.",
    
    "placement": "The placement cell helps students with internships, placement drives, aptitude training and interview preparation.",
    
    "library": "The college library provides textbooks, reference books and study resources for students.",
    
    "attendance": "Students should maintain the minimum attendance percentage required by their college regulations.",
    
    "contact": "For official information, contact the respective college department or administration office."
}

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chatbot response function
def get_response(user_question):

    question = user_question.lower()

    if "course" in question or "branch" in question:
        return college_info["courses"]

    elif "exam" in question or "test" in question:
        return college_info["exam"]

    elif "fee" in question or "fees" in question:
        return college_info["fees"]

    elif "scholarship" in question:
        return college_info["scholarship"]

    elif "hostel" in question:
        return college_info["hostel"]

    elif "placement" in question or "job" in question:
        return college_info["placement"]

    elif "library" in question:
        return college_info["library"]

    elif "attendance" in question:
        return college_info["attendance"]

    elif "contact" in question or "office" in question:
        return college_info["contact"]

    elif "hello" in question or "hi" in question:
        return "Hello! 👋 How can I help you with your college-related questions?"

    elif "thank" in question:
        return "You're welcome! 😊 I'm happy to help."

    else:
        return "Sorry, I don't have information about that yet. Please ask me about courses, exams, fees, scholarships, hostel, placements, library or attendance."


# User input
user_question = st.chat_input("Ask your question...")

if user_question:

    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    # Generate response
    response = get_response(user_question)

    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(response)

    # Save response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )


# Sidebar
with st.sidebar:
    st.header("🎓 College Support")

    st.write("You can ask about:")

    st.write("📚 Courses")
    st.write("📝 Exams")
    st.write("💰 Fees")
    st.write("🎓 Scholarships")
    st.write("🏠 Hostel")
    st.write("💼 Placements")
    st.write("📖 Library")
    st.write("📊 Attendance")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()