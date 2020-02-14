from flask import Flask, request
from flask_restful import Resource, Api

from multi_rake import Rake


app = Flask(__name__)
api = Api(app)


class KeywordExtractor(Resource):
    def get(self, language_code=None):
        rake = Rake(language_code=language_code)

        return rake.apply(request.form.get('text'))


api.add_resource(KeywordExtractor, 
                 '/',
                 '/<string:language_code>')

if __name__ == '__main__':
    app.run(debug=True)
