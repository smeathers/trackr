import copy
import logging

import voluptuous as vol
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak
from homeassistant import config_entries, exceptions
#from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from .const import DOMAIN


class TrackrConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self._discovery_info: BluetoothServiceInfoBleak | None = None
        self._discovered_device: DeviceData | None = None
        self._discovered_devices: dict[str, Discovery] = {}
        
    #def _show_main_form(self, errors=None):
    #    return self._show_user_form("user", DOMAIN_SCHEMA, errors or {})
        
    async def async_step_user(self, user_input=None) -> ConfigFlowResult:
        return self.async_show_form()
