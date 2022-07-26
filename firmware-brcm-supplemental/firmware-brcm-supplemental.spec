Name:           firmware-brcm-supplemental
Version:        1.3
Release:        0%{?dist}
Summary:        Broadcom brcm Supplemental Firmware

License:        Proprietary
URL:            https://github.com/bsdkurt/brcm-supplemental
Source0:        https://github.com/bsdkurt/brcm-supplemental/archive/refs/tags/brcm-supplemental-%{version}.tar.gz

BuildArch: noarch

%description
This repository contains board specific firmware & NVRAM for Broadcom brcm
devices. File names have been renamed to be board specific which aligns with
how OpenBSD's bwfm driver loads them.

%prep
%autosetup -n brcm-supplemental-brcm-supplemental-%{version}

%install
install -vdm0755 %{buildroot}/usr/lib/firmware/brcm
install -vm0644 brcm* %{buildroot}/usr/lib/firmware/brcm


%files
/usr/lib/firmware/brcm/*
%license LICENSE
%doc README.md

%changelog

