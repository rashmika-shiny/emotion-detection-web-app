# test_emotion_detection.py
# Unit tests for emotion detection functionality

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection import emotion_detector, emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        """Test emotion detector with joy emotion"""
        # Test with a happy statement
        result = emotion_detector("I am glad this happened")
        # Should return a dictionary with emotion keys
        self.assertIsInstance(result, dict)
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_detector_anger(self):
        """Test emotion detector with anger emotion"""
        result = emotion_detector("I am really mad about this")
        # Should return a dictionary with emotion keys
        self.assertIsInstance(result, dict)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_detector_sadness(self):
        """Test emotion detector with sadness emotion"""
        result = emotion_detector("I am really sad about this")
        # Should return a dictionary with emotion keys
        self.assertIsInstance(result, dict)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_detector_fear(self):
        """Test emotion detector with fear emotion"""
        result = emotion_detector("I am really afraid about this")
        # Should return a dictionary with emotion keys
        self.assertIsInstance(result, dict)
        self.assertIn('dominant_emotion', result)
    
    def test_emotion_detector_disgust(self):
        """Test emotion detector with disgust emotion"""
        result = emotion_detector("I really hate this")
        # Should return a dictionary with emotion keys
        self.assertIsInstance(result, dict)
        self.assertIn('dominant_emotion', result)
    
    @patch('EmotionDetection.emotion_detector.requests.post')
    def test_emotion_detector_success_response(self, mock_post):
        """Test successful API response"""
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.001,
                    "disgust": 0.002,
                    "fear": 0.003,
                    "joy": 0.884,
                    "sadness": 0.110
                }
            }]
        }'''
        mock_post.return_value = mock_response
        
        result = emotion_detector("I am happy")
        
        self.assertEqual(result['anger'], 0.001)
        self.assertEqual(result['joy'], 0.884)
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_predictor_format(self):
        """Test emotion predictor output format"""
        result = emotion_predictor("I love this")
        # Should return a formatted string
        self.assertIsInstance(result, str)
        # Should contain expected phrases for valid or error responses
        self.assertTrue(
            "For the given statement, the system response is" in result or
            "Invalid text! Please try again!" in result
        )
    
    @patch('EmotionDetection.emotion_detector.requests.post')
    def test_emotion_predictor_success(self, mock_post):
        """Test emotion predictor with successful response"""
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''{
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.001,
                    "disgust": 0.002,
                    "fear": 0.003,
                    "joy": 0.884,
                    "sadness": 0.110
                }
            }]
        }'''
        mock_post.return_value = mock_response
        
        result = emotion_predictor("I am happy")
        
        self.assertIn("For the given statement, the system response is", result)
        self.assertIn("joy", result)
        self.assertIn("The dominant emotion is joy", result)
    
    def test_empty_text_handling(self):
        """Test handling of empty text"""
        result = emotion_detector("")
        # Should still return a dictionary structure
        self.assertIsInstance(result, dict)
        self.assertIn('dominant_emotion', result)

if __name__ == '__main__':
    unittest.main()
