Summary:	Platform-independent, multi-threading and synchronization library for C++
Summary(pl.UTF-8):	Wieloplatformowa biblioteka C++ do obsługi wątków i synchronizacji
Name:		ZThread
Version:	2.3.2
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/zthread/%{name}-%{version}.tar.gz
# Source0-md5:	f2782d19b8ed6f1ff2ab8824dd4ba48e
Patch0:		%{name}-c++.patch
Patch1:		%{name}-destdir.patch
Patch2:		%{name}-am.patch
URL:		http://zthread.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ZThread package is an advanced object-oriented, cross-platform,
C++ threading and synchronization library that has been designed and
implemented by the author and released under the MIT license. It
provides a high level abstraction of the native threading mechanisms
to offer a great deal of flexibility and control.

%description -l pl.UTF-8
ZThread to zaawansowana, zorientowana obiektowo, wieloplatformowa
biblioteka C++ do wątkow i synchronizacji zaprojektowana i
zaimplementowana, a następnie wydana przez autora na licencji MIT.
Udostępnia wysokopoziomową abstrakcję natywnych mechanizmów wątków,
oferując dużą elastyczność i kontrolę.

%package devel
Summary:	Header files for ZThread library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ZThread
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for ZThread library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ZThread.

%package static
Summary:	Static ZThread library
Summary(pl.UTF-8):	Statyczna biblioteka ZThread
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ZThread library.

%description static -l pl.UTF-8
Statyczna biblioteka ZThread.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I share
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libZThread-2.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libZThread-2.3.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/*.{html,js,css}
%attr(755,root,root) %{_bindir}/zthread-config
%attr(755,root,root) %{_libdir}/libZThread.so
%{_libdir}/libZThread.la
%{_includedir}/zthread
%{_aclocaldir}/pthread.m4
%{_aclocaldir}/zthread.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libZThread.a
