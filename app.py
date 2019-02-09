from flask import Flask, request
application = Flask(__name__)
import emojify

@application.route('/')
def viewScores():
    return """
    <html>
        <head></head>
        <body>
        <form action="api" method="post">
        <textarea width="1000" height="2000" name="text" placeholder="Type something here"></textarea>
        <button type="submit">Emojify</button>
        </form>
        </body>
        </html>
"""

@application.route('/api', methods=['POST'])
def submitScore():
    text = request.form.get('text')
    return emojify.emojify(text)
