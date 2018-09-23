# -*- coding: utf-8 -*-
import scrapy


class GetMoviesSpider(scrapy.Spider):
    name = 'get_movies'
    allowed_domains = ['www.imdb.com/chart/top?ref_=nv_mv_250']
    start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250/']


    def parse(self, response):
        movies = response.xpath('//tbody/tr')

        for movie in movies:
            order = movie.xpath('.//@data-value').extract_first()
            relative_page_url = movie.xpath('.//a/@href').extract_first()
            absolute_page_url = 'www.imdb.com' + relative_page_url
            title = movie.xpath('.//*[@class="titleColumn"]/a/text()').extract_first()
            year = movie.xpath('.//*[@class="titleColumn"]/span/text()').extract_first()
            rating = movie.xpath('.//*[@class="ratingColumn imdbRating"]/strong/text()').extract_first()

            print(absolute_page_url)

            yield{
                'Order': order,
                'Title': title,
                'Year': year,
                'Rating': rating,
                'Movie_url': absolute_page_url
            }
