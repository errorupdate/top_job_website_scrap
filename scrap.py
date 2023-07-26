from bs4 import BeautifulSoup
# with open('home.html','r') as html_file:
#     content = html_file.read()
    
#     soup=BeautifulSoup(content,'lxml')
#     # tags = soup.find_all('h5')
#     # for course in tags:
#     #     print(course.text)
#     course_cards = soup.find_all('div',class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
        
#         print(f'{course_name} costs{course_price}')
import time
import requests
print('Put some skill that you ar not famaliar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').text
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                # print(published_date)
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills:{skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f'File saved: {index}')
                    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait+60)
        