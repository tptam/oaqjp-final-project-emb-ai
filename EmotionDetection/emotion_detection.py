"""
Module for emotion detection with the Watson NLP libraries
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotion expressed in given text
    Parameters:
        text_to_analyze (str)
    Returns:
        dict: scores for emotions and dominant emotion name
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/" \
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = payload, headers = header, timeout=30)
    formatted_response = json.loads(response.text)
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    emotion["dominant_emotion"] = max(emotion, key=emotion.get)
    return emotion
