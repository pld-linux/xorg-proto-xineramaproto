Summary:	Xinerama protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Xinerama i pomocnicze
Name:		xorg-proto-xineramaproto
Version:	1.1.2
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/proto/xineramaproto-%{version}.tar.bz2
# Source0-md5:	aedc285fffda0dd9d3df98b42f3dfe2d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
Obsoletes:	xorg-proto-panoramixproto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xinerama protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u Xinerama i pomocnicze.

%package devel
Summary:	Xinerama protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Xinerama i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	panoramixext
Obsoletes:	xorg-proto-panoramixproto-devel

%description devel
Xinerama protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u Xinerama i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xineramaproto.pc
