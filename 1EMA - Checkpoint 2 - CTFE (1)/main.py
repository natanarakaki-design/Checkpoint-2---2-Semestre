import network
import urequests
import time
import json
from machine import Pin, I2C
from i2c_lcd import I2cLcd
from umqtt.simple import MQTTClient

# --- Configurações do Wi-Fi ---
SSID = "Wokwi-GUEST"
PASSWORD = ""

# --- Configurações da OpenWeather ---
API_KEY = "Chave_API"
CIDADE = "Sao%20Paulo"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

# --- Configurações MQTT ---
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_01"
MQTT_TOPIC = "fiap/iot/grupo01/clima"

# --- Inicialização do I2C e LCD ---
i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
lcd = I2cLcd(i2c, 0x27, 4, 20)

# --- Conexão Wi-Fi ---
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

lcd.clear()
lcd.putstr("Conectando Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

lcd.clear()
lcd.putstr("Wi-Fi Conectado!")
time.sleep(1)

# --- Conexão MQTT ---
lcd.clear()
lcd.putstr("Conectando MQTT...")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()

lcd.clear()
lcd.putstr("MQTT Conectado!")
time.sleep(1)

# --- Loop Principal ---
while True:
    try:
        response = urequests.get(URL)
        
        if response.status_code == 200:
            dados = response.json()
            
            cidade = str(dados["name"])
            temp = float(dados["main"]["temp"])
            umidade = int(dados["main"]["humidity"])
            descricao = str(dados["weather"][0]["description"])
            
            response.close()

            # 1. Atualização do LCD 20x4
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr(f"Cidade: {cidade[:12]}")
            
            lcd.move_to(0, 1)
            lcd.putstr(f"Temp: {temp:.1f} C")
            
            lcd.move_to(0, 2)
            lcd.putstr(f"Umidade: {umidade}%")
            
            lcd.move_to(0, 3)
            # Remove acentos para garantir exibição correta no LCD
            lcd.putstr(f"Tempo: {descricao[:13]}")

            # 2. Criação do Dicionário/JSON estruturado
            payload = {
                "cidade": cidade,
                "temperatura": temp,
                "umidade": umidade,
                "condicao": descricao
            }
            
            # Converte para JSON e garante codificação em bytes UTF-8 para o MQTT
            json_str = json.dumps(payload)
            client.publish(MQTT_TOPIC, json_str.encode('utf-8'))
            
            print("Publicado com sucesso:", json_str)
            
        else:
            print("Erro na API OpenWeather. Status:", response.status_code)
            response.close()

    except Exception as e:
        print("Erro durante a execucao:", e)

    # Tempo entre atualizações
    time.sleep(30)