from flask import Flask, render_template, request, jsonify
import json
import logging

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load intents from the JSON file
try:
    with open('data/intents.json') as f:
        intents_data = json.load(f)
    logging.info("Successfully loaded intents.json")
except FileNotFoundError:
    logging.warning("intents.json file not found. Initializing with an empty dictionary.")
    intents_data = {"intents": []}
except json.JSONDecodeError:
    logging.error("Error decoding intents.json. Check if it's valid JSON.")
    intents_data = {"intents": []}

# Create a dictionary to easily access intents by tag
intents = {intent['tag']: intent for intent in intents_data.get('intents', [])}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    logging.debug(f"Received message: {user_message}")
    
    response = "I'm sorry, I don't have an answer to that question."
    redirect_url = None

    for intent in intents.values():
        for pattern in intent.get('patterns', []):
            if pattern.lower() in user_message:
                # Pick a random response from the matched intent
                response = intent['responses'][0] if intent.get('responses') else response
                follow_up = intent.get('follow_up')
                if follow_up:
                    # Check if the message contains follow-up intent keywords
                    for yes_pattern in follow_up.get('yes_patterns', []):
                        if yes_pattern in user_message:
                            response = follow_up['yes_response']
                            redirect_url = follow_up['redirect']
                            break
                    for no_pattern in follow_up.get('no_patterns', []):
                        if no_pattern in user_message:
                            response = follow_up['no_response']
                            break
                break
        if redirect_url:
            break

    logging.debug(f"Response: {response}, Redirect URL: {redirect_url}")
    return jsonify({'message': response, 'redirect': redirect_url})

# Define routes for other pages
@app.route('/diag')
def diag():
    return render_template('diag.html')

@app.route('/treatment')
def treatment():
    return render_template('treatment.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/adhd')
def adhd():
    return render_template('adhd.html')

@app.route('/autism')
def autism():
    return render_template('autism.html')

@app.route('/ocd')
def ocd():
    return render_template('ocd.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
