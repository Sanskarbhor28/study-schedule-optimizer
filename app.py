from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# ✅ Configure your API key
genai.configure(api_key="AIzaSyB3zV6tWl5Y_ig-oSNZJt6v330aZY8Ks-g")

# ✅ Use correct model name
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
chat_session = model.start_chat(history=[])

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        subjects = request.form.get("subjects")
        hours = request.form.get("hours")
        difficulty = request.form.get("difficulty")
        exam_date = request.form.get("exam_date")

        prompt = (
            f"Create a personalized study schedule.\n"
            f"Subjects: {subjects}\n"
            f"Daily study hours: {hours}\n"
            f"Difficulty (1-10): {difficulty}\n"
            f"Exam Date: {exam_date}\n"
            f"Output should be in table format."
        )

        try:
            response = chat_session.send_message(prompt)
            result = response.text
        except Exception as e:
            result = f"❌ Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
