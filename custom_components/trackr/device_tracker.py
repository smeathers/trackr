from homeassistant.components.device_tracker import SourceType
from homeassistant.components.device_tracker.config_entry import ScannerEntity
from homeassistant.helpers.restore_state import RestoreEntity

class BleScannerEntity(ScannerEntity, RestoreEntity):
    """Represent a tracked device."""
  
    @property
    def source_type(self) -> SourceType:
        """Return the source type, eg gps or router, of the device."""
        return SourceType.BLUETOOTH_LE
