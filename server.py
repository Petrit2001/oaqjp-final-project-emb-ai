"""Flask web server for the emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return the result."""
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the start page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
