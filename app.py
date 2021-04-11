from flask import Flask

app = Flask("app_name")

@app.route('/test/<name>')
def get(name):
    return 'Hello %s!' %(name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9080, debug=True)