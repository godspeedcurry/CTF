from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
from tqdm import tqdm
from concurrent import futures
from fake_useragent import UserAgent

chrome_options = Options()
# chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

chrome_options.add_argument("start-maximized")
chrome_options.add_argument("enable-automation")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-gpu")
id_list = [i for i in range(0, 10000)]
with open('score.txt','r') as f:
	s = [int(x.split(',')[0]) for x in f.read().strip().split('\n')]
id_list = list(set(id_list) - set(s))
ua = UserAgent(use_cache_server=False)
bar = tqdm(total=len(id_list))

def spider(myid):

    global chrome_options
    chrome_options.add_argument(f"--user-agent={ua.random}")
    try:
        browser = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')
        browser.get(f'https://rarity.tools/boredapeyachtclub/view/{myid}')
        bar.update(1)
        sleep(20)
        browser.execute_script("window.stop()")
        source = browser.page_source
        browser.quit()
        rarity_score = float(re.findall('<div class="px-2 mx-1 mb-0 text-lg font-extrabold text-green-500 bg-white rounded-md dark:bg-gray-800">(.*?)</div>',source,re.I|re.M|re.S)[0].strip())
        token_id = int(re.findall('<div class="flex-grow text-sm text-right text-gray-400"><span class="font-normal">ID</span>(.*?)</div>',source,re.I|re.M|re.S)[0].strip())
        print(f"{token_id},{rarity_score}")
        with open("score.txt","a") as f:
            f.write(f"{token_id},{rarity_score}\n")

    except Exception as e:
        print(myid,e)

with futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(spider, id_list))
