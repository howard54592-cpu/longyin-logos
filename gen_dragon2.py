import os
import requests
import json

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp-image-generation:generateContent?key={GOOGLE_API_KEY}"

prompt = "abstract dragon head logo black white fierce minimal"

data = {
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {
        "responseModalities": ["image", "text"]
    }
}

try:
    response = requests.post(url, json=data, timeout=30)
    print("Status:", response.status_code)
    if response.status_code == 200:
        result = response.json()
        print("Response keys:", result.keys())
        # Try to extract image
        if 'candidates' in result:
            for candidate in result.get('candidates', []):
                for part in candidate.get('content', {}).get('parts', []):
                    if 'inlineData' in part:
                        import base64
                        img_data = base64.b64decode(part['inlineData']['data'])
                        with open("/Users/spacefocusbot/.openclaw/dragon-logos/dragon6.png", "wb") as f:
                            f.write(img_data)
                        print("Image saved!")
                        break
    else:
        print(response.text[:500])
except Exception as e:
    print("Error:", e)
