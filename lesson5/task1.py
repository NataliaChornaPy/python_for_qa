# Write a function to get product price from web page for Deshevshe site.Handle the case when a product is out of stock
# -*- coding: utf-8 -*-
from lxml import html
import re
def main():
    pattern_abbr = re.compile('[0-9]')
    dom = html.parse(('http://deshevshe.net.ua/multivarka-rotex/rotex_rmc507_b'))
    title = dom.find('//*[@itemprop="price"]')
    price=re.match(pattern_abbr,title.text)
    if price:
       print "PRICE is",(title.text)
    else:
        print "Немає на складі"

if __name__ == '__main__':
    main()