%define	major 0
%define libname	%mklibname setproctitle %{major}
%define	devname	%mklibname setproctitle -d

Summary:	A setproctitle implementation
Name:		setproctitle
Version:	0.3.2
Release:	%mkrel 2
Group:		System/Libraries
License:	LGPL/BSD-style
URL:		http://www.altlinux.ru/
# http://sisyphus.ru/cgi-bin/srpm.pl/Sisyphus/setproctitle/getsource/0
Source0:	%{name}-%{version}.tar.xz
Patch0:		setproctitle-0.3.2-extra-ld-flags.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This library provides setproctitle function for setting the
invoking process's title.

%package -n	%{libname}
Summary:	A setproctitle implementation
Group:          System/Libraries

%description -n	%{libname}
This library provides setproctitle function for setting the
invoking process's title.

%package -n	%{devname}
Summary:	Development environment for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname setproctitle -d 0}

%description -n	%{devname}
This package contains development files required to build
setproctitle-based software.

%prep
%setup -q
%patch0 -p1 -b .ldflags~

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/*.so.*

%files -n %{devname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*
