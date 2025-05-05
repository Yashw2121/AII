def greet():
    return "Hello! How can I help you today?"

def goodbye():
    return "Goodbye! Have a great day."

def thank_you():
    return "You're welcome! Is there anything else I can assist you with?"

def ask_help():
    return "I can help you with basic inquiries. What do you need help with?"

def handle_order_inquiry():
    return "I can help with order status or tracking information. Please provide your order number."

def handle_product_info():
    return "We offer a variety of products. Could you please specify which product you are interested in?"

def handle_payment_issue():
    return "If you are having trouble with payment, please contact our support team at [Your Support Email/Phone Number]."

def handle_default():
    return "I'm sorry, I didn't understand your request. Could you please rephrase or ask in a different way?"

def chatbot():
    print("Chatbot : ",greet())
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot:", greet())
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot:", goodbye())
            break
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot:", thank_you())
        elif "help" in user_input or "assist" in user_input:
            print("Chatbot:", ask_help())
        elif "order" in user_input or "track" in user_input:
            print("Chatbot:", handle_order_inquiry())
        elif "product" in user_input or "item" in user_input:
            print("Chatbot:", handle_product_info())
        elif "payment" in user_input or "pay" in user_input or "issue" in user_input or "problem" in user_input:
            print("Chatbot:", handle_payment_issue())
        else:
            print("Chatbot:", handle_default())

if __name__ == "__main__":
    chatbot()