# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HockeyteamsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        lists = ['goals_aginest', 'goals_for_GF', 'losses', 'win_percent', 'year','ot_losses']
        try:
            for key in lists:
                value = adapter.get(key)
                if value is not None:
                    adapter[key] = float(value.strip())
                    print(type(adapter[key]))
                    print('Done////////////////////////////////////////////////////////////////')

        except TypeError as e:
            print(f"An error occurred: {e}")

        return item
