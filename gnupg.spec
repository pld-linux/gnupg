Summary:	gpg - GNU Privacy Guard
Name:		gnupg
Version:	0.9.9
Release:	1
Copyright:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source:		ftp://ftp.guug.de/pub/gcrypt/%{name}-%{version}.tar.gz
Icon:		gnupg.gif
URL:		http://www.d.shuttle.de/isil/gnupg/
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GPG is the main program for the GNUPG system. gpgm is a maintenance tool
which has some commands gpgm does not have; it is there because it does not
handle sensitive data ans therefore has no need to allocate secure memory.

%prep
%setup -q

%build
gettextize --force --copy
%configure \
	--without-included-gettext \
	--disable-m-debug \
	--disable-m-guard
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{_libdir}/gnupg/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	{AUTHORS,ChangeLog,NEWS,README,THANKS,TODO,doc/{DETAILS,FAQ,OpenPGP}}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS,TODO,doc/{DETAILS,FAQ,OpenPGP}}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*
%{_datadir}/gnupg
