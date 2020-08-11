from bs4 import BeautifulSoup
import requests

def main():
    main_url = "http://shopee.co.id"
    r1 = requests.get(main_url)
    soup = BeautifulSoup(r1.text, 'html.parser')
    r1_script_array = soup.find_all('script')
    
    all_script = []
    for item in r1_script_array:
        if item.get('src'):
            all_script.append(item.get('src'))
        
    for script_js in all_script:
        t = requests.get(script_js).text
        print(t)

if __name__=="__main__":
    main()
