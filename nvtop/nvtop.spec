Name:           nvtop
Version:        2.0.1
Release:        1

Summary:        AMD and NVIDIA GPUs htop like monitoring tool
License:        GPL
URL:            https://github.com/Syllo/%{name}
Source0:        https://github.com/Syllo/%{name}/archive/refs/tags/%{version}.tar.gz

BuildArch:      x86_64 aarch64 armhfp ppc64le s390x
BuildRequires:  libdrm-devel ncurses-devel cmake gcc git


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

%changelog
* Wed May 18 2022 Logan Sevcik <logan@sevcik.email> 2.0.1-1
- new package built with tito

