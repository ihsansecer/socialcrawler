import click

from utils import authenticate, read_file, write_file
from crawlers import UserCrawler
from crawlers import UserTweetCrawler
from networks import UserNetwork



@click.group()
def cli():
    pass


@cli.command()
@click.option("--depth", "-d", default=1, help="Depth level of crawler")
def crawl_users(depth):
    """
    Crawls users in screen_names.json using their friends and followers. Then saves it to data.json.
    """
    screen_names = read_file("screen_names.json")
    crawled_users = {}
    api = authenticate()
    for screen_name in screen_names:
        crawler = UserCrawler(screen_name, api)
        crawled_users.update(crawler.crawl(depth=depth))
    data = read_file("data.json")
    data.update({"crawled_users": crawled_users})
    write_file("data.json", data)


@cli.command()
@click.option("--incoming", "-in", default=1, help="Number of incoming edges")
@click.option("--outgoing", "-out", default=1, help="Number of outgoing edges")
def filter_users(incoming, outgoing):
    """
    Filters users by number of incoming and outgoing edges. Then saves it to data.json.
    """
    data = read_file("data.json")
    network = UserNetwork(data["crawled_users"])
    network.create()
    filtered_users = network.filter(incoming, outgoing)
    data.update({"filtered_users": filtered_users})
    write_file("data.json", data)

@cli.command()
def crawl_tweets():
    data = read_file("data.json")
    filtered_users = data["filter_users"]
    crawl_tweets = UserTweetCrawler(filtered_users)
    crawled_tweets = crawl_tweets.catch_user()
    data.update({"crawled_tweets": crawled_tweets})

@cli.command()
def crawl_tweets():
    """
    Crawls tweets using filtered user ids inside data.json. Then saves it to data.json.
    """
    data = read_file("data.json")
    filtered_users = data["filtered_users"]
    crawled_tweets = []
    data.update({"crawled_tweets": crawled_tweets})


if __name__ == '__main__':
    cli()
