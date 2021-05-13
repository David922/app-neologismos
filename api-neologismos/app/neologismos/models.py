from app.db import db, BaseModelMixin


class Neologism(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    neologism = db.Column(db.String)
    description = db.Column(db.String)
    source = db.Column(db.String)
    example = db.Column(db.String)
    s_term = db.Column(db.String)

    def __init__(self, neologism, description, source, example, s_term):
        self.neologism = neologism
        self.description = description
        self.source = source
        self.example = example
        self.s_term = s_term

    def __repr__(self):
        return f'Neologism({self.neologism})'

    def __str__(self):
        return f'{self.neologism}'