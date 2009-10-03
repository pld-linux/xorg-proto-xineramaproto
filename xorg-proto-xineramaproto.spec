Summary:	Xinerama extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Xinerama
Name:		xorg-proto-xineramaproto
Version:	1.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-%{version}.tar.bz2
# Source0-md5:	a8aadcb281b9c11a91303e24cdea45f5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
Obsoletes:	xorg-proto-panoramixproto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xinerama extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Xinerama.

%package devel
Summary:	Xinerama extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Xinerama
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	panoramixext
Obsoletes:	xorg-proto-panoramixproto-devel

%description devel
Xinerama extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Xinerama.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/panoramiXproto.h
%{_pkgconfigdir}/xineramaproto.pc
