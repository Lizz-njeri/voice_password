import speech_recognition as sr

# Function to capture and enroll the voice password as text
def enroll_voice_password():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say your password.")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        # Recognize the spoken password using Google Speech Recognition
        password = r.recognize_google(audio, language='en-in')
        print(f"Password enrolled: {password}")
        return password
    except Exception as e:
        print("Could not understand your password, please try again.")
        return None

# Function to capture the voice for authentication
def capture_voice_for_authentication():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say your password for authentication.")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        # Recognize the spoken password using Google Speech Recognition
        spoken_password = r.recognize_google(audio, language='en-in')
        print(f"User said: {spoken_password}")
        return spoken_password
    except Exception as e:
        print("Unable to recognize your voice.")
        return None

# Function to compare the enrolled password with the spoken password
def compare_passwords(enrolled_password):
    # Capture what the user says during authentication
    spoken_password = capture_voice_for_authentication()
    
    # Compare the enrolled password with the spoken password
    if spoken_password and spoken_password.lower() == enrolled_password.lower():
        print("Password match! Access granted.")
    else:
        print("Password does not match. Access denied.")

if __name__ == "__main__":
    # Step 1: Enroll the password (spoken by the user)
    enrolled_password = enroll_voice_password()

    if enrolled_password:
        # Step 2: Authenticate by comparing live input to the enrolled password
        compare_passwords(enrolled_password)
