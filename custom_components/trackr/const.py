from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

DOMAIN = "trackr"
# Platforms
PLATFORMS = [
    Platform.DEVICE_TRACKER,
    Platform.BUTTON
]
