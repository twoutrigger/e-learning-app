from db import db
from models.subject import SubjectModel
from models.course import CourseModel

# add subjects
subject_1 = SubjectModel(name='Business Intelligence',
                    desc='Business intelligence courses',
                    )
subject_2 = SubjectModel(name='Data Science',
                    desc='Data science courses',
                    )
subject_3 = SubjectModel(name='Data Engineering',
                       desc='Data engineering courses',
                    )

subject_1.save_to_db()
subject_2.save_to_db()
subject_3.save_to_db()

# ERROR
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# the current application. To solve this, set up an application context
# with app.app_context(). See the documentation for more information.


# add courses; need to add relationship to Subject + update existing table
course_1 = CourseModel(name='Looker',
                    desc='Looker courses',
                    subject_name = 'Business Intelligence',
                    )
course_2 = CourseModel(name='Tableau',
                    desc='Tableau courses',
                    subject_name = 'Business Intelligence',
                    )
course_3 = CourseModel(name='Linear Regression',
                    desc='Linear Regression courses',
                    subject_name = 'Data Science',
                    )
course_4 = CourseModel(name='Logitic Regression',
                    desc='Logistic Regression courses',
                    subject_name = 'Data Science',
                    )
course_5 = CourseModel(name='Airflow',
                    desc='Airflow courses',
                    subject_name = 'Data Engineering',
                    )
course_6 = CourseModel(name='S3 Bucket',
                    desc='S3 Bucket courses',
                    subject_name = 'Data Engineering',
                    )

course_1.save_to_db()
course_2.save_to_db()
course_3.save_to_db()
course_4.save_to_db()
course_5.save_to_db()
course_6.save_to_db()