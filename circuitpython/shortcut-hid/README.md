# CircuitPython HID sample.

![RaspberryPi Pico HID Sample](shortcut-hid.png)

## Requirement

* RaspberryPi pico
* CircuitPython
* usb_hid module
* adafruit_hid module
* タクトスイッチ
  https://akizukidenshi.com/catalog/g/gP-03648/

# Usage

タクトスイッチと、押したときの HIDエミュレーションは以下の通り。

| Pin | Comment |
|---|---|
| GP2 | タクトスイッチ / ALT + PrintScreen |
| GP3 | タクトスイッチ / Win + PrintScreen |
| GP4 | タクトスイッチ / ESCAPE |

# Install

CircuitPython をインストールした RaspberryPi Pico に、adafruit_hid モジュールと main.py をコピーして実行。

## Reference

[RaspberryPi Pico Setup:incmplt](https://www.incmplt.net/2022/09/10/raspberrypi-pico-setup/)

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

* [incmplt](https://www.incmplt.net/)
* [Info Circus,Inc.](https://www.infocircus.jp/)
