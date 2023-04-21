from db import db

class SubjectsModel(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    desc = db.Column(db.String(240))
    url = db.Column(db.String(80))

    def __init__(self, name, desc, url):
        self.name = name
        self.desc = desc
        self.url = url

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_subject_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_subject_id(cls, _id):
        return cls.query.filter_by(id=_id).first()