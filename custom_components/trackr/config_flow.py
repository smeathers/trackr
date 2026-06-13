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
    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface."""
        errors: Dict[str, str] = {}
    
        return self.async_show_form(
            step_id="user", data_schema=AUTH_SCHEMA, errors=errors
        )
