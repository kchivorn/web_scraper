import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

class Fetcher:
  def __init__(self, query):
    self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    self.driver.wait = WebDriverWait(self.driver, 1)
    self.query = query

  def  lookup(self):
    self.driver.get("https://www.google.com.kh/search?hl=en-U")

    try:
      box = self.driver.wait.until(EC.presence_of_element_located(
        (By.NAME, "q")
      ))
      print(box)
      button = self.driver.wait.until(EC.element_to_be_clickable(
        (By.NAME, "btnK")))
      print(button)
      box.send_keys(self.query)
      box.send_keys(Keys.ENTER)
    except:
      print("Failed, bro")

    soup = BeautifulSoup(self.driver.page_source, "html.parser")

    with open("test.html", "w+") as f:
      f.write(str(soup))
      f.close()

    answer = soup.find_all("div", class_="_sPg")   #PhantomJS without list

    if not answer:
      print("looking at class _tZg")
      answer = soup.find_all("li", class_="_tZg")  #PhantomJS with list

    if not answer:
      answer = soup.find_all("div", class_="_XWk")  #Chrome without list

    if not answer:
      answer = soup.find_all("li", class_="_AXc")  #Chrome with list

    if not answer:
      answer = ["I don't know"]

    self.driver.quit()
    return summarize(answer)

def summarize(answer):
  sentences = ""
  if len(answer)==1:
    if answer[0] == "I don't know":
      return answer[0]
    else:
      return answer[0].get_text()
  for i, sentence in enumerate(answer):
    sentences += str(i+1)
    sentences += ". "
    sentences += sentence.get_text()

  return sentences
