Summary:	GNOME panel object for posting blog entries
Summary(pl.UTF-8):	Obiekt panelu GNOME do wysyłania wpisów bloga
Name:		gnome-blog
Version:	0.8
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0a953c1dfade735285e768e785423222
Patch0:		%{name}-firstrun.patch
Patch1:		%{name}-applet-location.patch
Patch2:		%{name}-pygtk.patch
URL:		http://www.gnome.org/~seth/gnome-blog/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-desktop-devel
BuildRequires:	python-gnome-devel
BuildRequires:	python-pygtk-devel >= 1.99
BuildRequires:	rpm-pythonprov
Requires(post):	GConf2
%pyrequires_eq	python
Requires:	python-gnome-desktop-applet
Requires:	python-gnome-gconf
Requires:	python-gnome-ui
Requires:	python-pygtk-gtk >= 1.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.

%description -l pl.UTF-8
Obiekt panelu GNOME pozwalający na wygodne wysyłanie wpisów bloga do
dowolnego bloga obsługującego bloggerAPI.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/gnomeblog.schemas
%{py_sitescriptdir}/gnomeblog
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_libdir}/bonobo/servers/*.server
%attr(755,root,root) %{_libdir}/blog_applet.py
%{_datadir}/gnome-2.0/ui/*.xml
