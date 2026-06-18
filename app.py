from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
    'zh-CN': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'ja': 'Japanese'
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text_to_translate = data.get('text', '')
        source_lang = data.get('source', 'auto') 
        target_lang = data.get('target', 'en')

        if not text_to_translate:
            return jsonify({'error': 'No text provided'}), 400

        # Translate using GoogleTranslator
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text_to_translate)
        return jsonify({'translated_text': translated})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # We will use port 8000 to keep it entirely clear of Windows default system blocks
    app.run(debug=True, port=8000)