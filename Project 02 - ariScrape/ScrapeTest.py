from ariScrape import Scraper

# test ticker symbol @ nasdaq.com
test_ticker = "INTC"
url_prefix = "https://www.nasdaq.com/symbol/"
url_suffix = "/financials"
url_parts = [url_prefix,test_ticker,url_suffix]

# xpath of @top left of table @url
# >> //*[@id="financials-iframe-wrap"]/div[1]/table/tbody/tr[1]/td[2]
# xpath of @bottom right of table @url
# >> //*[@id="financials-iframe-wrap"]/div[1]/table/tbody/tr[19]/td[5]
# these are the string parts of the xpath that
# will not change while we iterate
xpath_part1 = '//*[@id="financials-iframe-wrap"]/div[1]/table/tbody/tr['
xpath_part2 = ']/td['
xpath_part3 = ']'

# init the column and row keys for the example table
xpath_column_key = [i for i in range(2,6,1)] # create column index 2-5
xpath_row_key = [i for i in range(1,20,1)] # create row index 1-19

# make an array of xpath_parts that we're going to iterate over
xpath_parts = [[xpath_part1,r,xpath_part2,c,xpath_part3] for c in xpath_column_key for r in xpath_row_key]

# create an ariScrape object
scrapeObj = Scraper()
scrapeObj.verbose = False
scrapeObj.getChromeDriverPath()
scrapeObj.getChromeDriver()
scrapeObj.setURLFromParts(url_parts)
scrapeObj.LoadPage()
# set this to True if you want to see the extracted
# values -- useful when obj.verbose is False
val_verbose = True
for xp in xpath_parts:
    scrapeObj.setXPathFromParts(xp)
    scrapeObj.ExtractFloatAtXPath()
    if val_verbose:
        print(scrapeObj.scrapped_item)
scrapeObj.driver.close()