# Structure of project

Things that the app needs:
- home page
- subjects page - returns a list of subjects
- subject page - returns a list of courses per subject
- course page - returns a list of videos per course. Shows progress per course
- video page - allows the user to watch a video, or select next / last video
- User page - returns all courses watched, and progress of each course. Maybe recommendations


Class variables:
- course (a collection of videos) - tracks progress, completion, course meta data
- video - tracks progress, completion, video url, video meta data
- user (consumer of courses) - videos and courses clicked on / completed
- subject (a collection of courses) - subject meta data