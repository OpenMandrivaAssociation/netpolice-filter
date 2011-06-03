Name: netpolice-filter
Version: 1.01
Release: 1%{?dist}
Packager: CAIR <support@cair.ru>

Summary: url filter for c-icap server
License: BSD
Group: System/Servers
Url: http://www.netpolice.ru/

Source0: %name-%version.tar.gz
Patch: %name-%version-strlcpy.patch
Patch1: %name-%version-eng-fix.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-{release}-buildroot

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: gcc-c++ >= 4.4 libc-icap-netpolice-devel libmemcache-devel opendbx-devel zlib-devel

Requires(pre): shadow-utils

Requires: %name = %version-%release
Requires: opendbx
Requires: opendbx-sqlite3

%description
ICAP module for checking URL against blacklist

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
aclocal
autoconf  
autoheader
cp /usr/share/libtool/config/ltmain.sh ltmain.sh
automake --add-missing --copy  
cp INSTALL INSTALL.txt

%configure cicapincdir=%_includedir/c_icap
make

%install
##make ROOT="$RPM_BUILD_ROOT" install
%{__make} DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/c_icap
mv %{buildroot}%{_libdir}/%name/srv_url_filter.so %{buildroot}%{_libdir}/c_icap
rm -rf %{buildroot}%{_libdir}/%name

%files
%doc AUTHORS README INSTALL.txt TODO
%_libdir/c_icap/srv_url_filter.so

%clean
make clean
rm -rf %{buildroot}

