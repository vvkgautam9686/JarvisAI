# Desktop Virtual Assistant (Jarvis) using Python & OpenAI API
This project is a voice-controlled virtual assistant similar to Alexa, built using Python. It integrates speech recognition, text-to-speech, Wikipedia search, web browsing, and AI-powered chat capabilities using the OpenAI API.

# Features
Voice Commands: Recognizes and responds to user commands via speech.
AI Chatbot: Uses OpenAI API to generate intelligent responses.
Application Control: Opens system applications like Notepad, VS Code, and Command Prompt.
Web Search & Wikipedia: Retrieves information from Wikipedia and searches the web.
Music Playback: Plays random songs from a specified music directory.
Real-Time Updates: Provides current time and interacts dynamically with the user.
# Installation & Setup
1. Clone the repository:
   git clone https://github.com/yourusername/desktop-virtual-assistant.git
2.Install dependencies:
  pip install pyttsx3 speechrecognition wikipedia pywhatkit openai
3. Add your OpenAI API key to config.py:
   apikey = "your_openai_api_key"
4. Run the assistant:
   python assistant.py
# Usage
  -> Say "open notepad", "open browser", or "play song" to perform actions.
  -> Use "According to Wikipedia..." to fetch summarized information.
  -> Say "Listen Jarvis" or "Jarvis" to chat with AI.
  -> Say "Ok Jarvis exit" to close the assistant.
# Future Enhancements
 ->  Add GUI for better user interaction.
 ->  Improve voice recognition accuracy.
 ->  Integrate with IoT devices for smart home control.
