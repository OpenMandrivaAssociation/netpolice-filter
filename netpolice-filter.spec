Name:	 	netpolice-filter
Version:	2.0
Release:	4

Summary:	url filter for c-icap server
License:	BSD
Group:		System/Servers
Url:		https://www.netpolice.ru/

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	c-icap-devel
BuildRequires:	libmemcache-devel
BuildRequires:	opendbx-devel
BuildRequires: 	zlib-devel

Requires(pre):	shadow-utils

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
%doc AUTHORS README INSTALL.txt TODO
%{_libdir}/c_icap/*.so
%config(noreplace) %{_sysconfdir}/*.conf*



%changelog
* Tue Dec 06 2011 Pischulin Anton <apischulin@mandriva.org> 2.0-2
+ Revision: 738268
- update to 2.0

  + Alex Burmashev <burmashev@mandriva.org>
    - import netpolice-filter

