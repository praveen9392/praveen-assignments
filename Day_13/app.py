from flask import Flask, request, render_template, url_for, session,redirect
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage
app = Flask(__name__)

app.secret_key = 'chj123hjha12345lama' 
chat_history = [] 

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username =="Praveen" and password=="gtk1234gh56":
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("home"))
        return render_template("login.html", error="Invalid credentials!")
    
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    result = ""
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    if request.method == "POST":
        query = request.form.get("query")
        format_expected = request.form.get("format")
        response = agent(query,format_expected)
        chat_history.insert(0, {"user": query, "bot": response}) 
        result = response
    return render_template("index.html", result=result, history=chat_history)

def agent(query,format_expected):
    model = ChatMistralAI(model="open-mistral-nemo", temperature=0, max_retries=2)
    messages = [
        SystemMessage(f"Give the answer {format_expected} in natural language"),
        HumanMessage(query)
    ]
    response = model.invoke(messages)
    return response.content

@app.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
