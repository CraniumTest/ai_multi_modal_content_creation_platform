from flask import Flask, request, jsonify, send_file
import openai
from PIL import Image
from io import BytesIO
from gtts import gTTS

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Text Generation using OpenAI GPT
@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

# Basic Image Generation - Mock Example
@app.route('/generate_image', methods=['POST'])
def generate_image():
    # This is a placeholder example since image generation is complex
    img = Image.new('RGB', (100, 100), color='blue')
    buf = BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')

# Text-to-Speech using gTTS
@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text', '')
    tts = gTTS(text=text, lang='en')
    buf = BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    return send_file(buf, mimetype='audio/mpeg', as_attachment=True, attachment_filename="audio.mp3")

if __name__ == '__main__':
    app.run(debug=True)
