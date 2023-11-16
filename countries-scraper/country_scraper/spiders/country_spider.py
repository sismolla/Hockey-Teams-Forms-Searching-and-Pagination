import scrapy
from HockeyTeams.items import HockeyteamsItem


class HockeyspiderSpider(scrapy.Spider):
    name = "hockeyspider"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]

    def parse(self, response):
        url = 'https://www.scrapethissite.com/pages/forms/?page_num='
        for i in range(1, 25):
            full_url = url + str(i)
            print(f'page {i} is under control*****************************')
            yield response.follow(full_url, callback=self.the_scraper_code)

    def the_scraper_code(self, response):
        items = HockeyteamsItem()
        table_data = response.css('table.table tr')
        for i in range(1, 26):
            items['url'] = response.url
            items['name'] = table_data[i].css('td.name::text').get().strip()
            items['year'] = table_data[i].css('td.year::text').get()
            items['Wins'] = table_data[i].css('td.wins::text').get().strip()
            items['losses'] = table_data[i].css('td.losses::text').get()
            items['ot_losses'] = table_data[i].css('td.ot-losses::text').get().strip()
            items['goals_for_GF'] = table_data[i].css('td.gf::text').get()
            items['goals_aginest'] = table_data[i].css('td.ga::text').get()
            if table_data[i].css('td.pct.text-success::text').get() is not None:
                items['win_percent'] = table_data[i].css('td.pct.text-success::text').get()
            elif table_data[i].css('td.pct.text-danger::text').get() is not None:
                items['win_percent'] = table_data[i].css('td.pct.text-danger::text').get()
            elif table_data[i].css('td.diff.text-success::text').get() is not None:
                items['diff_text_success'] = table_data[i].css('td.diff.text-success::text').get()
            elif table_data[i].css('td.diff.text-danger::text').get() is not None:
                items['diff_text_success'] = table_data[i].css('td.diff.text-danger::text').get()

            yield items
