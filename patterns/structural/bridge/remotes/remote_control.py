from patterns.structural.bridge.devices.device import Device


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self._device = device

    def toggle_power(self) -> None:
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self) -> None:
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self) -> None:
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self) -> None:
        self._device.set_channel((self._device.get_channel() - 10))

    def channel_up(self) -> None:
        self._device.set_channel((self._device.get_channel() + 10))
