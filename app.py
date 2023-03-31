from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response')
def get_response():
    prompt = request.args.get('msg')
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)