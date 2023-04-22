from db import db

class CourseModel(db.Model):
    __tablename__ = 'course'

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

    def __repr__(self):
        return f'<Course {self.name}>'
    
    @classmethod
    def find_by_course_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_course_id(cls, _id):
        return cls.query.filter_by(id=_id).first()