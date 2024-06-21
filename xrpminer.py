#!/usr/bin/python3
try:
  from requests.exceptions import RequestException
  from rich.console import Console
  import requests, time, os, json
  from rich.panel import Panel
  from rich import print
  from random import choice
  from fake_useragent import UserAgent
  from bs4 import BeautifulSoup
except (Exception) as e:
  exit(f"[Error]{str(e).capitalize()}!")

cookies, success, failed = [], [], []

url_proxies = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"

class Xrpminer:
  def __init__(self) -> None:
    pass
  
  def success(self, email, data):
    for item in success:
      if item['email'] == email:
        item['data'].append(data)
        break
      
  def failed(self, email, data):
    for item in failed:
      if item['email'] == email:
        item['data'].append(data)
        break
  
  def check(self, email):
    for item in cookies:
      if item['email'] == email:
        return True
      else:
        return False
        
  def count_time(self):
    for sleep in range(60, 0, -1):
      print(f"[bold bright_black]   ╰─>[bold green] {sleep}s[/]     ", end='\r')
      time.sleep(1)

  def count_sc(self, email):
    for item in success:
      if item['email'] == email:
        return len(item["data"])
  
  def count_fl(self, email):
    for item in failed:
      if item['email'] == email:
        return len(item["data"])

  def execution(self, email, reqsesion):
    with reqsesion as r:
      user_agent = UserAgent().random
      proxies_response = requests.get(url_proxies)
      proxies = proxies_response.text.split('\n')
      proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
      proxy = {'http':  choice(proxies)}
      r.headers.update({
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'dnt': '1',
        'Connection': 'keep-alive',
        'User-Agent': user_agent,
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-User': '?1',
        'Referer': 'https://faucetearner.org/dashboard.php',
        'Host': 'faucetearner.org',
      })
      response = r.get('https://faucetearner.org/faucet.php', proxies=proxy)
      r.headers.update({
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Host': 'faucetearner.org',
        'Origin': 'https://faucetearner.org',
      })
      response2 = r.post('https://faucetearner.org/api.php?act=faucet', data={}, proxies=proxy)
      response3 = r.post('https://faucetearner.org/dashboard.php', proxies=proxy)
      balance = BeautifulSoup(response3.content, 'html.parser')
      balance = balance.find_all("b", "fs-4")[0].text.strip()
      if 'congratulations' in str(response2.text).lower():
        try:
          xrp_earn = (str(response2.text).split(' XRP')[0].split('0.')[1])
        except (IndexError):
          xrp_earn = "0.000000"
        self.success(email, xrp_earn)
        return({
          "success": "1",
          "key": xrp_earn,
          "balance": balance
        })
      elif 'you have already' in str(response2.text).lower():
        xrp_earn = "0.000000"
        self.failed(email, xrp_earn)
        return({
          "success": "2",
          "key": xrp_earn,
          "balance": balance
        })
      else:
        return({
          "success": "0",
          "key": "0",
          "balance": "0"
        })
        
  def login(self):
    with open('accounts.json') as json_file:
      data = json.load(json_file)
        
    for account in data:
      email = account['email']
      url_proxies = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
      user_agent = UserAgent().random
      proxies_response = requests.get(url_proxies)
      proxies = proxies_response.text.split('\n')
      proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
      proxies = {'http':  choice(proxies)}
      #if not self.check(email):
      session = requests.Session()
      session.headers.update({
        'Accept': 'application/json',
        'User-Agent': user_agent
      })
      session.post("https://faucetearner.org/api.php?act=login", json={
        "email": email,
        "password": account['password']
      }, proxies=proxies)
      #session.get("https://faucetearner.org/dashboard.php", proxies=proxies)
      #cookie = session.cookies.get_dict()["user"]
      #cookie = cookie.split("-")[0]
      cookies.append({
        "email": email
      })
      success.append({
        "email": email,
        "data": []
      })
      failed.append({
        "email": email,
        "data": []
      })
      #else:
        #cookie = next(item["key"] for item in cookies if item["email"] == email)
      #print(cookie)
      execut = self.execution(email, session)
      balance = execut["balance"]
      if execut["success"] == "1":
        print(Panel(f"""
[bold white]Balance : {balance}[/]
[bold white]Success : {self.count_sc(email)}[/]
[bold white]Failed : {self.count_fl(email)}[/]
[bold white]Claim/Min : {execut["key"]} XRP[/]
[bold white]Status :[/] [bold green]Success[/]""", style="bold bright_black", width=56, title=f">>> [bold green]{email}[/] <<<"))
      elif execut["success"] == "2":
        print(Panel(f"""
[bold white]Balance : {balance}[/]
[bold white]Success : {self.count_sc(email)}[/]
[bold white]Failed : {self.count_fl(email)}[/]
[bold white]Claim/Min : {execut["key"]} XRP[/]
[bold white]Status :[/] [bold green]Failed[/]""", style="bold bright_black", width=56, title=f">>> [bold red]{email}[/] <<<"))
      else:
        print(Panel(f"""
[bold white]Balance : - XRP[/]
[bold white]Success : -[/]
[bold white]Failed : -[/]
[bold white]Claim/Min : - XRP[/]
[bold white]Status :[/] [bold red]Error[/]""", style="bold bright_black", width=56, title=f">>> [bold red]{email}[/] <<<"))
    self.count_time()
    self.login()

  def run(self):
    try:
      print(Panel(f"[italic white]XRP token mining is underway. You can stop the process at any time by pressing CTRL + Z keys.[/]", style="bold bright_black", width=56, title=">>> Note <<<"))
      try:
        self.login()
      except (RequestException):
        print("[bold bright_black]   ╰─>[bold red] No internet!", end='\r')
        time.sleep(10.5)
        self.login()
      except (KeyboardInterrupt):
        print("                                                       ", end='\r')
        time.sleep(2.5)
        self.login()
    except (Exception) as e:
      print(Panel(f"[italic red]{str(e).capitalize()}!", style="bold bright_black", width=56, title=">>> Error <<<"))
      exit()

if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear')
  getIp = requests.get("https://api.myip.com").json()
  ip = getIp["ip"]
  print(Panel(f"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold green]
  __  ______  ____  __  __ _                 
  \ \/ /  _ \|  _ \|  \/  (_)_ __   ___ _ __ 
   \  /| |_) | |_) | |\/| | | '_ \ / _ \ '__|
   /  \|  _ <|  __/| |  | | | | | |  __/ |   
  /_/\_\_| \_\_|   |_|  |_|_|_| |_|\___|_|   

          [italic white on red]You IP : {ip}""", style="bold bright_black", width=56))
  try:
    Xrpminer().run()
  except (KeyboardInterrupt, KeyboardInterrupt):
    exit()