from db import db
from models.subject import SubjectModel
from models.course import CourseModel
from models.video import VideoModel

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


# add videos
video_1 = VideoModel(name='Looker Studio in a minute',
                  desc='Looker Studio helps make it easy for everyone to do self-service analytics and data visualization.',
                  course_name = 'Looker',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/ZBoFvaWr-Dk'
                  )
video_2 = VideoModel(name='Look & Learn - Viewing dashboards',
                  desc='In Looker, dashboards are collections of saved tiles representing individual data queries.',
                  course_name = 'Looker',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/mTlW_WDq2r4'
                  )
video_3 = VideoModel(name='What is Tableau ? Explained in under 10 mins!',
                  desc='In this video I summarise the Tableau platform and how it fits into the Analytical flow in every business.',
                  course_name = 'Tableau',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/7Jl-RwkzqQ4'
                  )
video_4 = VideoModel(name='Tableau for Data Science and Data Visualization - Crash Course Tutorial',
                  desc='Learn to use Tableau to produce high quality, interactive data visualizations!',
                  course_name = 'Tableau',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/TPMlZxRRaBQ'
                  )
video_5 = VideoModel(name='',
                  desc='',
                  course_name = 'Linear Regression',
                  video_num = 1,
                  url = ''
                  )
video_6 = VideoModel(name='',
                  desc='',
                  course_name = 'Linear Regression',
                  video_num = 2,
                  url = ''
                  )
video_7 = VideoModel(name='',
                  desc='',
                  course_name = 'Logitic Regression',
                  video_num = 1,
                  url = ''
                  )
video_8 = VideoModel(name='',
                  desc='',
                  course_name = 'Logitic Regression',
                  video_num = 2,
                  url = ''
                  )
video_9 = VideoModel(name='',
                  desc='',
                  course_name = 'Airflow',
                  video_num = 1,
                  url = ''
                  )
video_10 = VideoModel(name='',
                  desc='',
                  course_name = 'Airflow',
                  video_num = 2,
                  url = ''
                  )
video_11 = VideoModel(name='',
                  desc='',
                  course_name = 'S3 Bucket',
                  video_num = 1,
                  url = ''
                  )
video_12 = VideoModel(name='',
                  desc='',
                  course_name = 'S3 Bucket',
                  video_num = 2,
                  url = ''
                  )
