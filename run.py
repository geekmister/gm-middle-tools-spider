from scrapy import cmdline
from scrapy.crawler import CrawlerProcess

from src.spiders.pyenv_github import PyenvGithubSpider

# quotes 对应的是爬虫名 在cmd运行 scrapy crawl quotes 同步
cmdline.execute("scrapy crawl pyenv_github_spider".split())


def execute_single_spider():
    cmdline.execute("scrapy crawl pyenv_github_spider".split())


def execute_multiple_spider_by_process():
    process = CrawlerProcess()
    process.crawl(PyenvGithubSpider)
    process.start()


def execute_multiple_spider_by_runner():
    # TODO Has another function by CrawlerRunner, see: https://blog.csdn.net/zouzhe121/article/details/102732243
    pass


if __name__ == "__main__":
    execute_multiple_spider_by_process()
