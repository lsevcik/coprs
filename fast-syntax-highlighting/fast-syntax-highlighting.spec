Name:           fast-syntax-highlighting
Version:        1.55
Release:        0%{?dist}

Summary:        Feature-rich syntax highlighting for ZSH
License: BSD
URL: https://github.com/zdharma-continuum/%{name}
Source0: https://github.com/zdharma-continuum/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

%description
Feature rich syntax highlighting for Zsh.

%prep
%autosetup

%install
mkdir -p %{buildroot}/usr/share/zsh/plugins/%{name} %{buildroot}/usr/share/licenses/%{name} %{buildroot}/usr/share/doc/%{name}
cp LICENSE %{buildroot}/usr/share/licenses/%{name}
cp README.md THEME_GUIDE.md %{buildroot}/usr/share/doc/%{name}
cp -r ./ %{buildroot}/usr/share/zsh/plugins/%{name}

%check

%files
%license LICENSE
%doc README.md THEME_GUIDE.md
/usr/share/zsh/plugins/fast-syntax-highlighting


%changelog
* Tue May 17 2022 Logan Sevcik <logan@sevcik.email> 1.55-1
- new package built with tito
