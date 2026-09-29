# Checkpoint-2---2-Semestre
Integrantes do Grupo:
-Natan Arakaki - RM: 569224
-Ethan Rodrigues - RM: 569448
-Wilian Aquiles - RM: 571177

**Turma:** 1EMA

Este repositório contém os códigos e arquivos necessários para a resolução da tarefa "Checkpoint 2", baseada nas instruções do documento de referência **Atividade_ESP32_MicroPython_LCD_API_MQTT.pdf**.

## Descrição do Projeto

O objetivo desta atividade prática é desenvolver e testar aplicações de comunicação utilizando o microcontrolador ESP32 programado em MicroPython. O projeto explora três recursos fundamentais em sistemas de Internet das Coisas (IoT):
1. Controle de um display LCD via protocolo I2C.
2. Consulta de dados meteorológicos por meio de uma API HTTP (OpenWeather).
3. Comunicação via protocolo MQTT para envio de dados.

O repositório abrange desde a implementação individual de cada recurso até o "Desafio" final, que consiste na integração completa de todas as etapas.

## Objetivos e Etapas

- **Etapa 1: Display LCD 20x4:** Configuração do circuito no Wokwi e exibição de mensagens no display utilizando as bibliotecas `lcd_api.py` e `i2c_lcd.py`.
- **Etapa 2: Consulta à API OpenWeather:** Conexão à rede (Wokwi-GUEST), requisição HTTP utilizando `urequests` para obter o JSON da API e extração de dados como temperatura, umidade e condição do tempo.
- **Etapa 3: Comunicação MQTT:** Conexão ao broker público do HiveMQ e publicação periódica de dados em formato JSON, com visualização e assinatura do tópico através do Node-RED.
- **Desafio Integrado:** Aplicação unificada onde o ESP32 consulta os dados meteorológicos na OpenWeather, apresenta as informações no LCD 20x4 e publica esses dados em JSON via MQTT para serem visualizados em um dashboard/fluxo no Node-RED.

## Tecnologias e Ferramentas Utilizadas

*   **Hardware / Simulador:** ESP32 (via simulador [Wokwi](https://wokwi.com/))
*   **Linguagem:** MicroPython
*   **Protocolos:** I2C, HTTP/REST, MQTT
*   **APIs e Serviços:** OpenWeather API, HiveMQ (Broker MQTT Público)
*   **Integração:** Node-RED
