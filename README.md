This is Fannie's Neuralink Submission.

NEURALINK(Root)
    ├──-
        ├── accounts
        ├── actions
        ├── host
        ├── neuralink
        ├── proxy
        ├── pull
        ├── scripts
        ├── templates
        ├── venv
        ├── db.sqlite3
        ├── docker-compose-deploy.yml
        ├── docker-compose.yml
        ├── dockerfile
        └── manage.py
        └── ReadMe
        └── requirements.txt

From the terminal navigate to the Neuralink Root Directory and run
`docker-compose -f docker-compose-deploy.yml up --build`

This will set up the Nginx server and allow you to access the application via the following link. 

[Link To Home Page](http://127.0.0.1:8000/)

You may log in using the following credentials 
username - neuralink
password - Neuralink33

From here you can access your dashboard to check out your profile. The data shown midway can be modified using the REST API capabilities. 

To use the REST API capability, navigate to http://127.0.0.1:8000/REST/

Click on the {'actions': link provided} (should be - "actions": "http://127.0.0.1:8000/REST/actions/")

From here, you may access the action items per user. You may POST new Actions, but keep in mind that the User may only have one device. 

To access user specific info, input the id number to obtain API response. For the 'neuralink' user, this will be 1. The link will then be as follows - "actions": "http://127.0.0.1:8000/REST/actions/1/" Now you may make use of the PUT api call to make any necessary changes. If you update the 'Data' field, you will notice the updates in the dashboard. Simply, navigate back to http://127.0.0.1:8000/ to access your dahsboard using the nav-link. 

The provided username/password credentials is for a 'superuser'. You may log in as admin and have full control over the backend databases. http://127.0.0.1:8000/admin/



Pros and cons of the implementation - 

Pros- User profile functionality, with REST API calls.

Cons- Not enough time to implement a better UI/UX experience for the REST API functionality. I believe I would have dont a much better job had I not be in school fulltime and working. I wasn't able to deploy to the cloud via docker deployment. Test functionality was completed by hand and did not make use of the tests.py per django application. No CI/CD pipeline was set for continuous updating and distributions. I wanted to have an interactive way for admin to list the whitelisted IP's. The IP's are configured in the docker build.

I would change the CI/CD pipeline and REST API functionalitiy if I was given more time. 

Thank you for the opportunity! 