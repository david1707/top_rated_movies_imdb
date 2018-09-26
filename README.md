# IMDB top rated movies
A python-based scrapper that gets the top 250 rated movies

## Getting Started
These instructions will tell you how to download, run and use this project:

### Installing

```
git clone https://github.com/david1707/top_rated_movies_imdb
```

### Usage

Navigate to the main folder, then run it with:
```
scrapy crawl get_movies
```

If you want to save the yield result, do it like this:

```
scrapy crawl get_movies -o top_250_movies.json
```

You can use .json, .xml, .csv....


## Built With

* [Python](https://www.python.org/) - Python is an interpreted high-level programming language for general-purpose programming.
* [Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.

## Authors

* **David Membrives** - *Initial work* - [david1707](https://github.com/david1707)


## License

This project is licensed under the ISC License
