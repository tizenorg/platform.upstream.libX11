Name:           libX11
Version:        1.5.0
Release:        0
License:        MIT
Summary:        Core X11 protocol client library
Url:            http://xorg.freedesktop.org/
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(xcb) >= 1.1.92
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86bigfontproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.11
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xproto) >= 7.0.13
BuildRequires:  pkgconfig(xtrans)
Requires:       %{name}-data >= %{version}

%description
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package xcb
Summary:        XCB X11 protocol client library
Group:          Graphics/X Window System
Requires:       %{name}-data >= %{version}

%description xcb
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package data
Summary:        Shared data for the Core X11 protocol library
Group:          Graphics/X Window System
BuildArch:      noarch

%description data
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

%package devel
Summary:        Development files for the Core X11 protocol library
Group:          Development/Libraries
Requires:       libX11 = %{version}
Requires:       libX11-xcb = %{version}

%description devel
The X Window System is a network-transparent window system that was
designed at MIT. X display servers run on computers with either
monochrome or color bitmap display hardware. The server distributes
user input to and accepts output requests from various client
programs located either on the same machine or elsewhere in the
network. Xlib is a C subroutine library that application programs
(clients) use to interface with the window system by means of a
stream connection.

This package contains the development headers for the library found
in libX11 and libX11-xcb.

%prep
%setup -q

%build
%reconfigure --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install


rm -rf %{buildroot}%{_libdir}/X11/Xcms.txt

%post   -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%post   xcb -p /sbin/ldconfig

%postun xcb -p /sbin/ldconfig

%docs_package

%files
%defattr(-,root,root)
%{_libdir}/libX11.so.6*

%files xcb
%defattr(-,root,root)
%{_libdir}/libX11-xcb.so.1*

%files data
%defattr(-,root,root)
%{_datadir}/X11

%files devel
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%_docdir/%{name}

%changelog
