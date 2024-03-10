from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

page_name = "Home"

@app.route('/')
def hello_world():
  return render_template('home.html', page_name=page_name)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
