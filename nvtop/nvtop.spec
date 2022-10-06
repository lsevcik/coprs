Name:           nvtop
Version:        2.0.4
Release:        1

Summary:        AMD and NVIDIA GPUs htop like monitoring tool
License:        GPL
URL:            https://github.com/Syllo/%{name}
Source0:        https://github.com/Syllo/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:      x86_64 aarch64 armhfp ppc64le s390x
BuildRequires:  libdrm-devel ncurses-devel cmake gcc-c++ git


%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD and
NVIDIA GPUs. It can handle multiple GPUs and print information about them in a
htop familiar way.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
/usr/share/applications/nvtop.desktop
/usr/share/icons/nvtop.svg

%changelog
* Thu Oct 06 2022 Logan Sevcik <logan@sevcik.email> 2.0.4-1
- nvtop 2.0.3 -> 2.0.4

* Fri Aug 26 2022 Logan Sevcik <logan@sevcik.email> 2.0.3-1
- nvtop 2.0.2 -> 2.0.3

* Sun Jun 12 2022 Logan Sevcik <logan@sevcik.email> 2.0.2-2
- nvtop pkgrel 1 -> 2 (logan@sevcik.email)

* Sun Jun 12 2022 Logan Sevcik <logan@sevcik.email> 2.0.2-1
- nvtop 2.0.1 -> 2.0.2 (logan@sevcik.email)

* Wed May 18 2022 Logan Sevcik <logan@sevcik.email> 2.0.1-1
- new package built with tito
