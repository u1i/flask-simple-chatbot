from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# A simple function to handle chatbot responses
def chatbot_response(message):
    # Here you can integrate your chatbot logic
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a bot, but I'm doing great! How about you?"
    }
    return responses.get(message.lower(), "I'm not sure how to respond to that.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_text = request.form['msg']
    response = chatbot_response(user_text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

