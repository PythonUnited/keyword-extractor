# Keyword extractor API

Simple API which uses[Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) 
and [multi-rake](https://github.com/vgrabovets/multi_rake) to extract keywords from 
text.

## Usage

First install the required packages and run the flask development server:

    pip install -r requirements.txt
    python api.py

Extract keywords for English text:

    curl -XGET http://localhost:5000/ -d text="Well, there's egg and bacon; egg sausage and bacon; egg and spam; egg bacon and spam; egg bacon sausage and spam; spam bacon sausage and spam; spam egg spam spam bacon and spam; spam sausage spam spam bacon spam tomato and spam;"

    [
        [
            "egg bacon sausage",
            6.466666666666667
        ],
        [
            "spam bacon sausage",
            5.9523809523809526
        ],
        [
            "egg sausage",
            4.466666666666667
        ],
        [
            "egg bacon",
            3.8
        ],
        [
            "bacon",
            2.0
        ],
        [
            "egg",
            1.8
        ],
        [
            "spam",
            1.2857142857142858
        ]
    ]

Optionally a language code can be specified, for example to extract keywords for Dutch text:

    curl -XGET http://localhost:5000/nl -d "text=Om te beginnen is er maar één bal en die moet je dus hebben, maar waar het dus in wezen om gaat, is: wat doe je met die bal?"

    [
        [
            "wezen om gaat",
            9.0
        ],
        [
            "maar \u00e9\u00e9n bal",
            7.5
        ],
        [
            "maar waar",
            4.5
        ],
        [
            "dus hebben",
            3.5
        ],
        [
            "bal",
            2.0
        ],
        [
            "dus",
            1.5
        ],
        [
            "beginnen",
            1.0
        ],
        [
            "moet",
            1.0
        ],
        [
            "doe",
            1.0
        ]
    ]

When no language code is specified the language is guessed my the `multi-rake` library:

    curl -XGET http://localhost:5000/ -d text="Aunque esa manera puede no ser obvia al principio a menos que seas holandés."
    [
        [
            "aunque",
            1.0
        ],
        [
            "manera",
            1.0
        ],
        [
            "obvia",
            1.0
        ],
        [
            "principio",
            1.0
        ],
        [
            "holand\u00e9s",
            1.0
        ]
    ]