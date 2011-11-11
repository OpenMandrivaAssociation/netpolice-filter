Name:	 	netpolice-filter
Version:	2.0
Release:	2

Summary:	url filter for c-icap server
License:	BSD
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://www.netpolice.ru/

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	c-icap-devel
BuildRequires:	libmemcache-devel
BuildRequires:	opendbx-devel
BuildRequires: 	zlib-devel

Requires(pre):	shadow-utils

Requires:	%{name} = %{version}-%{release}
Requires:	opendbx
Requires:	opendbx-sqlite3

Provides:	c-icap-url-filter

%description
ICAP module for checking URL against blacklist.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
autoconf
autoheader
automake --foreign --add-missing --copy
cp INSTALL INSTALL.txt

%configure cicapincdir=/usr/include/c_icap 
make

%install

mkdir -p  %{buildroot}/etc
%makeinstall_std CONFIGDIR=/etc

%files
%defattr(-,root,root)
%doc AUTHORS README INSTALL.txt TODO
%{_libdir}/c_icap/*.so
%{_libdir}/c_icap/*.la
%config(noreplace) %{_sysconfdir}/*.conf*

%clean
make clean
rm -rf %{buildroot}

%changelog
* Fri Aug 26 2011 L.Butorina <l.butorina@cair.ru> 2
- New test version netpolice 2.0 for Mandriva.

* Fri Jul 29 2011 L.Butorina <l.butorina@cair.ru> 1
- New test version netpolice 1.1 for Mandriva.
