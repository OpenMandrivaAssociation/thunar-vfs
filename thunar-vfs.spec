%define url_ver %(echo %{version} | cut -c 1-3)

%define major 2
%define apiversion 1
%define libname %mklibname %{name} %{apiversion} %{major}
%define develname %mklibname %{name} -d

Summary:	Virtual file system for Thunar
Name:		thunar-vfs
Version:	1.2.0
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	dbus-glib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libGConf2-devel
BuildRequires:	gamin-devel
%if %mdkver >= 201200
Buildconflicts:	hal-devel
%else
BuildRequires:	hal-devel
%endif
BuildRequires:	libxfce4util-devel >= 4.9.0
BuildRequires:	startup-notification-devel
BuildRequires:	intltool

%description
This package contains the virtual filesystem shipped with Thunar 1.0
and earlier releases.
It provides compatibility for applications that still use thunar-vfs.

%package -n %{libname}
Summary:	Libraries for the %{name}
Group:		Graphical desktop/Xfce
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname thunar 1 2} <= 1.0.2

%description -n %{libname}
Libraries for the %{name}.

%package -n %{develname}
Summary:	Development files for the thunar filemanager
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Development files for the %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-dbus \
	--enable-startup-notification \
	--enable-gnome-thumbnailers \
	--disable-gtk-doc

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README NEWS
%dir %{_libdir}/%{name}-%{apiversion}
%dir %{_datadir}/thumbnailers
%{_libdir}/%{name}-%{apiversion}/*
%{_datadir}/thumbnailers/*.desktop
%{_datadir}/gtk-doc/html/thunar-vfs

%files -n %{libname}
%{_libdir}/*%{apiversion}.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}-%{apiversion}
%{_includedir}/%{name}-%{apiversion}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
