# emotion_detector.py
# Main emotion detection functionality

import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP.
    
    Args:
        text_to_analyze (str): Text to analyze for emotions
    
    Returns:
        dict: Dictionary containing emotion scores and dominant emotion,
              or None values if input is invalid or API fails
    """
    # Input validation - check for blank or None text
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Watson NLP API URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
        'Content-Type': 'application/json'
    }
    
    # Request payload
    myobj = {
        'raw_document': {
            'text': text_to_analyze
        }
    }
    
    # Make the API request
    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=5)
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        # If API is unavailable, return None values
        print(f"API connection failed: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Handle the response based on status code
    if response.status_code == 200:
        # Successful response - parse the JSON
        try:
            formatted_response = json.loads(response.text)
            
            # Extract emotion scores
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            
            # Get individual emotion scores
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Find the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Return formatted response
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing response: {e}")
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    
    elif response.status_code == 400:
        # Bad Request - Invalid input (e.g., blank text, malformed request)
        print(f"Bad Request (400): Invalid input provided to the API")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    elif response.status_code == 500:
        # Internal Server Error
        print(f"Internal Server Error (500): API server error")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    else:
        # Handle other error cases
        print(f"API Error {response.status_code}: {response.text}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

def emotion_predictor(text_to_analyze):
    """
    Wrapper function that formats the emotion detection output.
    
    Args:
        text_to_analyze (str): Text to analyze for emotions
    
    Returns:
        str: Formatted string with emotion analysis results
    """
    # Get the raw emotion detection results
    result = emotion_detector(text_to_analyze)
    
    # Handle the case where API is unavailable
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the output string
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    
    formatted_output = f"For the given statement, the system response is 'anger': {anger}, "
    formatted_output += f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    formatted_output += f"The dominant emotion is {dominant_emotion}."
    
    return formatted_output
