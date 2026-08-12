import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
cleint = OpenAI()
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
         print("You said: ",stt)
         messages.append({"role":"user","content":stt})
         respone=cleint.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
         )
         print("AI Response: ",respone.choices[0].message.content)
main()  
        