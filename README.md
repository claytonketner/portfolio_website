# portfolio_website
http://claytonketner.com

This is the Django for my personal portfolio website. It runs on heroku (for
free - thanks heroku!).

Entries
============
Entries are stored as `html` files (in `entries/`), so that I have the
flexibility to do whatever I want, but also have a homebrewed "markdown" to
autofill some of the boilerplate. For more info on how that works, check out
[the entry readme](entries/README.md).

Entries are loaded into the database using
```python
python manage.py load_entries
```
This command goes through each `entries/*.html` file and grabs its content to
populate the `PortfolioEntry` model's fields. The `PortfolioEntry` model stores
the `<body>` along with metadata from the `<head>` of the html file.

This approach allows the entries to be verison controlled, but still have the
advantages of being in a database. Handy!
