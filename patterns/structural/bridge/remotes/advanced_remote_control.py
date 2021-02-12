from .remote_control import RemoteControl


class AdvancedRemoteControl(RemoteControl):
    def mute(self) -> None:
        self._device.set_volume(0)
