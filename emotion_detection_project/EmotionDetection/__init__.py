# EmotionDetection package
__version__ = "1.0.0"

# Import the main functions to make them available at package level
from .emotion_detector import emotion_detector, emotion_predictor

# Make functions available when importing the package
__all__ = ['emotion_detector', 'emotion_predictor']
