![Cool logo](./main/static/main/pictures/games_lib_bw_small.png)

# My Game Library

A web interface to manage my game collection, because having games on Steam, GoG, Humble bundle and consoles is too much to handle for only one brain.

## Installation

Install [pipenv](https://docs.pipenv.org/). For Mac users with Brew:

```bash
brew install pipenv
```

Otherwise, please follow [their installation instructions](https://docs.pipenv.org/install/#installing-pipenv).

Install all dependencies & a Python virtual environment:

```bash
pipenv install
```

Enter your pipenv shell:

```bash
pipenv shell
```

Set up the server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If all's gone well, you should now be able to connect via localhost. The admin panel is available at `/admin`.