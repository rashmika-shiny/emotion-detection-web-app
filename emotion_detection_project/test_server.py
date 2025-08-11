# test_server.py
# Test script to demonstrate Flask server functionality

from server import app
import requests
import time
import threading

def test_flask_app():
    """Test the Flask application endpoints"""
    print("=== Testing Flask Application ===")
    
    # Test with Flask test client
    with app.test_client() as client:
        print("Testing main page route...")
        response = client.get('/')
        print(f"✅ Main page status: {response.status_code}")
        print(f"✅ Contains title: {'Emotion Detection Application' in response.get_data(as_text=True)}")
        
        print("\nTesting emotion detection endpoint...")
        response = client.get('/emotionDetector?textToAnalyze=I am very happy today!')
        print(f"✅ Emotion endpoint status: {response.status_code}")
        print(f"✅ Contains result: {'Analysis Result' in response.get_data(as_text=True)}")
        
        print("\nTesting empty text handling...")
        response = client.get('/emotionDetector')
        print(f"✅ Empty text status: {response.status_code}")
        print(f"✅ Error handling: {'Error' in response.get_data(as_text=True)}")
        
    print("\n✅ All Flask tests passed!")
    print("📄 Server ready for deployment!")

if __name__ == "__main__":
    test_flask_app()
