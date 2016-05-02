import requests
import re
import Image

requests.packages.urllib3.disable_warnings()

SAVETOFILE = False
POPULARLINK='https://www.dcard.tw/api/forum/all/1/popular'
LINK='https://www.dcard.tw/api/forum/sex/1'


post_id=[]
post_link=[]
r = requests.get(LINK)
article = r.json()


"""# See the components
for post in article:
	for typ in post:
		print(typ)
"""

# find every id of article, store to post_id[] 
for post in article:
	post_id.append(post['id'])
#print post_id

# find every link in every article
for id in post_id:
	r = requests.get('https://www.dcard.tw/api/post/all/'+str(id))
	article = r.json()
	content =  article['version'][0]['content'] # looking into the content
	p = re.compile(ur'(http:\/\/i?.?imgur.com\/[\w]+)')
	result= re.findall(p,content)
	for i in result:
		second_r = requests.get(i)
		second_content = second_r.content
		second_p = re.compile(ur'(http:\/\/i?.?imgur.com\/\w+\.[jpeng]+)')
		res_pic = re.findall(second_p, second_content)
		post_link.append(res_pic[0])

# save to file
if SAVETOFILE:
	file=open('output','w')
	for each in post_link:
		#file.write("http://i.imgur.com/"+str(each)+'\n')
		file.write(str(each)+'\n')
	file.close()

quit( post_link)