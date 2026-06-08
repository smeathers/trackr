import copy
import logging

import voluptuous as vol
from homeassistant.components.bluetooth import (
    BluetoothServiceInfoBleak,
    async_discovered_service_info,
)
from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from .const import DOMAIN


class TrackrConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    VERSION = 1

    def __init__(self) -> None:
        """Set up a new config flow for Aranet."""
        self._discovery_info: BluetoothServiceInfoBleak | None = None
        
    def _show_main_form(self, errors=None):
        return self._show_user_form("user", DOMAIN_SCHEMA, errors or {})
        
    async def async_step_user(self, info):
