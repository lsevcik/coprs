Name:           usbboot
Version:        2022.05.27
Release:        0%{?dist}
Summary:        Raspberry Pi USB booting code

License:        Apache2
URL:            https://github.com/raspberrypi/usbboot
Source0:        https://github.com/raspberrypi/usbboot/archive/master.tar.gz
Patch0:         01-makefile.patch

BuildRequires:  libusb1-devel make gcc

%description
Raspberry Pi USB booting code

%prep
%autosetup -n usbboot-master


%build
%make_build


%install
%make_install


%check


%files
%{_bindir}/rpiboot
/usr/share/rpiboot
%license
%doc


%changelog
