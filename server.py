from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    answer = chat_completion.choices[0].message.content
    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
