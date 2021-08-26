# Django htmx Demo
This project demonstrates how to use [htmx](https://htmx.org) with Django.

It implements with django some examples of the [htmx examples page](https://htmx.org/examples/).

### Start the project
- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: ```docker-compose build ```

- Create some test data

    ```docker-compose run --rm django python manage.py create_products  100```

- Run ```docker-compose up``` and go to http://0.0.0.0:8000
to see your runserver.


---
Created with [Django Docker Starter Template](https://github.com/abel-castro/ddst).