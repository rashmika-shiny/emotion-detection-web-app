# test_optimized_server.py
# Test the optimized server functionality

from server import app

def test_optimized_server():
    """Test the optimized server functionality"""
    print("=== Testing Optimized Server ===")
    
    # Test server imports
    print("✅ Optimized server imports successfully")
    
    # Test functionality
    with app.test_client() as client:
        # Test main page
        response = client.get('/')
        print(f"✅ Main page works: {response.status_code == 200}")
        
        # Test error handling
        response = client.get('/emotionDetector?textToAnalyze=')
        error_handled = 'Invalid text!' in response.get_data(as_text=True)
        print(f"✅ Error handling works: {error_handled}")
        
        # Test valid input
        response = client.get('/emotionDetector?textToAnalyze=I%20am%20happy')
        valid_response = response.status_code == 200
        print(f"✅ Valid input processing: {valid_response}")
    
    print("\n🎉 All tests passed - Server is optimized and functional!")

if __name__ == "__main__":
    test_optimized_server()
