%define		_realname	gwireless_applet
Summary:	GNOME-based panel applet and management tool to manage wireless network cards 
Name:		gnome-applet-wireless
Version:	0.8
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/gwifiapplet/%{_realname}-%{version}.tar.gz
# Source0-md5:	c1e51e9cd1877e4df05c019eed761b6c
URL:		http://gwifiapplet.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel >= 2.4.0
BuildRequires:	gtkxmhtml-devel
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	intltool >= 0.21
BuildRequires:	gnome-libs-devel >= 1.4.2
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libgtop-devel >= 2.10.0
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to create a GNOME-based panel applet and management
tool to manage wireless network cards that support Linux wireless
extensions.

%prep
%setup -q -n %{_realname}-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	localedir=%{_datadir}/locale

%find_lang wireless-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f netspeed-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/%{_realname}2
%{_libdir}/bonobo/servers/*.server
%{_omf_dest_dir}/%{_realname}
%{_pixmapsdir}/%{_realname}
%{_pixmapsdir}/*.png
