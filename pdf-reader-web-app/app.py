from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    user_question = request.form['question']
    api_key = request.form['api_key']  # Add this line to get the API key from the form
    openai.api_key = api_key

    prompt = f"Question: {user_question}\nAnswer:"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )

    generated_answer = response['choices'][0]['text'].strip()

    return render_template('index.html', answer=generated_answer)

if __name__ == '__main__':
    app.run(debug=True)
