from db import db

class SubjectModel(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    desc = db.Column(db.String(240))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Subject {self.name}>'

    @classmethod
    def find_by_subject_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_subject_id(cls, _id):
        return cls.query.filter_by(id=_id).first()