import os
import google.genai as genai
from google.genai import types

# Configure the client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Prompt for the dragon logo
prompt = """Minimalist black and white logo of abstract dragon head, fierce fantasy dragon style, 3-5 sharp strokes, aggressive dominant look, long angular snout open mouth facing right, clean vector style thin lines, high contrast negative space, white background. Below the dragon, elegant traditional Chinese characters 龍吟. Under that, the words DRAGON ROAR in modern sans-serif font. No shading, no gradients, pure line art, premium logo design, centered composition."""

# Generate the image using the models API
response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=prompt,
    config={
        'response_modalities': ['image', 'text'],
    }
)

# Check for image in response
if response.candidates:
    for part in response.candidates[0].content.parts:
        if hasattr(part, 'inline_data') and part.inline_data:
            with open("/Users/spacefocusbot/.openclaw/dragon-logos/dragon6.png", "wb") as f:
                f.write(part.inline_data.data)
            print("Image saved to dragon6.png")
            break
    else:
        print("No inline data found. Full response:")
        print(response)
else:
    print("No candidates in response")
    print(response)
