# ============================================================
# AI STUDENT ASSISTANT CHATBOT
# GIST INTERNSHIP - TASK 1
# ============================================================

def chatbot(user_input):

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! 👋 I am your AI Student Assistant. How can I help you today?"

    # Machine Learning
    elif "machine learning" in user_input:
        return "Machine Learning is a branch of AI where computers learn patterns from data and use them to make predictions or decisions."

    # Artificial Intelligence
    elif "artificial intelligence" in user_input or "what is ai" in user_input or user_input == "ai":
        return "Artificial Intelligence (AI) enables computers to perform tasks that normally require human intelligence, such as learning, reasoning and problem-solving."

    # Skills
    elif "skill" in user_input:
        return "Important skills for an AI & Data Science student include Python, SQL, Machine Learning, Data Analysis, GitHub and AI fundamentals."

    # Python
    elif "python" in user_input:
        return "Python is a popular programming language used in AI, Machine Learning, Data Science and automation."

    # Placements
    elif "placement" in user_input:
        return "For placements, focus on programming, SQL, aptitude, communication, projects and technical interview preparation."

    # Projects
    elif "project" in user_input:
        return "Building practical projects helps demonstrate your technical skills. Try projects involving AI, Machine Learning, Data Analysis or automation."

    # Thank you
    elif "thank" in user_input:
        return "You're welcome! 😊 Keep learning and building projects!"

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 All the best with your learning and career!"

    # Unknown question
    else:
        return "I don't have an answer for that yet. Try asking about AI, Machine Learning, Python, skills, projects or placements."


# ============================================================
# CHATBOT INTERFACE
# ============================================================

print("=" * 55)
print("🤖 AI STUDENT ASSISTANT CHATBOT")
print("=" * 55)
print("Ask me about AI, Machine Learning, Python, skills,")
print("projects or placements.")
print("Type 'bye' to exit.")
print("=" * 55)


# ============================================================
# CONVERSATION LOOP
# ============================================================

while True:

    user_input = input("\nYou: ")

    response = chatbot(user_input)

    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        break
