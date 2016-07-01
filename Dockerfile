FROM django:onbuild
MAINTAINER Lee Gent <lee@leegent.net>
CMD ["gunicorn", "fizzbuzz.wsgi", "--log-file", "-", "-b", "0.0.0.0:8000"]
