Name:           xpademu
Version:        0.0.0
Release:        1%{?dist}
Summary:        Generic gamepad to virtual Xbox 360 controller multiplexer.

License:        GPL-3.0-or-later
URL:            https://github.com/petr666/xpademu
Source0:        xpademu.tar.gz

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       python3-evdev
Requires:       python3-inotify

%description
xpademu is a lightweight, zero-CPU idle event-driven background service
that maps generic physical gamepads into virtual Microsoft Xbox 360 controllers.

%prep
%autosetup -n xpademu

%install
install -D -p -m 0755 xpademu %{buildroot}%{_bindir}/xpademu
install -D -p -m 0644 packaging/systemd/xpademu.service %{buildroot}%{_unitdir}/xpademu.service
install -D -p -m 0644 examples/thrustmaster_score_a.json %{buildroot}%{_sysconfdir}/xpademu.d/thrustmaster_score_a.json.example
install -D -p -m 0644 examples/xiaomi_gamepad.json %{buildroot}%{_sysconfdir}/xpademu.d/xiaomi_gamepad.json.example

%post
%systemd_post xpademu.service

%preun
%systemd_preun xpademu.service

%postun
%systemd_postun_with_restart xpademu.service

%files
%{_bindir}/xpademu
%{_unitdir}/xpademu.service
%dir %{_sysconfdir}/xpademu.d
%config(noreplace) %{_sysconfdir}/xpademu.d/thrustmaster_score_a.json.example
%config(noreplace) %{_sysconfdir}/xpademu.d/xiaomi_gamepad.json.example
%license LICENSE

%changelog
* Mon Nov 09 2026 Petr Bartos <bartos.petr@gmail.com> - 0.0.0-1
- Initial release
