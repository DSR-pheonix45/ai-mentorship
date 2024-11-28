from model import MentorshipModel
from utils import format_response, get_user_input

def main():
    # Replace 'your_api_token' with your actual Hugging Face API token
    api_token = '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'
    model = MentorshipModel(api_token)
    print("AI Mentor: Hello! I'm here to help you. What do you want to talk about?")
    
    while True:
        user_input = get_user_input()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("AI Mentor: Goodbye!")
            break
        
        try:
            response = model.generate_response(user_input)
            print(f"AI Mentor: {format_response(response)}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()