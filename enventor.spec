
%define	git 20211205

Summary:        Enlightenment edc editor
Name: 	        enventor
Version:        1.0.0
Release:        0.%{git}.1
License: 	BSD
Group: 	        Graphical desktop/Enlightenment
URL: 	        http://www.enlightenment.org/
Source:         https://download.enlightenment.org/rel/apps/enventor/%{name}-%{version}.tar.xz

# Git taken from https://git.enlightenment.org/tools/enventor.git/

BuildRequires:	pkgconfig(efl)
Requires:       efl
Requires:       efl-devel

%description
EDC script Editor for enlightenment.

%prep
%autosetup -p1

%build
sed -i s,release_info=\"-release\ \$release\",release_info=\"\",g configure.ac
./autogen.sh
%configure --with-eolian-gen=/usr/bin/eolian_gen

%make_build

%install
%make_install
###make install DESTDIR=%%{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/*
%{_includedir}/enventor-1/*
%{_libdir}/*
%{_libdir}/pkgconfig/*
