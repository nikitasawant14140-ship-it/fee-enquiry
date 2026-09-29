# ============================================================
# AI FEE ENQUIRY CHATBOT
# M.Sc. (Computer Application) - Semester III
# Subject: Artificial Intelligence
# Credit Activity 1
# ============================================================

import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import re
import random


# ============================================================
# 1. FAQ DATABASE
# ============================================================

faqs = {

    "tuition_fee": {
        "questions": [
            "what is the tuition fee",
            "tuition fee",
            "college fees",
            "course fees",
            "how much is the tuition fee",
            "how much are the fees",
            "fee structure"
        ],
        "answer": (
            "The tuition fee depends on the course and academic year. "
            "Please contact the college office for the latest official fee structure."
        )
    },

    "admission_fee": {
        "questions": [
            "what is the admission fee",
            "admission fee",
            "admission fees",
            "how much is admission fee",
            "fee for admission"
        ],
        "answer": (
            "The admission fee is applicable at the time of admission. "
            "The exact amount depends on the course and college rules."
        )
    },

    "exam_fee": {
        "questions": [
            "what is the exam fee",
            "exam fee",
            "examination fee",
            "exam fees",
            "how much is exam fee"
        ],
        "answer": (
            "The examination fee is charged according to the examination "
            "and university rules. Please check the latest examination notice "
            "or contact the college office."
        )
    },

    "hostel_fee": {
        "questions": [
            "what is the hostel fee",
            "hostel fee",
            "hostel fees",
            "how much is hostel fee",
            "hostel charges"
        ],
        "answer": (
            "Hostel fees are separate from academic fees. "
            "The amount depends on the hostel facility and room type."
        )
    },

    "payment_methods": {
        "questions": [
            "how can i pay the fees",
            "how to pay fees",
            "payment methods",
            "fee payment method",
            "where can i pay the fees",
            "how do i pay"
        ],
        "answer": (
            "Fees can be paid using the payment methods provided by the "
            "college. Please check the official fee payment portal or "
            "contact the college office for the currently available methods."
        )
    },

    "online_payment": {
        "questions": [
            "can i pay fees online",
            "online fee payment",
            "pay fees online",
            "can fees be paid online",
            "online payment"
        ],
        "answer": (
            "Yes, if online payment is enabled by the college, students "
            "can pay through the official fee payment portal."
        )
    },

    "fee_deadline": {
        "questions": [
            "when is the fee deadline",
            "fee payment deadline",
            "last date for fee payment",
            "last date to pay fees",
            "fee due date",
            "when should i pay fees"
        ],
        "answer": (
            "The fee payment deadline may change for each semester or "
            "academic year. Please check the latest college notice for "
            "the exact last date."
        )
    },

    "late_fee": {
        "questions": [
            "is there a late fee",
            "late fee",
            "late fees",
            "penalty for late payment",
            "what happens if i pay late",
            "late payment"
        ],
        "answer": (
            "A late payment charge may be applicable if the fee is paid "
            "after the prescribed deadline. Please check the latest "
            "college notice for the applicable amount."
        )
    },

    "fee_receipt": {
        "questions": [
            "how can i get fee receipt",
            "fee receipt",
            "payment receipt",
            "receipt for fees",
            "where is my fee receipt",
            "download fee receipt"
        ],
        "answer": (
            "After successful fee payment, the fee receipt can usually "
            "be downloaded or collected according to the college's "
            "payment procedure."
        )
    },

    "refund": {
        "questions": [
            "fee refund",
            "can i get fee refund",
            "refund policy",
            "how to get refund",
            "fees refund"
        ],
        "answer": (
            "Fee refund depends on the college and university refund policy. "
            "Please contact the college office for the applicable rules."
        )
    },

    "scholarship": {
        "questions": [
            "is scholarship available",
            "scholarship",
            "fee scholarship",
            "scholarships",
            "can i get scholarship"
        ],
        "answer": (
            "Scholarship availability depends on eligibility criteria and "
            "the scholarship schemes applicable to the student. "
            "Please contact the college scholarship or administration office."
        )
    },

    "installment": {
        "questions": [
            "can i pay fees in installments",
            "installment",
            "installments",
            "pay fees in parts",
            "fee installment"
        ],
        "answer": (
            "Payment in installments depends on the college's rules. "
            "Please contact the college office to confirm whether "
            "installment payment is available."
        )
    }
}


# ============================================================
# 2. TEXT PREPROCESSING
# ============================================================

def clean_text(text):
    """
    Converts user input into a simple normalized form.
    """

    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# ============================================================
# 3. KEYWORD / FAQ MATCHING
# ============================================================

def calculate_score(user_input, question):
    """
    Calculates similarity using common words.
    This is a simple NLP approach suitable for a basic AI chatbot.
    """

    user_words = set(clean_text(user_input).split())
    question_words = set(clean_text(question).split())

    if not user_words or not question_words:
        return 0

    common_words = user_words.intersection(question_words)

    # Basic matching score
    score = len(common_words) / len(question_words)

    return score


def find_best_answer(user_input):

    user_input = clean_text(user_input)

    best_score = 0
    best_answer = None

    for faq in faqs.values():

        for question in faq["questions"]:

            score = calculate_score(user_input, question)

            if score > best_score:
                best_score = score
                best_answer = faq["answer"]

    # Confidence threshold
    if best_score >= 0.30:
        return best_answer

    return (
        "Sorry, I could not understand your question.\n\n"
        "You can ask me about:\n"
        "• Tuition fee\n"
        "• Admission fee\n"
        "• Exam fee\n"
        "• Hostel fee\n"
        "• Payment methods\n"
        "• Online payment\n"
        "• Fee deadline\n"
        "• Late fee\n"
        "• Fee receipt\n"
        "• Refund\n"
        "• Scholarship\n"
        "• Installments"
    )


# ============================================================
# 4. GREETING FUNCTION
# ============================================================

def get_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "Good morning!"

    elif hour < 17:
        return "Good afternoon!"

    else:
        return "Good evening!"


# ============================================================
# 5. CHATBOT RESPONSE
# ============================================================

def chatbot_response(user_input):

    text = clean_text(user_input)

    # Exit commands
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using the Fee Enquiry Chatbot. Goodbye!"

    # Greetings
    greetings = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if text in greetings:
        return (
            get_greeting()
            + " I am the Fee Enquiry Chatbot.\n\n"
              "How can I help you with your fee-related enquiry?"
        )

    # Thank you
    if "thank" in text:
        return random.choice([
            "You're welcome!",
            "You're welcome. Happy to help!",
            "No problem!",
            "Glad I could help!"
        ])

    # Main AI matching
    return find_best_answer(user_input)


# ============================================================
# 6. SEND MESSAGE
# ============================================================

def send_message(event=None):

    user_input = entry.get().strip()

    if user_input == "":
        return

    # Display user message
    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        "You: " + user_input + "\n",
        "user"
    )

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display chatbot response
    chat_area.insert(
        tk.END,
        "Bot: " + response + "\n\n",
        "bot"
    )

    chat_area.config(state=tk.DISABLED)

    # Clear input box
    entry.delete(0, tk.END)

    # Automatically scroll to bottom
    chat_area.see(tk.END)

    # Close application if user says bye
    if clean_text(user_input) in ["bye", "exit", "quit", "goodbye"]:
        root.after(1500, root.destroy)


# ============================================================
# 7. CLEAR CHAT
# ============================================================

def clear_chat():

    chat_area.config(state=tk.NORMAL)

    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Chat cleared.\n\n"
        "How can I help you with your fee enquiry?\n\n"
    )

    chat_area.config(state=tk.DISABLED)


# ============================================================
# 8. GUI WINDOW
# ============================================================

root = tk.Tk()

root.title("AI Fee Enquiry Chatbot")
root.geometry("750x650")
root.resizable(False, False)


# ============================================================
# 9. HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#2E3A59",
    height=80
)

header.pack(fill=tk.X)

title_label = tk.Label(
    header,
    text="AI Fee Enquiry Chatbot",
    font=("Arial", 22, "bold"),
    bg="#2E3A59",
    fg="white"
)

title_label.pack(pady=(15, 0))


subtitle_label = tk.Label(
    header,
    text="M.Sc. Computer Application | Artificial Intelligence",
    font=("Arial", 10),
    bg="#2E3A59",
    fg="white"
)

subtitle_label.pack()


# ============================================================
# 10. CHAT AREA
# ============================================================

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11),
    width=80,
    height=27,
    bg="#F5F7FA",
    state=tk.DISABLED
)

chat_area.pack(
    padx=15,
    pady=15
)


# Text formatting
chat_area.tag_config(
    "user",
    foreground="#1A73E8",
    font=("Arial", 11, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="#188038",
    font=("Arial", 11)
)


# ============================================================
# 11. INITIAL MESSAGE
# ============================================================

chat_area.config(state=tk.NORMAL)

chat_area.insert(
    tk.END,
    "Bot: " + get_greeting() +
    " I am the AI Fee Enquiry Chatbot.\n\n",
    "bot"
)

chat_area.insert(
    tk.END,
    "Bot: You can ask me questions about tuition fees, "
    "admission fees, exam fees, payment methods, deadlines, "
    "receipts, scholarships and more.\n\n",
    "bot"
)

chat_area.config(state=tk.DISABLED)


# ============================================================
# 12. INPUT FRAME
# ============================================================

input_frame = tk.Frame(root)

input_frame.pack(
    fill=tk.X,
    padx=15,
    pady=(0, 10)
)


entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=58
)

entry.pack(
    side=tk.LEFT,
    padx=(0, 10),
    ipady=8
)


send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#2E3A59",
    fg="white",
    width=10,
    command=send_message
)

send_button.pack(
    side=tk.LEFT
)


clear_button = tk.Button(
    root,
    text="Clear Chat",
    font=("Arial", 10),
    command=clear_chat
)

clear_button.pack(
    pady=(0, 10)
)


# ============================================================
# 13. ENTER KEY SUPPORT
# ============================================================

root.bind(
    "<Return>",
    send_message
)


# ============================================================
# 14. START CHATBOT
# ============================================================

entry.focus()

root.mainloop()