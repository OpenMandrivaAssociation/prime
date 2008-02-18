%define version	        1.0.0.1
%define release         %mkrel 5

%define dict_version    1.0.0
%define suikyo_version  2.1.0-2

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:         prime
Summary:      PRIME is Japanese PRedictive Input Method Editor
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
Requires:        %{libname} = %{version}
BuildRequires:   ruby

%description
PRIME is Japanese PRedictive Input Method Editor.


%package -n %{libname}
Summary:    Prime library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
Prime library.


%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh

%configure2_5x
# parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/prime
cp -f etc/Custom_prime.rb $RPM_BUILD_ROOT/%{_sysconfdir}/prime/

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc ChangeLog COPYING README TODO
%{_sysconfdir}/*
%{_datadir}/%name
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*


