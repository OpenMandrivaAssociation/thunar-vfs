%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define api	1
%define major	2
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Name:           thunar-vfs
Version:        1.2.0
Release:		6
Summary:        Virtual filesystem shipped with Thunar 1.0 and earlier releases
Group:          Graphical desktop/Xfce
License:        LGPLv2+
URL:            http://thunar.xfce.org
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.34
BuildRequires:	pkgconfig(exo-1) >= 0.6.0
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(gconf-2.0) >= 2.4.0
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) >= 2.10.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gthread-2.0) >= 2.12.0
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.10.0
BuildRequires:	pkgconfig(libpng) >= 1.2.0
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.4
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.8.0
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	intltool

%description
Thunar-vfs contains the virtual filesystem shipped with Thunar 1.0 and
earlier releases. It provides compatibility for applications that still
use thunar-vfs while Thunar was ported to GVFS.

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Conflicts:	%{name} < 1.2.0-2

%description -n %{libname}
Thunar-vfs contains the virtual filesystem shipped with Thunar 1.0 and
earlier releases. It provides compatibility for applications that still
use thunar-vfs while Thunar was ported to GVFS.

This package contains the shared libraries for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 1.2.0-2

%description -n %{devname}
Thunar-vfs contains the virtual filesystem shipped with Thunar 1.0 and
earlier releases. It provides compatibility for applications that still
use thunar-vfs while Thunar was ported to GVFS.

This package contains the libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/doc

%check
make tests

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README 
%doc docs/ThumbnailersCacheFormat.txt docs/README.volumes
%{_datadir}/thumbnailers/thunar-vfs-font-thumbnailer-1.desktop

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/thunar-vfs-*

%files -n %{devname}
%doc HACKING TODO
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/%{name}-%{api}/
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/thunar-vfs-%{api}.pc
