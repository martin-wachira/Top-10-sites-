#import the required libraries
from lxml import html
import pandas as pd
import requests
#set header 
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept":"text/html,application/xhtml+xml,application/xml;\
q=0.9,image/webp,*/*;q=0.8"}
url = 'https://www.alexa.com/topsites'
#get the page
try:
	page=requests.get(url, headers=headers)
except Exception as e:
	print(str(e))
	page = None
	
tree = html.fromstring(page.content)
details = []
#scrape the required data
for i in range(2,52):
	name = tree.xpath("/html/body/div[1]/div/section/div/div/section[2]/span/span/div/div/div[2]/div["+str(i)+"]/div[2]/p/a/text()")
	time = tree.xpath("/html/body/div[1]/div/section/div/div/section[2]/span/span/div/div/div[2]/div["+str(i)+"]/div[3]/p/text()")
	time_2 = tree.xpath("/html/body/div[1]/div/section/div/div/section[2]/span/span/div/div/div[2]/div["+str(i)+"]/div[4]/p/text()")
	percentage = tree.xpath("/html/body/div[1]/div/section/div/div/section[2]/span/span/div/div/div[2]/div["+str(i)+"]/div[5]/p/text()")
	percentage_2 = tree.xpath("/html/body/div[1]/div/section/div/div/section[2]/span/span/div/div/div[2]/div["+str(i)+"]/div[6]/p/text()")
	details.append(((str(name).strip("'[]'")),(str(time).strip("'[]'")),(str(time_2).strip("'[]'")),(str(percentage).strip("'[]'")),(str(percentage_2).strip("'[]'"))))


#Save the result to a dataframe
df = pd.DataFrame(details, columns=[' Site','Daily Time on Site','Daily Pageviews per Visitor','% of Traffic From Search','Total Sites Linking In'])

print(df)

#Save the data to csv
df.to_csv('alexa.csv', index=False)
