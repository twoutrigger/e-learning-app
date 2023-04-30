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

# add courses
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
video_5 = VideoModel(name='Linear Regression in 2 minutes',
                  desc='Linear Regression in 2 minutes',
                  course_name = 'Linear Regression',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/CtsRRUddV2s'
                  )
video_6 = VideoModel(name='Linear Regression, Clearly Explained!!!',
                  desc='The concepts behind linear regression, fitting a line to data with least squares and R-squared, are pretty darn simple!',
                  course_name = 'Linear Regression',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/7ArmBVF2dCs'
                  )
video_7 = VideoModel(name='Logistic Regression: An Introduction',
                  desc='What is a logistic regression?',
                  course_name = 'Logistic Regression',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/3tq4t41MsPc'
                  )
video_8 = VideoModel(name='StatQuest: Logistic Regression',
                  desc='Logistic regression is a traditional statistics technique that is also very popular as a machine learning tool.',
                  course_name = 'Logistic Regression',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/yIYKR4sgzI8'
                  )
video_9 = VideoModel(name='1. What is Apache Airflow? Airflow Beginners Tutorial',
                  desc='Apache Airflow is one of the most powerful platforms used by Data Engineers for orchestrating workflows.',
                  course_name = 'Airflow',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/4aB1NE6qQzs'
                  )
video_10 = VideoModel(name='Dynamic DAGs in Apache Airflow for Advanced',
                  desc='Dynamic DAGs in Apache Airflow for beginners👍',
                  course_name = 'Airflow',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/6eHuOd96unQ'
                  )
video_11 = VideoModel(name='Getting started with Amazon S3 - Demo',
                  desc='In this demo, we learn how to create and configure S3 buckets.',
                  course_name = 'S3 Bucket',
                  video_num = 1,
                  url = 'https://www.youtube.com/embed/e6w9LwZJFIA'
                  )
video_12 = VideoModel(name='All you need to know about encrypting AWS S3 buckets',
                  desc='Learn how to enable S3 default encryption.',
                  course_name = 'S3 Bucket',
                  video_num = 2,
                  url = 'https://www.youtube.com/embed/SHWcTPcp8As'
                  )


# ERROR WHEN WRITING TO DB VIA FLASK SHELL:
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# the current application. To solve this, set up an application context
# with app.app_context(). See the documentation for more information.