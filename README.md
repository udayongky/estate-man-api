# Estate Management API

## Installation

### Requirements

Before proceeding make sure you have installed [Rye](https://rye.astral.sh/guide/installation/)

### Manual Installation

    $ curl -LOk https://github.com/udayongky/estate-man-api/archive/master.zip
    $ unzip master
    $ mv estate-man-api example
    #Copy to DJANGO_SECRET_KEY in .env.local
    $ python -c "import secrets; print(secrets.token_urlsafe(38))"
    $ rye sync

