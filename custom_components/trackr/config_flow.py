import copy
import logging

import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN


class TrackrConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    def _show_main_form(self, errors=None):
        return self._show_user_form("user", DOMAIN_SCHEMA, errors or {})
        
    async def async_step_user(self, info):
