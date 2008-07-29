%define	major 0
%define libname	%mklibname setproctitle %{major}

Summary:	A setproctitle implementation
Name:		setproctitle
Version:	0.1
Release:	%mkrel 4
Group:		System/Libraries
License:	LGPL
URL:		http://www.altlinux.ru/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This library provides setproctitle function for setting the
invoking process's title.

%package -n	%{libname}
Summary:	A setproctitle implementation
Group:          System/Libraries

%description -n	%{libname}
This library provides setproctitle function for setting the
invoking process's title.

%package -n	%{libname}-devel
Summary:	Development environment for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
This library provides setproctitle function for setting the
invoking process's title.

This package contains development files required to build
%{name} based software.

%prep

%setup -q -n %{name}-%{version}

%build

make RPM_OPT_FLAGS="%{optflags} -fPIC -DPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_mandir}/man3

install -m0755 libsetproctitle.so.%{version} %{buildroot}%{_libdir}/
ln -snf libsetproctitle.so.%{version} %{buildroot}%{_libdir}/libsetproctitle.so.%{major}
ln -snf libsetproctitle.so.%{version} %{buildroot}%{_libdir}/libsetproctitle.so

install -m0644 setproctitle.h %{buildroot}%{_includedir}/
install -m0644 setproctitle.3 %{buildroot}%{_mandir}/man3/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*


