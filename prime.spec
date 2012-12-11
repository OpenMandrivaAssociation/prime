%define version	        1.0.0.1
%define release         %mkrel 8

%define dict_version    1.0.0
%define suikyo_version  2.1.0-2

Name:         prime
Summary:      Japanese PRedictive Input Method Editor
Version:      %{version}
Release:      %{release}
URL:          http://sourceforge.jp/projects/prime/
Source0:      %{name}-%{version}.tar.bz2
Group:        System/Internationalization
BuildRoot:    %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:      GPL
Obsoletes:       uim-prime <= 0.4.6-1.beta2.3mdk
Requires:        prime-dict >= %{dict_version}
Requires:        suikyo >= %{suikyo_version}
Requires:        ruby-progressbar
Requires:        ruby-sary >= 1.2.0
BuildRequires:   ruby
Obsoletes:	%{mklibname prime 0} < %version-%release

%description
PRIME is Japanese PRedictive Input Method Editor.

%package devel
Summary: Development files for prime
Group: Development/Other
Requires: %name = %version
Conflicts: lib64prime0 < %version-%release
Conflicts: libprime0 < %version-%release

%description devel
This package contains development files for prime.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x --with-rubydir=%{ruby_sitelibdir}
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/prime
cp -f etc/Custom_prime.rb $RPM_BUILD_ROOT/%{_sysconfdir}/prime/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README TODO
%{_sysconfdir}/*
%{_datadir}/%name
%{_bindir}/*
%{ruby_sitelibdir}/*

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Jul 21 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0.1-8mdv2009.0
+ Revision: 239270
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sun Jul 06 2008 Funda Wang <fundawang@mandriva.org> 1.0.0.1-7mdv2009.0
+ Revision: 232039
- revert to arch-dependent packages

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 1.0.0.1-6mdv2009.0
+ Revision: 227795
- it should be noarch pacakge, it only contains data files and ruby script source
- split pkgconfig file into devel package

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 19 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0.1-5mdv2008.1
+ Revision: 172384
- do not list twice %%_docdir
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Apr 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.0.1-4mdk
- rebuild against suikyo-2.1.0-2

* Fri May 27 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.0.1-3mdk
- fix requires

* Sat Apr 16 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.0.1-2mdk
- Fixed prime-dict version Requires for X86-64.

* Wed Mar 30 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.0.1-1mdk
- new release

* Wed Mar 02 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.9.4-0.rc1.1mdk
- new release
- add obsoletes uim-prime <= 0.4.6-1.beta2.3mdk
- fix requires

* Thu Feb 24 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.9.4-0.beta2.1mdk
- new release
- define prime-dict_version and suikyo_version
- spec cleanup

* Thu Feb 17 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.9.4-0.alpha3.1mdk
- cleanups
- fix build
- first spec for mdk (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

