"""Emotion detection using the Watson NLP library."""
import requests


def emotion_detector(text_to_analyze):
    """Return the emotion scores and the dominant emotion for a text."""
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers, timeout=30)
    if response.status_code == 400:
        return dict.fromkeys(
            ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion'])
    emotions = response.json()['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions