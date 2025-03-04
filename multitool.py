import requests
import os
import colorama
from colorama import Fore, Style
from pystyle import Center

black = "\033[1;30m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
invalidurl = f"{red}[! webhook multitool !]{white} invalid url"



os.system("cls")
print("                      funnytool \n")
webhook = input("webhook:")
username = input("username:")
avatar_url = input("avatar (leave blank if u want):")
content = input("message:")

data={
    "content": content,
    "username": username,
    "avatar_url": avatar_url
}
os.system("title webhook multifunny")
os.system("cls")

print(Center.XCenter(f""" {Fore.LIGHTBLACK_EX}                                   .=*.       .++:                            .++.                 
                             ...    .+#:....   .*#: ..       ...        ...    .#*:                 
           .#*:..=#*. .+#-..+#%%#+...+%+#%%#=. .*#*#%%#-. .:*#%%#=.. .-#%%%#-. .#*: .+#=.           
            =%=..#%%-.:%*.:##:..:#*..+%*...=%*..*%=..:*%:.-%#:..-%*..=%+. .+%+..#*:=%*:.            
            .*#.=#=##:+%-.+%*++++#%-.+%:   .*#-.*#:  .+%-.*%:   .=%-.#*.   .##:.#%#%+.              
            .-%=#*.=%+#*..+%+::::::..+%-   .*#:.*#:  .+%-.+%-.  .+%-.##.   .##:.##=*%+..            
            ..*%%-..#%#: .:#%=..-#*..+%#-.:*%+..*#:  .+%-.:##-.:+%+..=%*:.:#%=..#*:.-%#:            
             .-*+.  :*=.   .-*##*=...=*:+##*:. .++:  .=*:  .-*##*:.  ..+###+.. .*+. .:+*:           
                                                                                                    
                                                                                                    
                                                                                                    
                                        ....       ....                           ....              
                                        .+#: .--. .=%*..:-.                       :#*.              
              ........ .....  ....  .....+#:.:*#........*#-..  .....      .....   :##.              
              .#%#%%%**%#%%*. -%*.  .#*..+#:-#%%%*:-%+-#%%%#:.=%%%%%*:. .+%%%%%=..:##.              
              .#%-. :%*. .+%- -%*.  .#*..+#: :*#.  -%+..*#: .=%+. .:##:.*#-. .=%*.:##.              
              .##:  :%+. .+%- -%*.  .#*..+#: :*#.  -%+..*#: .*#:   .+%-:%*.   .##::##.              
              .##:  :%+. .+%- -%*.  :#*..+#: :*#.  -%+..*#: .+%-   .*#-.##:. .:%#.:##.              
              .##:  :%+. .+%- .*%*=+#%*..+#: .*%+-.-%+..+%+=.:*%+-=#%=. :##=-+##: :##.              
              .--.  .-:. .:-.  .:==-.--..:-. ..-=-..-:. .:==. .:===-..  ..:===:.  .--.          {Fore.RESET}     """))

print(f'{Fore.LIGHTMAGENTA_EX}Username: {username}')
print(f'Message: {content} \n')
print("1.Spam Webhook")
print(f"2.Delete Webhook {Style.RESET_ALL}")

tool_picked = input("")
if tool_picked is "1":
    while True:
        requests.post(webhook, json = data)
elif tool_picked is "2":
    requests.delete(webhook)


# requests.post(webhook, json = data)

