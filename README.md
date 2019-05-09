[![Build Status](https://travis-ci.org/dhamma1991/milestone-project-4.svg?branch=master)](https://travis-ci.org/dhamma1991/milestone-project-4)


It was decided to hide some of the default Django 'hints' for when the user is creating an account or changing their password. This was to prevent the form from cluttering up, as the hints, especially for the password, constituted a large proportion of the text content of the forms before the decision to hide the hints was taken. Django seems fairly relaxed about the username or password the user chooses, with authentication that seems pretty standard across the Internet. It was decided therefore to hide the password and username hints using CSS, this being the obvious way to hide them. 

It would probably be more efficient to hide the hints by modifying the forms backend, but with the CSS route only taking a tiny amount of code, this was my preferred option.

Should the user fail the validation when the form is submitted, then hints will still show as before, highlighted in red.

{{ It was decided to not go with client-side validation for the user forms. It would be envisioned that????? }}



Material Icons are used on tasks.html to represent the user's hitpoints, experience, and also as icons representing tasks. 

Within the wireframes for the project, canva elements were used for the icons. It was decided to go with Material Icons during development as these would be easier to implement, are included with Materialize, and are as aesthetically viable as the canva elements.


With the task/done url, there is technically an exploit the user can perform where they can modify the URL to change the amount of xp they gain.

For example, say UserX has a task with id of 6, with a difficulty of Easy. If the user manually enters tasks/done/6/AM (with the 'AM' standing for ambitious), the user will mark the task as done, but gain the 40 xp reward for an Ambitious task completion, as opposed to the usual 10 xp for an Easy task.

However, it should be noted that the user has full control over the difficulty that they set to their tasks, so it doesn't make sense for the user to exploit the url system this way. Therefore, although this exploit exists, it doesn't really effect the functionality of the app.

# Testing

Automated testing was conducted using Django's built-in test framework (TestCase).

Sanity tests were conducted first, these can be found in levelup/tests.py. Simple assertion tests were used to check that the test framework was functioning correctly.

Building up from there, I tested some of the built-in Django components, starting with the forms. I tested the AddTaskForm and UserCreationForm, checking that objects can be created successfully and that form.is_valid is true and false in cases where it should be true and false. No issues were detected during the tests. The tests themselves can be found within levelup/test_forms.py.

I then moved to testing authentication. I was not expecting any problems here, since I am using the default Django authentication system. I tested that a user with some credentials was able to successfully log on. This test was fine, the test can be found in test_authentication.

I then moved to testing views. Much of the more custom functionality the app possesses can be found within the views, so I focused particularly on these tests during the testing process.

I first attempted a simple test just checking that the index page can be reached by using self.client.get("/"). At first I got a Value Error stating: Missing staticfiles manifest entry for 'css/style.css'. After some googling I followed the advice in [this stackoverflow thread](Missing staticfiles manifest entry for 'css/style.css') and managed to fix the error by running python manage.py collectstatic. This fixed the error, and the first simple test passed.

# Technologies Used
Django
[link here]

Materialize 1.0.0
https://materializecss.com/

jQuery 3.2.1
[link here]

chain-fade
https://www.jqueryscript.net/animation/Sequential-Entrance-Animations-chain-fade.html

# REFERENCES
Images

Task Checkbox
https://www.canva.com/media/MAAQottVXFI with custom colour modification