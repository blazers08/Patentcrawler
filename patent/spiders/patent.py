import scrapy
# from bs4 import BeautifulSoup
from patent.items import PatentItem
import lxml
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class patentCrawler(scrapy.Spider):
	name = 'patent'
	# url_num = 0 
	# start_urls = []
	x = 0

	def start_requests(self):
		for x in range(8000000,8000010,1):
			xstr = str(x)
			yield scrapy.Request('http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='+xstr+'.PN.&OS=PN/'+xstr+'&RS=PN/'+xstr, self.parse)
	# xstr = '6923000'
	# start_urls = [
 #        'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='+xstr+'.PN.&OS=PN/'+xstr+'&RS=PN/'+xstr,
 #        'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='+xstr+'.PN.&OS=PN/'+xstr+'&RS=PN/'+xstr,
 #        'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1='+xstr+'.PN.&OS=PN/'+xstr+'&RS=PN/'+xstr
 #    ]
	def parse(self, response):
		# response = HtmlResponse(url='http://example.com', body=body)
 		# res = Selector(response=response).xpath('/html/body/font()').extract()
		res = Selector(response)
		for title in res.xpath('//font[@size="+1"]/text()').extract():
			print("======Title======")
			print(title)#.select('font::text')[0].text)

		for abstract in res.xpath('//body/p/text()').extract():
			print("======Abstract======")
			print(abstract)#.xpath('p'))[0].text

		for contents in res.xpath('//table[2]/tr[2]/td[1]/b/text()').extract():
			print("======Contents======")
			print(contents)#.select('font'))[0].text

		def parse_detail(self, response):
			patentitem = PatentItem()
			patentitem['title'] = res.xpath('//font[@size="+1"]/text()').extract()
			patentitem['abstract'] = res.xpath('//body/p/text()').extract()
			patentitem['contents'] = res.xpath('/table[2]/tr[2]/td[1]/b/text()').extract()
			return patentitem