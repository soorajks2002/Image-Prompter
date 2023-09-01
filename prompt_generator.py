import openai
from api_key import open_ai_api_key

openai.api_key = open_ai_api_key

def generate_prompt (keywords) :
    
    prompt = "write an image prompt for DALL-E using these words {keywords}"

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "write an image prompt for DALL-E using these words [human, bike, bottle]"},
                {"role": "assistant", "content": "Generate an image of a human riding a bicycle while holding a water bottle."},
                {"role": "user", "content": prompt.format(keywords=keywords)}
            ]
        )

    return response["choices"][0]["message"]["content"]