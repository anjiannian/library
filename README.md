### Deploy
* Database

    ```
    CREATE DATABASE library DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci
    CREATE USER nobody@localhost IDENTIFIED BY "hell0";
    GRANT ALL PRIVILEGES ON library. * TO nobody@localhost;
    ```

* Requirements

    `pip install -r requirements.txt`

* Migrate

    `python manage.py migrate`
