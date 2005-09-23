Summary:	Xinerama protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Xinerama i pomocnicze
Name:		xorg-proto-xineramaproto
Version:	1.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/xineramaproto-%{version}.tar.bz2
# Source0-md5:	91d70352ee2c7c8c3f848981719b90f3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xineramaproto.pc