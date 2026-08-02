from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI()
client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
        "role":"user",
        "content":[
            {"type":"text","text":"Generate a captio for this image"},
            {"type":"image","image_url":"https://iamges.pexels.com/photos/879109/pexels-photo-879109.jpeg"}
            ]
        }
    ]
)