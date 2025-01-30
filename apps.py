from flask import Flask, render_template, request
import google.generativeai as genai  

app = Flask(__name__)

genai.configure(api_key="AIzaSyB15CH4qj_uhsUrqIdV7PGedPfRt6UKzXw")  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']  
    try:
        
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")  
        
        
        response = model.generate_content(user_message)  
        
        
        chatbot_reply = response.text.strip()  
    except Exception as e:
        print(f"ERROR: {str(e)}")  
        chatbot_reply = "Sorry, I couldn't get a response. Please try again."

    return render_template('index.html', user_message=user_message, chatbot_reply=chatbot_reply)

if __name__ == "__main__":
    app.run(debug=True)
