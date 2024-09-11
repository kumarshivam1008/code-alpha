import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# Load SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Define a list of FAQ questions and their corresponding answers
faq_data = {
    "What is your return policy?": "Our return policy allows you to return products within 30 days of purchase.",
    "How do I track my order?": "You can track your order by logging into your account and visiting the 'Orders' section.",
    "What payment methods do you accept?": "We accept Visa, Mastercard, American Express, and PayPal.",
    "How do I contact customer support?": "You can contact customer support by emailing support@example.com or calling 1-800-123-4567.",
    "Do you offer international shipping?": "Yes, we offer international shipping to select countries. Please check our shipping page for more details.",
}

# List of FAQ questions
faq_questions = list(faq_data.keys())

# Function to find the most similar FAQ question
def find_most_similar_question(user_input):
    # Append user input to FAQ questions for similarity comparison
    all_questions = faq_questions + [user_input]
    
    # Convert questions to vectors using TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(all_questions)
    
    # Calculate similarity between the user input and FAQ questions
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    
    # Find the most similar question (excluding the user input itself)
    similarity_scores = cosine_matrix[-1][:-1]
    most_similar_index = np.argmax(similarity_scores)
    
    return faq_questions[most_similar_index], similarity_scores[most_similar_index]

# Chatbot function
def chatbot():
    print("Hello! I am an FAQ chatbot. Ask me anything about our services.")
    print("Type 'quit' to exit the chat.")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "quit":
            print("Goodbye! and fuck you")
            break
        
        # Process user input with spaCy
        user_input_nlp = nlp(user_input)
        
        # Find the most similar FAQ question
        most_similar_question, similarity_score = find_most_similar_question(user_input)
        
        # If the similarity is high enough, provide the answer
        if similarity_score > 0.5:  # Threshold can be adjusted
            print(f"\nBot: {faq_data[most_similar_question]}")
        else:
            print("\nBot: I'm sorry, I couldn't find an answer to that question. Please try asking differently.")

# Run the chatbot
chatbot()
