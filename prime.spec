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
