# Raspberry Pi Pico : Experiment Codes

RaspberryPi Pico experiment source code.

## Description

## Requirement

## Usage

```text
pico-experiment
  +- micropython-basic      : Pico だけで動作する MicroPython のサンプルコード
  |   +- led.py             : Pico 本体の LED を点滅させる(Lチカ)コード
  |   +- get-sensor.py      : Pico 本体の 温度センサーを読み取りコンソール表示
  |   +- i2c-scan.py        : I2C 0,1 をスキャンし接続しているデバイス情報を表示
  |
  +- micropython
  |   +- bme280-lcd         : BME280 で WBGT簡易測定 8x2 LCD に情報表示
  |   |   +- main.py        : メインの処理
  |   |   +- ST7032.py      : 8x2 LCD 制御ライブラリ
  |   |
  |   +- ae-kit45-keypad4x3 : KEYPAD 4x3 キットを使用した基本的な動作確認
  |   |   +- keypad4x3.py   : KEYPAD 4x3 の動作確認プログラム
  |   |
  |   +- thermistor         : 103JT-025/050 サーミスターを使用した温度測定コード
  |   |   +- main.py        : 103JT-025/050 サーミスター温度測定コード
  |
  +- circuitpython
  |   +- 3d-mouse
  |   |   +- code.py        : KXM52-1050 を使用した3Dマウス 実装例
  |   |
  |   +- shortcut
  |   |   +- code.py        : adafurit HID キーボードエミュレーション
  |   |
```

## Install

## Future plans

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

* [incmplt](https://www.incmplt.net/)
* [Info Circus,Inc.](https://www.infocircus.jp/)
