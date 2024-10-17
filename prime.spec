%define debug_package %{nil}

%define dict_version    1.0.0
%define suikyo_version  2.1.0-2

Name:         prime
Summary:      Japanese PRedictive Input Method Editor

Version:      1.0.0.1
Release:      13
URL:          https://sourceforge.jp/projects/prime/
Source0:      %{name}-%{version}.tar.bz2
Group:        System/Internationalization
License:      GPL
Obsoletes:       uim-prime <= 0.4.6-1.beta2.3mdk
Requires:        prime-dict >= %{dict_version}
Requires:        suikyo >= %{suikyo_version}
Requires:        ruby-progressbar
Requires:        ruby-sary >= 1.2.0
BuildRequires:   ruby
Obsoletes:	%{mklibname prime 0} < %{version}-%{release}

%description
PRIME is Japanese PRedictive Input Method Editor.

%package devel
Summary: Development files for prime

Group: Development/Other
Requires: %{name} = %{version}
Requires: suikyo-devel >= %{suikyo_version}
Conflicts: lib64prime0 < %{version}-%{release}
Conflicts: libprime0 < %{version}-%{release}

%description devel
This package contains development files for prime.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x --with-rubydir=%{ruby_sitelibdir}
make

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_sysconfdir}/prime
cp -f etc/Custom_prime.rb %{buildroot}/%{_sysconfdir}/prime/

%clean

%files
%doc ChangeLog COPYING README TODO
%{_sysconfdir}/*
%{_datadir}/%{name}
%{_bindir}/*
%{ruby_sitelibdir}/*

%files devel
%{_libdir}/pkgconfig/*.pc

