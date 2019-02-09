from flask import Flask, request
app = Flask(__name__)
import emojify

@app.route('/create')
def viewScores():
    return """
    <html>
        <head></head>
        <body>
        <form action="api" method="post">
        <textarea name="text" placeholder="Type something here"></textarea>
        <button type="submit">Emojify</button>
        </form>
        </body>
        </html>
"""

@app.route('/api', methods=['POST'])
def submitScore():
    text = request.form.get('text')
    return emojify.emojify(text)
