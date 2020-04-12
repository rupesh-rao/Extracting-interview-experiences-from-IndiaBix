from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

def page_soup(url):
    req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    furl = urlopen(req)
    html = furl.read()
    furl.close()
    soup = BeautifulSoup(html,'html.parser')
    return soup

url = 'https://www.indiabix.com/placement-papers/companies/'
soup = page_soup(url)
containers = soup.findAll('ul')
f = open('inter_exp.csv','a',encoding = 'utf-8')
headers='Company_Name,  Experience of, Keywords, Title_of_Experience, URL, Interview_Experience\n'
#f.write(headers)
        
c=0
for i in range(2):
    container = containers[i].findAll('a')
    print(len(container))
    for contain in container:
        company_name = contain.text
        url = 'https://www.indiabix.com' + contain['href']
        soup = page_soup(url)
        ul = soup.findAll('ul')
        interviews = ul[0].findAll('li')
        print()
        print(len(interviews))
        print()
        
        for interview in interviews:
            c+=1
            info = interview.a.text         
            new_url = 'https://www.indiabix.com' + interview.a['href']
            interview_soup = page_soup(new_url)
            
            name_class = interview_soup.findAll('div',{'class':'div-paper-view-notes mx-gray'})
            name = name_class[0].span.text
            
            meta = interview_soup.findAll('meta',{'name':'keywords'})
            keywords = meta[0]['content']
            
            data_class = interview_soup.findAll('div',{'class':'div-paper-data'})
            data = data_class[0].text.replace('\n','|')
            print(c)

            f.write(company_name + ',' + name + ',' + keywords.replace(',','|') + ',' + info.replace(',','|') + ',' + new_url + ',' + data.replace(',','|') +'\n' )

    
f.close()




