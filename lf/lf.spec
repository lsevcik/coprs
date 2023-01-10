%global goipath github.com/gokcehan/lf
%global tag r28
%global gomodulesmode GO111MODULE=auto
%gometa

%global _docdir_fmt %{name}

%global golicenses LICENSE
%global godocs README.md
%global godevelheader %{expand:
# The devel package will usually benefit from corresponding project binaries.
Requires:  %{name} = %{version}-%{release}
}
%global common_description %{expand:
lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger file manager.
}


Name:           lf
Version:        %{tag}
Release:        1%{?dist}
Summary:        Terminal file manager
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  go-srpm-macros git

%gopkg

%description
%{common_description}

%prep
%goprep

#%generate_buildrequires
#%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/lf %{goipath}

%install
%gopkginstall
install -vdm 0755 %{buildroot}/usr/share/man/man1
install -vdm 0755 %{buildroot}%{_bindir}
install -vDm 0755 lf.1 %{buildroot}/usr/share/man/man1
install -vDm 0755 %{gobuilddir}/bin/lf %{buildroot}%{_bindir}

%files
%license %{golicenses}
%doc %{godocs}
/usr/share/man/man1/lf.1.gz
%{_bindir}/*

%gopkgfiles

%changelog
* Tue Jan 10 2023 Logan Sevcik <logan@sevcik.email> r28-1
- r27 -> r28

* Sat Jun 04 2022 Logan Sevcik <logan@sevcik.email> r27-2
- new package built with tito

%autochangelog
