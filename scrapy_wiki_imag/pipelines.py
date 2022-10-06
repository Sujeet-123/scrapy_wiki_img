# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline

class customImagepipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.url.split('/')[-1]

