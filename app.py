from flask import Flask, request
application = Flask(__name__)
import emojify

@application.route('/')
def viewScores():
    return """
    <!doctype html>
        <head><title>Make ur text emoji</title></head>
        <body>
        <form action="api" method="post">
        <textarea style="width:1000; height:800" name="text" placeholder="Type something here"></textarea>
        <button type="submit">Emojify</button>
        </form>
        </body>
        </html>
"""

@application.route('/api', methods=['POST'])
def submitScore():
    text = request.form.get('text')
    return emojify.emojify(text)
