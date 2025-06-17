import google.generativeai as genai

genai.configure(api_key="AIzaSyCUGzJ_p1W0vhUXkabKVwqT7UiO0PhRHx4")  # 🔁 Add your Gemini API key here

def get_ai_advice(info: dict) -> str:
    prompt = f"""
    I'm sharing the following resume information:

    Skills:
    {', '.join(info.get('skills', []))}

    Entities / Experience:
    {', '.join(info.get('entities', []))}

    Based on the above, give me AI-generated career suggestions.
    """
    
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
