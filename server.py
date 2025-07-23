from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/emotionDetector', methods=['POST'])
def emotion_detect():
    text_to_analyze = request.form['textToAnalyze']
    status = emotion_detector(text_to_analyze)
    if status == 400:
        return "Invalid text! Please try again"
@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detect():
    """
    Process the text input and return emotion scores and dominant emotion.
    """
    ...
# Otherwise, continue showing the emotion response
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response
if __name__ == '__main__':
    app.run(debug=True)
