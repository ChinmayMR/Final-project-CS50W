# Trios Intranet - An intranet for The Trios Hotel employees

## Introduction
### What is an intranet?
An intranet is a private network that is used by an organization to share information and resources with its employees. It is similar to the internet, but it is not accessible to the public. Intranets can be used to store documents, share files, collaborate on projects, and communicate with employees. They can also be used to provide employees with access to training materials, benefits information, and other resources. Intranets can be a valuable tool for organizations of all sizes. They can help to improve communication, collaboration, and productivity.  
*This information was provided by [Bard](https://bard.google.com), a large language model from Google AI.*

In this intranet you can add, remove and view annoucements/alerts, send and approve leave applications, request appointments and view, add checklists.

## Installation
Download the files and then execute the following commands(required):  
 - `` pip install -r requirements.txt ``  
 - `` python manage.py makemigrations intracom ``  
 - `` python manage.py migrate ``
## How to run the application?
- Make sure you completed the steps shown in the [Installation](#installation) section.
- Run `` python manage.py createsuperuser `` and create a new user.
- Optional: If you want to get accesss to manager permissions such as being able to create new post or approving new users, go to the admin page and then set the manager option to True for the user. This is only for the first user other users can be made a manager using the [edit-users-page](#edit-users-page).
- Log-in and you will be redirected to the *[home-page](#home-page--alerts-page)*!
- If you try to create a user using the register form then the user will need to be approved by a manager before he/she logs in.
## Distinctiveness and Complexity
I wanted to make a project that would be practical and helpful to people. I was visiting my dad's hotel with my family when I noticed that the employees were still using paper checklists, which could easily get lost or torn and that paper would get wasted. This made me think about how I could create a digital checklist that would be more convenient and efficient.

In terms of complexity, I used Django with more than one model and JavaScript on the front-end. This was also the first time I used CSS transitions. Making the design mobile-friendly was also a new challenge using CSS and javascript. This project is a website which helps the employees in their work. They can easily check if there has been any announcements or if someone wants to meet them or even find the day-to-day checklists that they use or if they want to submit a leave application. These are all possible through the app.

![mobile-friendly screenshots](https://lh3.googleusercontent.com/drive-viewer/AFGJ81ooADupY6UB_lzJ3LH1K5nzOE2JRd8pwOnSYZDghbnyHa3OepDIoS-xgD43pq444ewrv_EjgyQWHbDP8Jq-Y_DhAvy8aA=w1920-h1007)

## Any other additional information the staff should know about your project
 - If you try to create a user using the register form and try to login with the same credentials you will not be able to since each user will need to be approved by the manager-users before they are allowed to sign in, this is because this is a employee only website. In case you are the first user, then you can create a superuser using the command `` python manage.py createsuperuser `` and then go to the django admin page and manually set manager boolean to true in the user model. For the other users after that they can be approved through the *[edit-users-page](#edit-users-page)*.
## Why you did it?
 The ideology of this project was to make a website which was both practical and helpful.  I created this *[intranet](#what-is-an-intranet)* to help hotel employees switch away from paper. Paper-based systems are often inefficient, ecologically unfriendly and time-consuming. They can also be a source of lost or misplaced information. An *[intranet](#what-is-an-intranet)* can help to eliminate these problems by providing a centralized location for employees to store and access information. Everyone nowadays has a mobile phone on them so this site can be accessed wherever you are. 
## Project structure / features
### Register page
You can register in this page. But if you try to login using the same credentials you used to sign in you can will not be able to login. Why, you might ask, well this is because this a employee only website, so not everyone can access this website, so you should get approval from any of the users which are managers. They should go to the *[edit-users-page](#edit-users-page)* and approve the users.  

![Register page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81rXc7mPz_I03WHQZ0Q3JLWeJ5NRMZkOz2WScKrHyeY_AEXnB9dKl7FxYkPotknfiMVLdzxUVMiILSP-uuazOYbH0KolVw=w1920-h1007)  
### Login page
You can login using the credentials you registered with in the *[register page](#register-page)* if you are approved by anyone of the managers and you will be redirected to the *[home-page](#home-page--alerts-page)*.
![Login page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81qtaTxCy7rfiiN1WLZfWcEhu4FKr5FCp2xghFJQDEgZQpwb7sbef3VwbN4C7ramXj7OLoT89kxsZU2756N3gpRJigrqxg=w1920-h1007)

### Expanding nav bar
The nav bar expands on hovering and there are 4 main icons in the middle. Those 4 icons in the middle lead to their respective pages, more details about the pages are mentioned below. The icon at the bottom is for logging out and the icon at the top(edit users) is for approving new users and making users into managers.
![Expanding nav bar](https://lh3.googleusercontent.com/drive-viewer/AFGJ81p52HNMvCbhikoPn2fXrCjgNfsZCe8n3WejjRfHVOpDc9qIeOIHUazTwKpuXAAzgbKwMTjYDe-rKMLi3cfEcG2wZhQP4g=w1920-h1007)
### Home page / Alerts page
This is the first page you see when you login. Here you can see of all the announcements posted by any of the managers. If you are the manager you will see an add button to add a new alert. If you are a manager you can also see a delete button when you hover over each indivudual alert when you click on that button, the corresponding alert will be deleted. If you click on the "View details" button you can see all of the details of the alert you clicked on.

![Home page / Alerts page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81qdQVH_P_Jabhqya79-cAspLZTTnjH37M78YC3eZ8tuXQr4w0loqrV0qJaeMdLPPAg-o6aVvUptRARzTzVPDr33U5TAvQ=w1920-h1007)

### Checklist page
This is the second item in *[nav-bar](#expanding-nav-bar)*.You can see a filter button on the bottom right, and when you click on that button then a filter menu will appear and you can filter for the required department. If you are the manager you will see an add button to add a new checklist which opens a modal for you to add a new checklist. If you are a manager when you hover over each indivudual checklist item you can also see a delete button.  When you click on that button, the corresponding checklist will be deleted. If you click on the "View details" button you see the all of the tasks of the checklist you clicked on.
![Checklist page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81ohz8WOgbD9OGC8THY1d8BqPYCWwaQf1jzeB9ScvSJPz326O3DV7WTrls4-Vf0w4ZRva_EDOIoE7KMExRNIi4zolkS7=w1920-h1007)

### Appointment page
This is the third item in the *[nav-bar](#expanding-nav-bar)*. You can see all of your requests and request others have made to you here. If you are a manager you can see all of the requests. You can see a add button at the bottom and when clicked it opens a modal for you to create a new appointment with any of the managers. The person who got the request can accept or decline with a message by clicking on the cross and check-mark icons shown when hovered. If you click on the "View details" button you see the all of the details of the appointment you clicked on.
![Appointment page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81rtTTLXtc9On_28FUcT06WEFd3gNqTM_w2lf4KPraCt989aYAqkCjcVuM67eamABq9wPUygqfyCMXrmNezwkwLpvI_8bw=w1920-h1007)

### Leave page
This is the 4th item in the *[nav-bar](#expanding-nav-bar)*. You see all of your leave applications here and check if they were accepted or declined. If you are a manager you can see all of the requests. Similar to the appointments page you can accept or decline the leave applications with a message. If you click on the "View details" button you see the all of the details of the leave application you clicked on.
![Leave page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81ohnYDG8pqz94Ydrx-sVROlQdBJOtLbV3ICq2xoYa5iAkThwaiHN90eaalABzv76dLDf340K9WLbD-uJEe-dQpMMrDVmA=w1920-h1007)

### Edit users page
This page can only be accessed by managers. In this page you can make a user into a manager and approve or decline and any user approval requests. If a user is a manager then you can see this page icon in top portion of nav bar.
![Edit users page](https://lh3.googleusercontent.com/drive-viewer/AFGJ81qkTtEbGVLEZSgXqRAot-TK02gzP-Lul9ASUY6m0s-_1KCavUcaKrXJBEF-2XRFCLJ6jybre1JP_zcxXF-VvhH_qERDuQ=w1920-h1007)

## Files
```
trios
├── trios/ -> core application
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py -> Settings for the application
│   ├── urls.py -> Global urls mapping
│   └── wsgi.py 
├── intracom/  -> The main website/app
│   ├── migrations/ -> Automatically generated migrations folder
│   ├── static/
│   │   └── intracom/
│   │       ├── alert.css -> CSS file for alerts page
│   │       ├── alert.js -> Javascript file for alerts page
│   │       ├── appointment.css -> CSS file for appointment page
│   │       ├── appointment.js -> Javascript file for appointment page
│   │       ├── checklists.css -> CSS file for checklists page
│   │       ├── checklists.js -> Javascript file for checklists page
│   │       ├── edit.css -> CSS file for edit page
│   │       ├── icon.png -> Favicon for the all the pages
│   │       ├── leave.css -> CSS file for leave page
│   │       ├── leave.js -> Javascript file for leave page
│   │       ├── login.css -> CSS file for login page
│   │       └── styles.css -> CSS file for styles page
│   ├── templates/
│   │   └── intracom/
│   │       ├── alerts.html -> Alert page
│   │       ├── appointment.html -> Appointment page
│   │       ├── checklists.html -> Checklist page
│   │       ├── edit.html -> Edit user page
│   │       ├── layout.html -> Basic layout template file
│   │       ├── leave.html -> Leave application page
│   │       ├── login.html -> Login page
│   │       └── register.html -> Register page
│   ├── __init__.py
│   ├── admin.py -> Registering models to admin
│   ├── apps.py
│   ├── models.py -> App models
│   ├── tests.py
│   ├── urls.py -> URLs in this app
│   └── views.py -> Website views
├── manage.py
├── README.md -> README file 
└── requirements.txt -> file that contains the project dependencies
```