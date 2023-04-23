# Instructions on writing to data.db

Access via terminal:
1. "flask shell"
2. "from app import db"
3. "from models.<model py> import <model class>", i.e. "from models.course import CourseModel"
4. "db.create_all()"
5. Create a class object, i.e. "course_test = CourseModel(name='jim', desc='bob', url='test')"
6. Pass class object for validation, i.e. "course_test"
7. "db.session.add(<class object>)", i.e. "db.session.add(course_test)"
8. Write to db, i.e. "db.session.commit()"