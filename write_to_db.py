from  app import app
from models.subjects import SubjectsModel

subj_1 = SubjectsModel(name='Business Intelligence',
                       desc='Business intelligence courses',
                       url='123')
subj_2 = SubjectsModel(name='Data Science',
                       desc='Data science courses',
                       url='234')
subj_3 = SubjectsModel(name='Data Engineering',
                       desc='Data engineering courses',
                       url='345')

subj_1.save_to_db()
subj_2.save_to_db()
subj_3.save_to_db()

# ERROR
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# the current application. To solve this, set up an application context
# with app.app_context(). See the documentation for more information.