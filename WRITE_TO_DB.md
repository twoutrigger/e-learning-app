# Instructions on writing to data.db

Access via terminal:
1. "python db.py"
2. "flask shell"
3. "from app import db" (currently commented out)
4. "from models.\<model py> import \<model class>", i.e. "from models.course import CourseModel"
5. "db.create_all()"
6. Create a class object, i.e. "course_test = CourseModel(name='jim', desc='bob', url='test')"
7. Pass class object for validation, i.e. "course_test"
8. "db.session.add(\<class object>)", i.e. "db.session.add(course_test)"
9. Write to db, i.e. "db.session.commit()"

Other tips:
- Delete rows from SQLite - "DELETE FROM \<table> WHERE \<condition>"
- Update rows from SQLite - "UPDATE \<table> SET \<column>=\<new value> WHERE \<condition>"