# FILDZ CYBEROS Button API

Button API for [FILDZ CYBEROS Button](https://github.com/fildz-official/FILDZ_CYBEROS_Button) library.

## Setup

1. Download and extract .zip file contents to fildz_button_api folder.
2. Upload fildz_button_api folder to your MicroPython powered device.

## Usage

### Coroutine + Property:

```Python
import uasyncio as asyncio
import fildz_cyberos as cyberos
from fildz_button_api import ButtonAPI


async def btn_clicked():
    print('Button clicked')

async def main():
    await cyberos.init()
    btn = ButtonAPI('BUTTON-0F889A-ABW')  # Listen for events from this cyberware. 
    btn.on_click = btn_clicked  # Once "on_click" event received, run btn_clicked() coroutine.
    await cyberos.run_forever()

asyncio.run(main())
```

### Coroutine + Task + Event:

```Python
async def btn_clicked(btn):
    while True:
        await btn.on_click.wait()
        print('Button clicked')
        btn.on_click.clear()

async def main():
    await cyberos.init()
    btn = ButtonAPI('BUTTON-0F889A-ABW')
    asyncio.create_task(btn_clicked(btn))
    await cyberos.run_forever()

asyncio.run(main())
```

## Documentation

The documentation for this library is currently a work in progress. It will be available soon to provide detailed explanations of the library's API, usage examples, and best practices.

## Contributing

FILDZ CYBEROS is an open-source project that thrives on community contributions. We welcome developers to contribute to the project by following the MIT license guidelines. Feel free to submit pull requests, report issues, or suggest enhancements to help us improve the project further.

## Acknowledgment 

We are immensely thankful to the [MicroPython](https://github.com/micropython/micropython) community for developing and maintaining this incredible open-source project. Their dedication and hard work have provided us with a powerful and versatile platform to build upon.
