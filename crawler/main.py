from bs4 import BeautifulSoup
info = []
with open('C:\\Users\\Administrator\\PycharmProjects\\crawler\\sample.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > h3')
    descs = Soup.select('body > div.main-content > ul > li > p')
    print(images,titles,descs)

for image,title,desc in zip(images,titles,descs):
    data = {
        'image':image.get('src'),
        'title':title.get_text(),
        'desc':desc.get_text()
    }
    info.append(data)

for i in info:
    if float(i[image]>3):
        print(i['image'],i['title'],i['desc'])