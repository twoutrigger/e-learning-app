from db import db

class VideoModel(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240))
    desc = db.Column(db.String(240))
    course_name = db.Column(db.String(80))
    video_num = db.Column(db.Integer)
    url = db.Column(db.String(80))

    def __init__(self, name, desc, course_name, video_num, url):
        self.name = name
        self.desc = desc
        self.course_name = course_name
        self.video_num = video_num
        self.url = url

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Video {self.name}>'
    
    @classmethod
    def find_by_video_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_video_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_course_num(cls, course_name, video_num):
        return cls.query.filter_by(course_name=course_name, video_num=video_num).first()