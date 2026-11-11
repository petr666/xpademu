# xpademu

A lightweight tool (and background service) that translates any generic physical gamepad into a virtual Microsoft Xbox 360 controller using `evdev` and `inotify`.

## Why `xpademu`?

* **Steam Input isn't always an option** (non-Steam games, standalone emulators, native apps).
* **Native Xbox support just works** out-of-the-box in most modern games if a compatible controller is present.
* **Existing tools have issues with:** 
  * bluetooth reconnection and device drop issues.
  * mapping of digital buttons to analog axes (essential for cheap gamepads with digital shoulder buttons instead of analog triggers).
  * mapping of some extra gamepad buttons (e.g. to the Xbox Guide button).
* **Device Masking:** Unlike other tools that leave underlying device nodes exposed, `xpademu` creates a permanent virtual Xbox pad and actively unlinks the physical device's original `eventX` and `jsX` nodes from `/dev/input/`. This prevents games from accidentally grabbing the raw physical device instead of the mock controller, eliminating random control conflicts and disconnection bugs.

> *Disclaimer:* While built to solve real pain points, this project was also made for fun. And frankly, it was faster to hack it together (with some help of Gemini) than spending hours searching for a tool that got everything right or trying to fix them :o)

## Preparing Configuration Files

`xpademu` uses JSON configuration files. Each configuration file represents **one emulated virtual Xbox 360 controller**. You can run multiple configuration files simultaneously using the same `xpademu` instance to create multiple independent virtual Xbox controllers.

Furthermore, a **single configuration file can contain multiple physical devices** mapped into that same virtual Xbox controller. This allows you to combine split inputs (such as a custom arcade stick layout or a separate throttle and wheel) into a unified virtual pad.

Some configuration examples can be found [**here**](examples). Names of inputs and ranges for the device axes to be mapped can be found, for example, using the [`evtest`](https://github.com/freedesktop-unofficial-mirror/evtest) tool.

## Usage

When started, `xpademu` immediately creates a fake Xbox controller device and waits for configured device(s) to be connected.

When a device disconnects, the Xbox controller device is not removed and `xpademu` is just waiting again for reconnection of the device.

### 1. Direct Execution
Run the script directly by passing your JSON configuration file(s):

```bash
sudo xpademu <config1.json> [<config2.json> ...]
```

### 2. Systemd Service Integration
`xpademu` integrates with systemd to run automatically in the background:

```bash
# Enable and start the service
sudo systemctl enable --now xpademu.service

# View xpademu logs
sudo journalctl -u xpademu.service -f
```

Configuration is loaded from `/etc/xpademu.d/*.json`.

## Maintenance & Contributions

This project serves my personal setup needs as is. 

* If you want changes, please submit a merge request with a patch.
* Alternatively, feel free to fork it, or just tweak it in place for your needs - after all, it is just a simple Python script ;o)

## License

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
