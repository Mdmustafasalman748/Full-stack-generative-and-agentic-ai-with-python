import speech_recognition as sr
def main():
    r = sr.Recognizer() #Speech to text
    with sr.Microphone as source: #Mic access
        r.adjust_for_ambient_noise(source) #Adjust for noise
        r.pause_threshold=2 
        SYSTEM_PROMPT=f"""
        You're an expert voice agent. YOu are rgiven the transcript of what user had said usng voice. You need to output as if you are an voice agent and whatever you speak will converted back to audio using AI and played back to user. You need to output only the text that you will speak back to user. Do not output anything else.
        """
        messages=[
            {"role":"system","content":SYSTEM_PROMPT}
        ]
        while(True):
         print("Speak Something: ")
         audio=r.listen(source) #Listen to user
         print("Processing audio...(STT)") 
         stt=r.recognize_google(audio) #Convert audio to text
         messages.append({"role":"user","content":stt})
main()  
        