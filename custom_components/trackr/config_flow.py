from homeassistant import config_entries
from .const import DOMAIN


class TrackrConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
