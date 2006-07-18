Summary:	Open Fingerprint Architecture - identyfying a piece of music with just sound
Summary(pl):	Open Fingerprint Architecture - identyfikowanie muzyki po samym d¼wiêku
Name:		libofa
Version:	0.9.3
Release:	1
License:	GPL v2 or Adaptive Public License
Group:		Libraries
Source0:	http://www.musicdns.org/themes/musicdns_org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	51507d2c4b432bd2755f48d58471696e
Patch0:		%{name}-link.patch
Patch1:		%{name}-c++.patch
URL:		http://www.musicdns.org/
BuildRequires:	curl-devel
BuildRequires:	expat-devel >= 1.95
BuildRequires:	fftw3-devel >= 3.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MusicDNS and the Open Fingerprint Architecture provide a system for
identifying a piece of music with nothing more than the sound of the
piece itself.

%description -l pl
MusicDNS i Open Fingerprint Architecture dostarczaj± system do
identyfikowania utworów muzycznych bez dodatkowych informacji, na
podstawie samego d¼wiêku.

%package devel
Summary:	Header files for libofa library
Summary(pl):	Pliki nag³ówkowe biblioteki libofa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-devel >= 3.0
Requires:	libstdc++-devel

%description devel
Header files for libofa library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libofa.

%package static
Summary:	Static libofa library
Summary(pl):	Statyczna biblioteka libofa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libofa library.

%description static -l pl
Statyczna biblioteka libofa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libofa.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libofa.so
%{_libdir}/libofa.la
%{_includedir}/ofa1
%{_pkgconfigdir}/libofa.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libofa.a
