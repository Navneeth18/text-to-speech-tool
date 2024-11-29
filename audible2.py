import pyttsx3
import time

# initializing the global variables
engine = pyttsx3.init()


# say function in specific language, as of now multiple languages are not supported.
def say_in_language(text, voice_id):
    engine1 = pyttsx3.init()
    engine1.setProperty('voice', voice_id)
    engine1.say(text)
    engine1.runAndWait()
# say function that is takes the text(string) and outputs the voice.
def say(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5) #controls the speed of the output voice

def get_voice_id(language_code):
    voices = engine.getProperty('voices')
    for voice in voices:
        if language_code in voice.languages or language_code in voice.id:
            return voice.id
    return None

def textToSpeech(file_path,voice_id):
    try:
        print("reading the file")
        say("reading the file...")
        with open(file_path,"r", encoding="utf-8") as f:
            content = f.read()
            say_in_language(content,voice_id)
    except FileNotFoundError:
        engine.say("File not found, please provide a valid file path")
        print("Error: File not found. Please provide a valid file path.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        engine.say("Sorry!, from my side, error in reading the file")

if __name__ == '__main__':
    print("welcome to audible - a text to speech tool")
    say("welcome to audible, a text to speech tool")
   
    say("Enter the path to your text file")
    # file_path = input("Enter the path to your text file: ").strip()  #to take the input from user
    file_path = "./song.txt" #giving it a sample text file.
    print("1- English\n2- Hindi\n3- Telugu")
    print("select language: ")
    say("select language")
    try:
        ch = int(input("Select a language (1/2/3): "))
        if ch == 1:
            voice_id = get_voice_id('en')
            textToSpeech(file_path, voice_id)
        elif ch == 2:
            voice_id = get_voice_id('hi')
            textToSpeech(file_path, voice_id)
        elif ch == 3:
            voice_id = get_voice_id('te')
            textToSpeech(file_path, voice_id)
        else:
            raise ValueError("Invalid input")
        
        if not voice_id:
            print("Selected language voice is not available. Falling back to default.")
            say("Selected language voice is not available. Falling back to default.")
            voice_id = get_voice_id('en')
            textToSpeech(file_path, voice_id)
    except ValueError:
        print("Invalid input. Using English as the default language.")
        say("Invalid input. Using English as the default language.")
        voice_id = get_voice_id('en')
        textToSpeech(file_path, voice_id)



    