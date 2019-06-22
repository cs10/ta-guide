# TA Guide
This is a guide for all CS10 TAs/Head TAs!

- [TA Guide](#ta-guide)
  * [Pre-Semester Prep](#pre-semester-prep)
  * [First-Week Prep](#first-week-prep)
  * [Academic Intern Management](#academic-intern-management)
  * [Key Contacts](#key-contacts)
  * [Alonzo](#alonzo)
  * [Publishing Assignments](#publishing-assignments)
  * [End-of-Semester](#end-of-semester)
  * [Reimbursements](#reimbursements)
  * [Extension Policy](#extension-policy)


## Pre-Semester Prep
### Course Website
Here are some tasks you'll need to do before starting on the website:
* Figure out the course calendar. Be sure to run this by the professor before adding it to the website
* Update the syllabus.

Below are the tasks you'll need to do to create the new semester's course website:
* Make a new website repo in the cs10 org on Github. Create a new, blank, private repository on Github titled with the semester and year (ex: su19) and then mirror push from the previous semester's repository.
* In `bjc-r/course`, create a new lab page for the semester (like [this](https://beautyjoy.github.io/bjc-r/course/cs10_fa18.html)). You can just copy a previous semester’s and update the order of the labs for this. Be sure to name it consistently with the ones from previous semesters!
* To get the labs, discussions, and lectures on the weekly schedule, go to the appropriate Google Calendars and add the sections. They will automatically populate the weekly schedule. If you do not have access to these, ping a previous Head TA.
* To automatically route to the new semester, update [this file](https://github.com/cs10/cs10.github.io/blob/master/index.html)

### New Staff Emails
To give new TAs cs10 emails, go to the CS10 Google Domain and under emails, add the new email aliases. Sometimes, the email aliases don't work with Berkeley emails, so you can route them to personal Gmail accounts instead. You do need special permissions to access the Google Domain, so talk to a previous Head TA if you need it.

### Keycard Access
Students get keycard access to the lab automatically, but we need to ask explicitly for keycard access for TAs, Readers, and Academic Interns. 

In order to get keycard access, email [Kevin Mullally](mailto:kevinm@berkeley.edu) with names, SIDs, and proxies (the first set of digits on the back of student IDs) for everyone needing keycard access. **This should be done at least a week before the semester starts, since UCPD only processes requests every Thursday.**

### Pre-Semester Meeting
Be sure to schedule a pre-semester meeting with the staff. This is usually done a couple days before the semester starts. Here are some things usually covered:
* Changes to syllabus/course policies
* TA/Reader responsibilities
* How to book rooms
* TA Homework assignment responsibilities
* How to write reading quizzes

### Academic Intern Set Up
Before doing any of the following, please go through the interest form and make sure that everyone who filled it out received at least a B- in CS10. Students who did not get at least a B- are not elligible to serve as an academic intern. 

#### Syllabus
Edit the Academic Intern syllabus with information about: 
* Units/Responsibilities
* Meetings/Make Ups
* Checkoff instructions
* Contact information
* Extra opportunities

#### Units
During the normal semester, 1-unit Academic Interns are required to work 3 hours/week and 2-unit Academic Interns are required to work 6 hours/week. In the summer, those values are doubled.

#### Contract
Once you've updated the Academic Intern syllabus, email all eligible Lab Assistant candidates with a contract form, asking for the following information: 
* How many units they'd like
* Their availability
* Some confirmation that they've read the syllabus (in the past, we've included a secret word on the syllabus that they need to fill out)
* Their ID number/proxy

In the same email, you should also send out the [Academic Intern guide](https://docs.google.com/document/d/1LNuCs9S1jfghuKfYeFGz8mDVZmfoucWSMl-k7jRPlJ4/edit?usp=sharing) to serve as a guide for Academic Interning.

#### Piazza/Checkoff Room
Once interested students have filled out the Academic Intern contract, you may add them to an Academic Intern Piazza and to the LA Checkoff Room on Slack. You can only do the latter if you have Admin access on Slack, so be sure to ask a previous Head TA to give it to you if you don't have it!

#### Scheduling
You may use the script `scripts/AIAssigner.py` to assign sections to Lab Assistants. Instructions on usage are on the script.

#### Pre-Semester Meeting and Bonding
Schedule a pre-semester Academic Intern meeting and a separate bonding section (booking the Woz is best for bonding). 

During the pre-semester meeting, things you may go over include:
* Rules/logisitcs
* Tips from the AI Guide
* General teaching/debugging strategies

The professor usually leads bonding, so make sure they're free for it!

### Section Scheduling
After getting staff availability, we've usually assigned sections by hand. If you have enough staff to, try to pair new TAs with veteran TAs for lab sections. You may also try using the script `scripts/AIAssigner.py` and adapt it to this purpose.

### Scheduling OH Rooms
If possible, try to schedule some rooms for office hours before the semester starts. Rooms are in high-demand, and it's often hard to get a good room once the semester begins. 

TAs/classes are only allowed to book office hours in the Alcoves in Soda (283, 341A/B, 411, 611, 651). We are also allowed to hold office hours in 200 SD, though we aren't allowed to officially book the room. To hold office hours in 200SD, just make sure no other classes are using the room (UCBUGG and CNM share the room with us usually) and add it to our caldendar.

### Configuring Alonzo
#### Updating Assignments
In [`bcourses-config.js`](https://github.com/cs10/Alonzo/blob/master/scripts/cs10/bcourses-config.js), update the following variables (comments on the file explains what these variables are):
* `cs10.courseID`
* `cs10.labsID`
* `cs10.START_DATE`
* `cs10.TA_EMAILS` (not entirely sure if this is needed, but it's a good idea to fill it out just in case)
* `cs10.LAB_ASSISTANT_MANAGER`
* Assignment IDs
* Help Links

Be sure to also double check the other variables to make sure they're accurate. 

In order to push your changes, you will need to [push to Heroku](https://devcenter.heroku.com/articles/git#deploying-code).

#### Updating Canvas API Key (if necessary)
You may need to update the Canvas API Key on [Heroku](https://dashboard.heroku.com/apps/alonzo) (this can be found at Settings → HUBOT CANVAS KEY). To set a new Canvas API Key, go to bCourses → Account → Settings → Create a new Access Token (Purpose: Alonzo and set an expiration date).

#### Update Roles on Slack
There are two roles on Slack, tas and readers (roles are used when you @tas or @readers). 

To assign someone to the tas/readers role (example shown for tas), message Alonzo with the following:
`<username> has tas role`

Similarly, to remove someone from the tas/readers role (example shown for tas), message Alonzo with the following:
`<username> does not have tas role`

To check who has a certain role, you can message Alonzo with the following:
`who has tas role`

Slack does not show usernames for users by default. Usually, you can figure out a user's username just by @ing them, but if you can't find it, you can message Alonzo `show users` and Alonzo will list all users and their usernames. 

You will need to be a collaborator on Heroku to update roles on Slack. An existing collaborator can make you a collaborator to the Alonzo project if needed. 

## First-Week Prep
### Teaching Your First Section
### Scheduling Exam/Review Session Rooms

## Academic Intern Management

## Key Contacts

## Alonzo

## Assignments
### Publishing Assignments
### Extension Policy

## Exam Scanning

## Reimbursements

## End-of-Semester
### Grades
#### EPA
