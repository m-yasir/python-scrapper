import scrapy


class CWC(scrapy.Spider):
    name = "cwc"

    def start_requests(self):
        start_urls = [
            "https://www.cricketworldcup.com/news/en/"
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        btn = response.css("button.js-show-more-button").get()
        btn.click()
        for news in response.css("figcaption.thumbnail__caption"):
            yield {
                "title": news.css("h5.thumbnail__title::text").get(),
                "date": news.css("time.thumbnail__date-day::text").get(),
                "year": news.css("time.thumbnail__date-year::text").get(),
            }