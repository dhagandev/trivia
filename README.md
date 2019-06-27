# You Have a Trivia Problem

### Concept
Think you're better than your friends at trivia? Do they call you a know-it-all? Do you know it all? Are you the master of all things trivial? Well you may have a trivia problem! Basically, like every other trivia game out there, you answer questions to compete with others.

### Why Trivia?
Creating a trivia app allowed me to work with an API. I used the Open Trivia Database (https://opentdb.com/api_config.php) to provide my questions to the user. Since I didn't want to repeat questions in my database, I stored what I received from the API in my database if the question did not appear in my database. This was good practice for me to be using 3rd party APIs.

### What Happened to Conway?
Well you see, that is a long story...

##### Technically
Technically speaking, Jen and I had failed from the start. We approached the problem from a front-end focus with the intent of modelling the backend off what the user would see. However that was the wrong way to work with Django. We should've first thought of how we would route our pages and database calls; had we started with that, we would have sooner realized that the designer's first (and final) iteration of the design had create, read, and update on one page in a way that was overly challenging for our current skill level. (That being said, I plan on returning to Conway and trying it again.) The second biggest technical challenge would be the algorithm for Conway. I had studied and implemented it before, but it was completely foreign to Jen so I worked with her to help break it down.

##### With Regards to Teamwork
As I have said to Jen, she excels at following the basic flow of creating with the use of tools. Where she struggles most is breaking down problems and understanding very basic concepts. Now, the rest of this critique will be focused on the designers that were on our Conway team.
Our designers refused to discuss anything related to the project until the Thursday before. They worked diligently that Friday, but mostly with each other. The intent was to teach us as developers what they do and the most they taught is that "Oh, we do research". It frustrated me a bit that everything was divided, but I accepted it as a divide and conquer method and it seemed to work for our team dynamic. 
As the development progressed, I made sure to keep the designers updated. I later heard that behind the developers' backs, they were complaining about being kept informed. They repeatedly made it clear that after that Friday, they had no interest in the project and were not going to include it in their portfolios. (For this reason, when I rework Conway I will not be including their names on the project except to give Sara credit for the sprites.) 
I heard about several complaints they had made against us, and myself in particular, such as the fact I list myself as a UI/UX Developer on LinkedIn made Mary feel as though I thought I knew more about UI/UX than her and Sara, but I never claimed that to be the case. I did question some of their design choices because I wanted to understand their methods, especially since they neglected to communicate why they made any of their choices. I informed them of when choices they made could be confusing to a user and we compromised on changes. I fully recognized that the design was their lead and they had final say. 
In addition to their back talk, they refused to communicate or provide us as developers with necessary files that we needed. For example, the day before the project was due I asked them for a hex shade of red that they would like for a warning/error message. They refused to pick a color and told me, as a developer, to choose it. Several questions I have asked them went unanswered. Overall, they were incredibly uncooperative, which was quite surprising to me given that I had heard high remarks of Sara. I will say I felt Sara did contribute to the project, where as I honestly cannot think of one concrete piece that Mary had contributed to the project.
I am grateful for the experience to work with designers and despite Conway being a trainwreck with poor teamwork, I am proud of the project and learned a great deal. 

### Site Link
https://djangotrivia.herokuapp.com/

### How to Play
Sign up or log in and click "question". From there, enjoy answering various trivia questions!

### Technology Used
Python
Django
HTML
CSS
Heroku
Git

### Biggest Challenge
The biggest challenge came from the Conway project - learning to think "back-end" first. As a front-end developer, it was difficult for me to translate certain components into the most appropriate backend structure. Furthermore, Jen and I had allowed the designer's design to rule the direction of the routes. It was not until it was too late that we realized had structured our architecture in a way that was impossible for our skill level.

### Key Learnings & Take Aways
* Working with uncooperative designers who have no interest/care in the project
* Working with developers of a lower skill level than myself
* Patience and professionalism

### Project Continuation
* Select difficulty
* Select category
* Personal scores for different difficulties
* Personal scores for different categories
* Different types of login
* Achievements