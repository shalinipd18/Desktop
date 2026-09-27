import random

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  Run: pip install pyttsx3")


def setup_tts():
    """Check that text-to-speech is available (used once at startup)"""
    if not TTS_AVAILABLE:
        return None
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)
        return engine
    except Exception:
        return None


def speak(engine, text):
    """Speak text or show fallback.
    Note: creates a fresh engine internally each call, since reusing
    one pyttsx3 engine across multiple runAndWait() calls causes it
    to go silent after the first utterance on many systems.
    """
    if engine:
        try:
            fresh_engine = pyttsx3.init()
            fresh_engine.setProperty("rate", 150)
            fresh_engine.setProperty("volume", 0.9)
            fresh_engine.say(text)
            fresh_engine.runAndWait()
            fresh_engine.stop()
            del fresh_engine
        except Exception:
            print(f"🔊 [AUDIO]: {text}")
    else:
        print(f"🔊 [AUDIO]: {text}")


def get_samples():
    """Fun phrases to try"""
    return [
        "Hello! I am your computer!",
        "Python is awesome!",
        "This is AI speaking!",
        "Welcome to the future!",
    ]


def main():
    print("🤖 AI VOICE LAB")
    print("===============")

    engine = setup_tts()

    if engine:
        print("✅ Voice ready! Try typing something...")
    else:
        print("⚠️  No audio, but you can still learn!")

    speak(engine, "Hello! Type something for me to say!")

    while True:
        text = input("\n👤 You: ").strip()

        if text.lower() == 'exit':
            speak(engine, "Goodbye!")
            break
        elif text.lower() == 'sample':
            phrase = random.choice(get_samples())
            print(f"💬 {phrase}")
            speak(engine, phrase)
        elif text == "":
            print("💡 Type 'sample' for ideas or 'exit' to quit")
        else:
            speak(engine, text)
        

if __name__ == "__main__":
    main()