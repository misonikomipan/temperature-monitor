# temperature-monitor
raspberry piを用いたサーバー室の温度測定を行い、定期的にSlackに室温を送信する。
また、異常時にもSlackへ通知を行う。
## 作成者の環境
- Raspberry Pi 3B
- 温湿度センサ モジュールDHT11（https://akizukidenshi.com/catalog/g/g107003/）
## 使い方
### DHT11とラズパイの接続
- DHT11の1番：ラズパイの5V
- DHT11の2番：ラズパイのGPIO
- DHT11の4番：ラズパイのGND
### Slack
- 以下を参考にしてWebHookURLを発行し、main.pyに書き込んでください。
https://api.slack.com/messaging/webhooks

## 権利関係
DHT11で測定したデータをPythonで用いるにあたって、https://github.com/szazo/DHT11_Python.gitのスクリプトを利用させていただきました。
