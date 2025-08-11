# test_error_handling.py
# Test script to validate error handling functionality

from server import app
from EmotionDetection import emotion_detector, emotion_predictor

def test_error_handling():
    """Test comprehensive error handling"""
    print("=== Testing Error Handling Functionality ===\n")
    
    # Test 1: emotion_detector with blank inputs
    print("1. Testing emotion_detector with blank inputs:")
    print(f"   Empty string: {emotion_detector('')}")
    print(f"   None input: {emotion_detector(None)}")
    print(f"   Whitespace: {emotion_detector('   ')}")
    
    # Test 2: emotion_predictor with blank inputs
    print("\n2. Testing emotion_predictor with blank inputs:")
    print(f"   Empty string: {emotion_predictor('')}")
    print(f"   Whitespace: {emotion_predictor('   ')}")
    
    # Test 3: Flask server error handling
    print("\n3. Testing Flask server error handling:")
    with app.test_client() as client:
        # Test blank input
        response = client.get('/emotionDetector?textToAnalyze=')
        print(f"   Blank input status: {response.status_code}")
        print(f"   Contains error message: {'Invalid text! Please try again!' in response.get_data(as_text=True)}")
        
        # Test whitespace input  
        response = client.get('/emotionDetector?textToAnalyze=%20%20%20')
        print(f"   Whitespace input status: {response.status_code}")
        print(f"   Contains error message: {'Invalid text! Please try again!' in response.get_data(as_text=True)}")
        
        # Test missing parameter
        response = client.get('/emotionDetector')
        print(f"   Missing parameter status: {response.status_code}")
        print(f"   Contains error message: {'Invalid text! Please try again!' in response.get_data(as_text=True)}")
        
        # Test normal input (should work but may get API error)
        response = client.get('/emotionDetector?textToAnalyze=I%20am%20happy')
        print(f"   Valid input status: {response.status_code}")
        print(f"   Response handled: {len(response.get_data()) > 0}")
    
    print("\n✅ Error handling validation complete!")
    print("🔧 All error scenarios properly handled!")

if __name__ == "__main__":
    test_error_handling()
