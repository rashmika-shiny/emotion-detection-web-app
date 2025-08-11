# Emotion Detection Web Application

A comprehensive web application that analyzes emotions in text using IBM Watson NLP services and Flask web framework.

## 🚀 Features

- **Real-time Emotion Analysis**: Detects anger, disgust, fear, joy, and sadness in text
- **Web Interface**: User-friendly web form for text input
- **Error Handling**: Comprehensive error handling for invalid inputs and API failures
- **Responsive Design**: Clean, modern web interface
- **REST API**: RESTful endpoint for emotion detection

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **AI/ML**: IBM Watson NLP Emotion Analysis
- **Frontend**: HTML5, CSS3
- **HTTP Client**: Requests library
- **Testing**: Python unittest

## 📁 Project Structure

```
emotion_detection_project/
├── EmotionDetection/
│   ├── __init__.py              # Package initialization
│   └── emotion_detector.py      # Core emotion detection logic
├── server.py                    # Main Flask web server
├── server_optimized.py          # Optimized server version
├── test_emotion_detection.py    # Unit tests for emotion detection
├── test_error_handling.py       # Error handling tests
├── test_formatting.py           # Output formatting tests
├── test_optimized_server.py     # Optimized server tests
├── test_server.py              # Server functionality tests
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Flask
- Requests library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rashmika-shiny/emotion-detection-web-app.git
cd emotion-detection-web-app
```

2. Install required packages:
```bash
pip install flask requests
```

3. Run the application:
```bash
python server.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📖 Usage

### Web Interface
1. Open the application in your web browser
2. Enter text in the input field
3. Click "Analyze Emotion"
4. View the emotion analysis results

### API Endpoint
```
GET /emotionDetector?textToAnalyze=your_text_here
```

**Example Response:**
```
For the given statement, the system response is 'anger': 0.1, 'disgust': 0.05, 'fear': 0.02, 'joy': 0.8, 'sadness': 0.03. The dominant emotion is joy.
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest test_*.py
```

Or run individual test files:
```bash
python test_emotion_detection.py
python test_server.py
```

## 🔧 API Details

The application uses IBM Watson NLP Emotion Analysis service to process text and return emotion scores for:
- **Anger**: Intensity of angry emotion
- **Disgust**: Intensity of disgusted emotion  
- **Fear**: Intensity of fearful emotion
- **Joy**: Intensity of joyful emotion
- **Sadness**: Intensity of sad emotion
- **Dominant Emotion**: The emotion with the highest score

## 🛡️ Error Handling

- **Blank Input**: Handles empty or whitespace-only text
- **API Failures**: Graceful degradation when Watson API is unavailable
- **Network Issues**: Timeout and connection error handling
- **Invalid Responses**: JSON parsing error handling

## 👨‍💻 Author

**Mandapalli Rashmika**
- GitHub: [@rashmika-shiny](https://github.com/rashmika-shiny)
- Email: shinywork006@gmail.com

## 📄 License

This project is created for educational purposes as part of a course assignment.

## 🙏 Acknowledgments

- IBM Watson NLP for emotion analysis capabilities
- Flask community for the excellent web framework
- Course instructors for project guidance
