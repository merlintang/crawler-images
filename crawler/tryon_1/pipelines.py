# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
import os.path

class Tryon1Pipeline(object):
    def process_item(self, item, spider):
        detailURL = item['imageUrl']

        imageUrl_others = item["imageUrlOthers"]

        path = '../../tmp/images/full/'

        if not os.path.exists(path):
            os.makedirs(path)

        image=requests.get(detailURL)

        path = path + item['id'] + '.jpg'

        f=open(path,'wb')
        f.write(image.content)
        f.close()

        prefix = 'https://s3-us-west-1.amazonaws.com/maydayproject/item/'
        item['imageUrl'] = prefix + item['id'] + '.jpg'

        for index, url in enumerate(imageUrl_others):
            image = requests.get(url)
            path = path + item['id'] + '_' + str(index)+'.jpg'
            f = open(path, 'wb')
            f.write(image.content)
            f.close()
            imageUrl_others[index] = prefix + item['id'] + '_' + str(index)+'.jpg'

        if os.path.isfile(path):
            return item