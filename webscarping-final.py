from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
from urllib.request import urlopen, Request



webpage = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url=webpage, headers = headers)

page = urlopen(req)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

