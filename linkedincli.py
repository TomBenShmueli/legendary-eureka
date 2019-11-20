import requests
import click
from bs4 import BeautifulSoup

#  Sends a get request to the and returns the html. Returns None in cases the request is failed.
def get_url_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        return (requests.get(url)).content
    return None


#  Returns a BeautifulSoup object which allows for html manipulation and efficient data extraction.
def beautify(url):
    source = get_url_content(url)
    if source is None:
        return source
    else:
        return BeautifulSoup(source, "html.parser")

#  Returns a list of relevant LinkedIn job links.
def extractjobs(url):
    jobs = beautify(url)
    joblist = jobs.find_all("a", class_="result-card__full-card-link")
    if joblist == []:
        return None
    else:
        linklist = []
        for link in joblist:
            linklist.append(link.get('href'))
        return linklist


@click.command()
@click.option('--joburl', prompt='Please enter a LinkedIn job url in order to receive similar positions.',
              help='URL to insert')
def pullinfo(joburl):
    print(extractjobs(joburl))

if __name__ == '__main__':
    pullinfo()
