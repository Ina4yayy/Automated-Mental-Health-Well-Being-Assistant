from flask import Flask, render_template, request, jsonify
from chatbot import get_chat_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = get_chat_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
