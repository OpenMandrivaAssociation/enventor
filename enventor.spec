%define	name enventor
%define	git_version 20190227
#%%define use_ccache 1

Summary:        Enlightenment edc editor
Name: 	        %{name}
Version:        %{git_version}
Release:        1
License: 	BSD
Group: 	        Graphical desktop/Enlightenment
URL: 	        http://www.enlightenment.org/
Source:         %{name}-%{git_version}.tar.xz

#BuildRequires:	elementary-devel
BuildRequires:	efl-devel
BuildRequires:	elementary
BuildRequires:  efl
Requires:       efl
Requires:       efl-devel
Requires:       elementary
Requires:       elementary-devel
Requires:       evas-generic-loaders

%description
EDC script Editor for enlightenment.

%prep
%setup -qn %{name}-%{version}

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