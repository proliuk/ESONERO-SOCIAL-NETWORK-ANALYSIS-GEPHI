from selenium import webdriver
import pandas
import json
number_of_pages = 91 #adattarlo al numero che restituisce il sito
google_path = r"chromedriver.exe"
driver = webdriver.Chrome(google_path)
driver.get("https://ricerca.repubblica.it/ricerca/repubblica?query=conte&fromdate=2020-01-07&todate=2020-02-07&sortby=score&author=&mode=any")
articles_list=[]
for page in range(number_of_pages):
    try:
        articles = driver.find_elements_by_tag_name("article")
        for i in articles:
            article={}
            title = i.find_element_by_tag_name("h1")
            article['title'] = title.text
            articles_list.append(article)
    #get the address from the "next" button
        navbar = driver.find_elements_by_class_name("pagination")
        pages_links = navbar[0].find_elements_by_tag_name("li")
        address = pages_links[-1].find_element_by_tag_name("a").get_attribute("href")
        print(address)
        with open("title.json","w") as json_file:
            json.dump(articles_list, json_file)
        driver.get(address)
    except:
        driver.close()
driver.close()
pandas.read_json("title.json").to_csv("titlerepubblica.csv",index=False)
