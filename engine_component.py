from requests_html import HTMLSession
import pandas as pd
import time

# converting the code it into fucntion
def get_ai_response(url):
    url = url.replace(" ", "+")
    new_session = HTMLSession()
    new_r = new_session.get("https://iask.ai/?mode=question&q={}".format(url))
    new_r.html.render(sleep = 5)  #type: ignore 

 
    # getting the name of the company
    company = new_r.html.xpath('/html/body/div/main/section/div[1]/div[3]',first = True)  #type: ignore
    response  = company.text
    new_session.close()
    
    return response 

#if __name__ == '__main__':    print(get_ai_response("Gwalior"))