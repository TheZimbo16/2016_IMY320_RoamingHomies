# 2016_IMY320_RoamingHomies
IMY 320 Project 2016

Hosted at: http://lethalpapercut.pythonanywhere.com

Table of Contents
Website Link	2
Team Members	3
1.	Project Background and Description	3
2.	Design choices for the website	4
3.	Software Choices	7
4.	Security	7
5.	High-Level Requirements	8
6.	Specific Exclusions from Scope	8
7.	Affected Parties	9
8.	Implementation	9
9.	Borrowed APIs	9
REFERENCES	10


 
Website Link

http://lethalpapercut.pythonanywhere.com
We struggled to find a free webserver that had Django already installed and so eventually settled on PythonAnyWhere webserver. 
ROAMING HOMIES
PROJECT READ ME
October 14, 2016

Team Members
DREW LANGLEY 11039753
SCHAE IND 14058104
VUKILE LANGA 14035449
GEROME SCHUTTE 12031519
ESTIAN ROSSLEE 12223426
HUGO MEIRING 13230795
ALFI OLOO 14201692
Our team was made up of seven people, all working together on the front-end, back-end and integration thereof. Our team worked well together and produced a functional and attractive website that we can be proud of. Our strengths lay in having three multimedia students and four computer science students, therefore allowing us to combine our knowledge and skills in to the Roaming Homes website and app.

1.	Project Background and Description
As a NPO, our team came up with the concept of the Roaming Homes, a bus service for homeless and underprivileged people who need shelter. This shelter is in the form of repurposed buses which travel to various destinations in the Johannesburg area during to allow the people to collect food that has been donated to the organization, as well as have a shower and sleep on one of the bunk beds offered on the bus. 
Our task is to create a supporting website and mobile application so that people looking to help out and the team of the Roaming Homes initiative can effectively communicate and handle administrative matters, as well as provide a means for them to publicize news and their efforts and to spread awareness of their many events and programs. The website will allow those interested in helping or donating communicate with members of the Roaming Homes team.
 
2.	Design choices for the website
Our team chose a simple design for this website as it needs to be uncluttered and simple to navigate. Due to the nature of the website, the content is limited and thus allows for a clean and simple design. 
A hero image was used on the homepage in order to immediately set the tone for the website – serious, well maintaining a sense of class and integrity – as well as visually captivate the user. The background images are all black and white for simplicity and uniformity and, contain content that alludes to homeless South Africans or the city of Johannesburg. Good quality photos were chosen to ensure the website contained an air of professionalism.
South African colours were, for the most part, not used in our website as they do not work well together and would have made it very difficult to keep our website simple. Instead, we opted for a simple background image that shows a hand drawn picture of the Johannesburg city skyline with a light blue and red accents. We allowed for the South African theme to show in our website through our hero image and background images, rather than the colours. The South African flag is, however, represented in slightly lighter tones when the menu button is clicked.
The drawn image of the Johannesburg city skyline is artistic without being too stiff and formal as to make our organization seem like a bank. The simple colours tie in with our theme and allow the background image to be an unobtrusive nod to the home city of our organization
 
 

Our logo for Roaming Homes is a bus with a roof, describing what our Non-Profit Organization is all about – Offering a roaming home to those in need. The name Roaming Homes is included in the navigation bar at the top of each page so that the user always knows what website they are on.
  
We chose three fonts to use on this website, a large, bold heading font and a smaller, serif subheading font and, a sans-serif body font, for clear readability.
	Body Font: Montserrat
	Heading Font: Nanami
	Sub-heading Font: Roboto 
A burger menu was used for navigation within our horizontal static nav-bar. The burger menu allows for our website to stay simple and uncluttered, it is also easy to add more navigation links without compromising the style of the navigation bar. Our login and Register links remain in the navigation bar, regardless of which subpage you are on, so that the user is always able to easily login or register from any page.
Our main content is kept in slightly transparent white containers, so as to stand out and be easily read against the background, without obscuring the background picture, which would have been the result had the containers been opaque.
 
Our forms for login and registration are kept minimal, so as to not bombard the user with unnecessary fields to fill in. They are simple and straight-forward as to keep with our simple design and thus make the website usable and user-friendly. 
3.	Software Choices
Front-end:
For the front-end of our website we used HTML5 to create the content and CSS for the styling of the website. We chose these for their simplicity and effectiveness in creating an attractive and usable website. The styling of the website allowed us to make it user-friendly, as well as usable.
Back-end:
For the back-end Python Django was decided upon as the framework, as it provides a lot of functionality, such as URL routing, user authentication, an admin interface, object modelling to extract from the database, and templating, which allows one to construct web pages from multiple html files and thus make maintenance and reuse of code easier. The latest version of Django posed a problem in terms of our use of the Google Calendar API, thus forcing us to use a slightly older version of Django.
Initially, our plan was to use MongoDB but we encountered problems when we tried to use it in conjunction with Django. We used MySQL as our chose database as it is simple to work with in terms of accessing the database. 

4.	Security
Security measures were taken in our coding of the back-end to ensure that our website is safe and secure against the entry-level hacker or a person randomly clicking and pushing keys on our website. Django comes with built-in security and security measures, therefore ensuring our websites safety and thus, being a more effective option than PHP.
 

5.	High-Level Requirements
 
The new system includes the following (Given by the client):
For the Website:
•	A front page for news, stories and events
•	An about page and an area to get contact information or contact forms
•	A calendar system to show upcoming events and what is planned
•	Administrative staff should be able to edit and create posts to display on the website and in the app
•	Login system for Roaming Homes members
•	Means of storing documents and files.

For the app:
•	Login System for members
•	A means of reflecting the content from the website, such as news.
•	An announcement function to spread news to all those involved quickly and effectively.
•	A calendar system similar to that of the website.

6.	Specific Exclusions from Scope
It was noted that some features were not required such as:
•	An image gallery for the website
•	A chat function for the mobile app.
 
7.	Affected Parties
The following peoples will be directly affected by use and implementation of the Roaming Homies system.
•	General Public
•	Homeless people
•	Roaming Homes team and following

8.	Implementation
By using a combination of the Agile and Parallel Tracks development methods we were able to ensure that the project is completed on time and the products created comply with standards. By making use of already existing systems such as the Google Calendar API for the calendar and JavaScript libraries for the login system and contact forms or pages, we can create beautiful working systems easily and effectively.
9.	Borrowed APIs
Our team made use of the google calendar API, as we were advised to make use of the resources we were able to find online. Although the Google Calendar initially caused problems with implementation, the problems were able to be resolved to allow for a fully functional calendar and event-making webpage.

 
REFERENCES
Bester, D. (n.d.). Nkululeko | Portrait Study of a Homeless Man. Nkululeko. Fine Art Street Photography, Johannesburg.
Google Developers. (2016, October). Calendar API. Retrieved from Google Calendar API: https://developers.google.com/google-apps/calendar/
Slabbert, M. (n.d.). jozi-skyline. jozi-skyline. Morris Slabbert Designs, Johannesburg.
Various. (2016, October). Flag of South Africa. Retrieved from Wikipedia: https://en.wikipedia.org/wiki/Flag_of_South_Africa
Viseux, C. (n.d.). Mandela's Funeral. Johannesburg.

