from typing import Any


from scrapy import Spider
from scrapy.http import Response


class PyenvGithubSpider(Spider):
    name = "pyenv_github_spider"
    start_urls = ["https://github.com/pyenv/pyenv/releases"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        list_selector = response.xpath("//a[@class='Link--primary Link']")
        for one_selector in list_selector:
            version = one_selector.xpath("//a[@class='Link--primary Link']/text()").extract()[0]
            print("玛德")
            print(version)

        print(list_selector)

