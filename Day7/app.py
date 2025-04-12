from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
content = ""
@app.route("/updatefortoday", methods=['GET', 'POST'])
def updatefortoday():
    global content
    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for(share))
    return render_template("update.html", data=content)

@app.route("/share", methods=['GET'])
def share():
    return render_template("share.html", data=content)

@app.route("/clearnotepadtxt", methods=['GET'])
def clearnotepad():
    global content
    content = ""
    return "Notepad cleared!"

if __name__ == '__main__':
    app.run()
