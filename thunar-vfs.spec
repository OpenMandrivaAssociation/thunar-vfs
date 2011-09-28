%define url_ver %(echo %{version} | cut -c 1-3)

%define major 2
%define apiversion 1
%define libname %mklibname %{name} %{apiversion} %{major}
%define develname %mklibname %{name} -d

Summary:	Virtual file system for Thunar
Name:		thunar-vfs
Version:	1.2.0
Release:	%mkrel 4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	dbus-glib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libGConf2-devel
BuildRequires:	gamin-devel
BuildRequires:	hal-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	startup-notification-devel
BuildRequires:	intltool
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains the virtual filesystem shipped with Thunar 1.0 and earlier
releases. It provides compatibility for applications that still use thunar-vfs.

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
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS
%dir %{_libdir}/%{name}-%{apiversion}
%dir %{_datadir}/thumbnailers
%{_libdir}/%{name}-%{apiversion}/*
%{_datadir}/thumbnailers/*.desktop
%{_datadir}/gtk-doc/html/thunar-vfs

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{apiversion}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}-%{apiversion}
%{_includedir}/%{name}-%{apiversion}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_libdir}/pkgconfig/*.pc
