"""
Flask web server for emotion detection application.

This module provides a web interface for analyzing emotions in text using
the Watson NLP emotion detection service.
"""

from flask import Flask, request
from EmotionDetection import emotion_predictor

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page with emotion detection form."""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emotion Detection Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
            }
            input[type="text"] {
                width: 70%;
                padding: 10px;
                font-size: 16px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007cba;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #005a87;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                background-color: #f0f8ff;
                border: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Emotion Detection Application</h1>
            <p>Welcome to the emotion detection service! Enter some text
               below to analyze its emotional content.</p>

            <form action="/emotionDetector" method="GET">
                <label for="textToAnalyze">Text to analyze:</label><br><br>
                <input type="text" id="textToAnalyze" name="textToAnalyze"
                       placeholder="Enter text here..." required><br><br>
                <button type="submit">Analyze Emotion</button>
            </form>
        </div>
    </body>
    </html>
    '''


@app.route('/emotionDetector')
def emotion_detection():
    """Emotion detection endpoint with comprehensive error handling."""
    # Get the text from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text is provided and not blank
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return error message for blank input
        return create_error_page(
            "Invalid Input Error",
            "Invalid text! Please try again!",
            "Please provide some text to analyze. Empty or blank text "
            "cannot be processed.",
            "#ffe6e6",
            "#ff9999",
            "#cc0000"
        )

    # Get emotion analysis using our emotion_predictor function
    result = emotion_predictor(text_to_analyze)

    # Check if the result indicates an error (Invalid text)
    if "Invalid text! Please try again!" in result:
        # Return formatted error page for invalid text
        return create_error_page(
            "Analysis Error",
            result,
            "The text could not be processed due to API connectivity "
            "issues or invalid content. Please check your input and "
            "try again.",
            "#fff3cd",
            "#ffeaa7",
            "#856404",
            text_to_analyze
        )

    # If we get here, we have a successful result
    return create_success_page(text_to_analyze, result)


def create_error_page(title, error_message, description, bg_color,
                      border_color, text_color, analyzed_text=None):
    """Create a formatted error page."""
    analyzed_text_html = ""
    if analyzed_text:
        analyzed_text_html = (
            f'<p><strong>Analyzed Text:</strong> "{analyzed_text}"</p>'
        )

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title} - Emotion Detection</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
            }}
            .error {{
                margin-top: 20px;
                padding: 15px;
                background-color: {bg_color};
                border: 1px solid {border_color};
                border-radius: 5px;
                color: {text_color};
            }}
            .back-link {{
                margin-top: 20px;
            }}
            .back-link a {{
                color: #007cba;
                text-decoration: none;
            }}
            .back-link a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{title}</h1>
            {analyzed_text_html}

            <div class="error">
                <h3>⚠️ Error:</h3>
                <p><strong>{error_message}</strong></p>
                <p>{description}</p>
            </div>

            <div class="back-link">
                <a href="/">&larr; Go Back and Try Again</a>
            </div>
        </div>
    </body>
    </html>
    '''


def create_success_page(text_to_analyze, result):
    """Create a formatted success page."""
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Emotion Analysis Result</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
            }}
            .result {{
                margin-top: 20px;
                padding: 15px;
                background-color: #f0f8ff;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}
            .back-link {{
                margin-top: 20px;
            }}
            .back-link a {{
                color: #007cba;
                text-decoration: none;
            }}
            .back-link a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Emotion Analysis Result</h1>
            <p><strong>Analyzed Text:</strong> "{text_to_analyze}"</p>

            <div class="result">
                <h3>Analysis Result:</h3>
                <p>{result}</p>
            </div>

            <div class="back-link">
                <a href="/">&larr; Analyze Another Text</a>
            </div>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
