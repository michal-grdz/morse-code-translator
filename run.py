from flask import Flask
import translation_logic as tl

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/to_morse/<text>', methods=['GET'])
def to_morse(text):
    return tl.text_to_morse(text)

@app.route('/from_morse/<morse>', methods=['GET'])
def from_morse(morse):
    return tl.morse_to_text(morse)

if __name__ == "__main__":
    app.run(debug=True)
