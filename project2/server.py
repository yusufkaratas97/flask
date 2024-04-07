"""
This module serves as the main server script for the Emotion Detector web application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Render the index page of the website.

    This function utilizes the render_template function to render the index.html template.
    The index.html template typically serves as the main landing page of the website.

    Returns:
        str: The HTML content of the rendered index page.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return " Invalid text! Please try again!."
    return f"For the given statement, the system response is \
        'anger': {response['anger']}, 'disgust': {response['disgust']}, '\
        fear': {response['fear']}, 'joy': {response['joy']} and 'sadness\
        ': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
    Render the index page of the website.

    This function utilizes the render_template function to render the index.html template.
    The index.html template typically serves as the main landing page of the website.

    Returns:
        str: The HTML content of the rendered index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
