from scrapy import cmdline

spider = 'bookstoscrape'
arguments = [
]

command = f'scrapy crawl {spider}'
if arguments:
    arguments = " ".join(arguments)
    command = f'{command} {arguments}'

cmdline.execute(command.split())
