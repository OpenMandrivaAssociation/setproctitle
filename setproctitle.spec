%define	major 0
%define libname	%mklibname setproctitle %{major}
%define	devname	%mklibname setproctitle -d

Summary:	A setproctitle implementation
Name:		setproctitle
Version:	0.3.2
Release:	3
Group:		System/Libraries
License:	LGPL/BSD-style
URL:		https://www.altlinux.ru/
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


%changelog
* Thu Jul 15 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.2-2mdv2011.0
+ Revision: 553684
- fix compiler flags so that we can set them correctly (P0)

* Wed Jul 14 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 553357
- new release: 0.3.2
- cleanup heavily

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2010.0
+ Revision: 433730
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2009.0
+ Revision: 260628
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 252346
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2008.1
+ Revision: 140792
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdv2007.0
+ Revision: 115951
- Import setproctitle

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1-2mdk
- rebuild

* Sat Dec 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.1-1mdk
- initial mandrake package

