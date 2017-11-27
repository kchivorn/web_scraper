import subprocess
import os
import requests
from bs4 import BeautifulSoup
from web_scraper import Fetcher

class Commander:
  def __init__(self):
    self.confirm = ["yes", "affirmative", "si", "sure", "ok", "do it", "yeah", "confirm", "of course", "certainly"]
    self.cancel = ["no", "negative", "never", "don't", "wait", "cancel"]

  def discover(self, text=""):
    if "what" in text and "name" in text:
      if "my" in text:
        self.respond("You havent told me your name yet")
      else:
        self.respond("My name is Artificial Intelligent. How are you?")
    else:
      f = Fetcher(text)
      answer = f.lookup()
      self.respond(answer)

    if "launch" or "open" in text:
      app = text.split(" ", 1)[-1]
      print(app)
      subprocess.call(app, shell=True)

  def respond(self, response):
    print(response)
    subprocess.call("say '" + response + "'", shell=True)

cmd = Commander()

cmd.discover("how to make apple pie")
