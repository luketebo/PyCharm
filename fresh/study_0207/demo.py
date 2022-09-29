from xml import etree

from lxml import html
import requests
tree = requests.get(r"https://baidu.com")
tree = etree.HTML(tree.txt)
result = tree.xpath("//div")
print(result)