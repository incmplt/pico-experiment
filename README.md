# Raspberry Pi Pico : Experiment Codes

RaspberryPi Pico experiment source code.

## Description

## Requirement

## Usage

```text
pico-experiment
  +- micropython-basic     : Pico だけで動作する MicroPython のサンプルコード
  |   +- led.py            : Pico 本体の LED を点滅させる(Lチカ)コード
  |   +- get-sensor.py     : Pico 本体の 温度センサーを読み取りコンソール表示
  |   +- i2c-scan.py       : I2C 0,1 をスキャンし接続しているデバイス情報を表示
  |
  +- micropython
  |   +- bme280-lcd        : BME280 で WBGT簡易測定 8x2 LCD に情報表示
  |   |   +- main.py       : メインの処理
  |   |   +- ST7032.py     : 8x2 LCD 制御ライブラリ
```

## Install

## Future plans

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

* [incmplt](https://www.incmplt.net/)
* [Info Circus,Inc.](https://www.infocircus.jp/)
