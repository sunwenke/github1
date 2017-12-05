import scrapy


class GithubItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
    branches = scrapy.Field()
    commits = scrapy.Field()
    releases = scrapy.Field()