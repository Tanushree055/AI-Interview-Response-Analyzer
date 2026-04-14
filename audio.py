import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2.0 
    recognizer.energy_threshold = 300

    try:
        with sr.Microphone() as source:
            print("Adjusting for noise... Please wait")
            recognizer.adjust_for_ambient_noise(source,duration=1)

            print("Speak now...")
            audio=recognizer.listen(source, timeout=5, phrase_time_limit=30)
        text= recognizer.recognize_google(audio, language="en-IN")
        return text
    except sr.WaitTimeoutError:
        return "No speech detected"
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Speech service error"