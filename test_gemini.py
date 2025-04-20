import google.generativeai as genai

# ✅ Set your API key
genai.configure(api_key="AIzaSyB3zV6tWl5Y_ig-oSNZJt6v330aZY8Ks-g")

# ✅ Use correct model (gemini-1.5-pro or gemini-pro)
model = genai.GenerativeModel("gemini-1.5-pro")

response = model.generate_content("Give me a weekly study plan for 3 subjects in table format.")
print(response.text)
