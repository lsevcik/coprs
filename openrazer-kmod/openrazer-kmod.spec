%define buildforkernels akmod
%define debug_package %{nil}

Name:          openrazer-kmod

Version:       3.5.0
Release:       1%{?dist}
Summary:       OpenRazer kernel module

Group:         System Environment/Kernel

License:       GPL2
URL:           https://openrazer.github.io
Source0:       https://github.com/openrazer/openrazer/archive/refs/tags/v%{version}.tar.gz

BuildRequires: %{_bindir}/kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null
%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    cp -a openrazer-%{version} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*}/driver \
        modules
done


%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p $RPM_BUILD_ROOT%{kmodinstdir_prefix}${kernel_version%%___*}%{kmodinstdir_postfix}
    install -D -m 0755 _kmod_build_${kernel_version%%___*}/driver/razer*.ko \
         $RPM_BUILD_ROOT%{kmodinstdir_prefix}${kernel_version%%___*}%{kmodinstdir_postfix}
done
mkdir -p $RPM_BUILD_ROOT/usr/lib/udev/rules.d
install -Dm 755 openrazer-%{version}/install_files/udev/razer_mount $RPM_BUILD_ROOT/usr/lib/udev
install -Dm 644 openrazer-%{version}/install_files/udev/99-razer.rules $RPM_BUILD_ROOT/usr/lib/udev/rules.d
%{?akmod_install}

%clean
rm -rf $RPM_BUILD_ROOT

%package common
Summary: Meta-package for user-space openrazer tools
Group: System Environment/Kernel
Requires: openrazer-daemon
Requires: python3-openrazer
Conflicts: openrazer-meta
Provides: openrazer-kernel-modules-dkms

%description common
This meta-package exists because "this standard is stupid"
and won't let me not have a -common package 😡

%files common
/usr/lib/udev/razer_mount
/usr/lib/udev/rules.d/99-razer.rules

%changelog
* Thu Dec 01 2022 Logan Sevcik <logan@sevcik.email> 3.5.0-1
- 3.4.0 -> 3.5.0

* Sun Jul 31 2022 Logan Sevcik <logan@sevcik.email> 3.4.0-1.1
- Release 3.4.0

* Sun Jun 05 2022 Logan Sevcik <logan@sevcik.email> 3.3.0-1.2
- new package built with tito

