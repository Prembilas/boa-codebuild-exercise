from flask import Flask

app = main(__name__)

@app.route('/')
def hello():
    return "Welcom to BoA Flask"

if __name__ == '__main__':
    app.run()
