import pytest

from patterns.structural.bridge.devices.device import Device
from patterns.structural.bridge.remotes.remote_control import RemoteControl


class NewDevice(Device):
    def __init__(self) -> None:
        self._enabled = False
        self._volume = 0
        self._channel = 0

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume_level: int) -> None:
        self._volume = volume_level

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = channel


class TestRemoteControl:
    @pytest.fixture()
    def remote_control(self, new_device: Device) -> RemoteControl:
        return RemoteControl(new_device)

    @pytest.fixture()
    def new_device(self) -> Device:
        return NewDevice()

    def test_toggle_power(
        self, new_device: Device, remote_control: RemoteControl
    ) -> None:
        new_device.disable()

        remote_control.toggle_power()
        assert new_device.is_enabled()

        remote_control.toggle_power()
        assert not new_device.is_enabled()

    def test_volume_up(self, new_device: Device, remote_control: RemoteControl) -> None:
        base_volume = 0
        new_device.set_volume(base_volume)

        remote_control.volume_up()
        assert new_device.get_volume() > base_volume

    def test_volume_down(
        self, new_device: Device, remote_control: RemoteControl
    ) -> None:
        base_volume = 10
        new_device.set_volume(base_volume)

        remote_control.volume_down()
        assert new_device.get_volume() < base_volume

    def test_channel_down(
        self, new_device: Device, remote_control: RemoteControl
    ) -> None:
        base_channel = 10
        new_device.set_channel(base_channel)

        remote_control.channel_down()
        assert new_device.get_channel() < base_channel

    def test_channel_up(
        self, new_device: Device, remote_control: RemoteControl
    ) -> None:
        base_channel = 0
        new_device.set_channel(base_channel)

        remote_control.channel_up()
        assert new_device.get_channel() > base_channel
