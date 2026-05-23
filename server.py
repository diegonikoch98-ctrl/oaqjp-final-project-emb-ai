from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response is None or response.get('dominant_emotion') is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!."
        
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    output_message = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )
    
    return output_message

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)