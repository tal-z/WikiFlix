from flask import Flask, Response, render_template
from frames_generator import screenshots

app = Flask(__name__)

@app.route('/')
def index():
    print("hit route")
    # Return the result on the web
    return Response('hello world')


@app.route('/wiki_feed')
def wiki_feed():
    # Return the result on the web
    return Response(screenshots('Little Red Lighthouse'),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
