# The MIT License (MIT)
# Copyright (c) 2023 Edgaras Janušauskas and Inovatorius MB (www.fildz.com)

################################################################################
# FILDZ CYBEROS BUTTON API
#
# Button API for "fildz_button" library.

# TODO:
#  1. Lazy loading of API events could be useful in some cases because you may not need all the events.

import uasyncio as asyncio
from uasyncio import Event
import fildz_cyberos as cyberos


class ButtonAPI:
    def __init__(self, cyberware):
        self._cyberware = cyberware
        self._on_down = Event()
        self._on_hold = Event()
        self._on_up = Event()
        self._on_click = Event()
        self._on_double_click = Event()
        asyncio.create_task(self.push())

    ################################################################################
    # Events
    #
    @property
    def on_down(self):
        return self._on_down

    @on_down.setter
    def on_down(self, value):
        asyncio.create_task(cyberos.event.push(self._cyberware, 'on_down', value))

    @property
    def on_hold(self):
        return self._on_hold

    @on_hold.setter
    def on_hold(self, value):
        asyncio.create_task(cyberos.event.push(self._cyberware, 'on_hold', value))

    @property
    def on_up(self):
        return self._on_up

    @on_up.setter
    def on_up(self, value):
        asyncio.create_task(cyberos.event.push(self._cyberware, 'on_up', value))

    @property
    def on_click(self):
        return self._on_click

    @on_click.setter
    def on_click(self, value):
        asyncio.create_task(cyberos.event.push(self._cyberware, 'on_click', value))

    @property
    def on_double_click(self):
        return self._on_double_click

    @on_double_click.setter
    def on_double_click(self, value):
        asyncio.create_task(cyberos.event.push(self._cyberware, 'on_double_click', value))

    ################################################################################
    # Tasks
    #
    async def push(self):
        await cyberos.event.push(self._cyberware, 'on_down', self._on_down)
        await cyberos.event.push(self._cyberware, 'on_hold', self._on_hold)
        await cyberos.event.push(self._cyberware, 'on_up', self._on_up)
        await cyberos.event.push(self._cyberware, 'on_click', self._on_click)
        await cyberos.event.push(self._cyberware, 'on_double_click', self._on_double_click)

    async def pull(self):
        await cyberos.event.pull(self._cyberware)
