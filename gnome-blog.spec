Summary:	GNOME panel object for posting blog entries
Summary(pl):	Obiekt panelu GNOME do wysy³ania wpisów bloga
Name:		gnome-blog
Version:	0.7
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	20c5666668c27d0b31e2bc5249b9e707
URL:		http://www.gnome.org/~seth/gnome-blog/
BuildRequires:	python-pygtk-devel >= 1.99
BuildRequires:	rpm-pythonprov
Requires(post):	GConf2
%pyrequires_eq	python
Requires:	python-gnome-gconf
Requires:	python-pygtk-gtk >= 1.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.

%description -l pl
Obiekt panelu GNOME pozwalaj±cy na wygodne wysy³anie wpisów bloga do
dowolnego bloga obs³uguj±cego bloggerAPI.

%prep
%setup -q

%build
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{py_sitedir}/gnomeblog
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
