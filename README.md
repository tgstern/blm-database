# A Black Lives Matter Database

This application is designed as a tool to support the Black Lives Matter Movement.
Initially the pages have links to learn more, donate to memorial funds, and join the
official movement.

## API and SQL queries

The power comes from entering a location on the home page, which pulls links from the
SQL database and Representative data from Google Civic Data API. The routes are built
with Django and sources of the articles and links are listed on the about page.

The location feature works best with a full address, but will also work just as a state
filter. The Django route will pull the appropriate data and add sections to the index
as needed.

## Updating

On the about page, there is also a place to add feedback that will get pushed to the 
database and is accessible to view from the Django admin page. New links and sources
can also be added through the admin page to make it easy to update the content.

This site is hosted live with Heroku at https://blm-database.herokuapp.com