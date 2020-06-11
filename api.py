from flask import Flask, request
from flask_restful import Resource, Api

from multi_rake import Rake


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(
        KeywordExtractor,
        '/',
        '/<string:language_code>'
    )
    return app


class KeywordExtractor(Resource):
    def get(self, language_code=None):
        rake = Rake(language_code=language_code)

        text = request.form.get('text')
        if text:
            return rake.apply(text)

        return 'No text given', 400


if __name__ == '__main__':
    app = create_app()
    app.run(host ='0.0.0.0', debug=True)
