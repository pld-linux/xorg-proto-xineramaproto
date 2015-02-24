Summary:	Xinerama extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xinerama
Name:		xorg-proto-xineramaproto
Version:	1.2.1
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{version}.tar.bz2
# Source0-md5:	9959fe0bfb22a0e7260433b8d199590a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
Obsoletes:	xorg-proto-panoramixproto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xinerama is an X extension that allows multiple physical screens
controlled by a single X server to appear as a single screen.

%description -l pl.UTF-8
Xinerama to rozszerzenie X pozwalające na sterowanie wieloma
fizycznymi ekranami przez pojedynczy serwer X tak, że stają się
jednym ekranem.

%package devel
Summary:	Xinerama extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xinerama
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	panoramixext
Obsoletes:	xorg-proto-panoramixproto-devel

%description devel
Xinerama is an X extension that allows multiple physical screens
controlled by a single X server to appear as a single screen.

%description devel -l pl.UTF-8
Xinerama to rozszerzenie X pozwalające na sterowanie wieloma
fizycznymi ekranami przez pojedynczy serwer X tak, że stają się
jednym ekranem.

%prep
%setup -q -n xineramaproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/panoramiXproto.h
%{_pkgconfigdir}/xineramaproto.pc
