Summary:	gpg - GNU Privacy Guard
Name:		gnupg
Version:	0.9.8
Release:	1
Copyright:	GPL
Group:		Utilities/File
Group(pl):	Narz璠zia/Pliki
Source:		ftp://ftp.guug.de/pub/gcrypt/%{name}-%{version}.tar.gz
Patch:		gnupg.patch
Icon:		gnupg.gif
URL:		http://www.d.shuttle.de/isil/gnupg/
BuildPrereq:	gdbm-devel
BuildPrereq:	zlib-devel
Provides:	pgp
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GPG is the main program for the GNUPG system. gpgm is a maintenance tool
which has some commands gpgm does not have; it is there because it does not
handle sensitive data ans therefore has no need to allocate secure memory.

%prep
%setup -q
%patch -p1

%build
gettextize --force --copy
autoconf
%configure \
	--prefix=%{_prefix} \
	--without-included-gettext \
	--disable-m-debug \
	--disable-m-guard
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/gnupg
%{_datadir}/gnupg

%changelog
* Tue May 25 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.7-1]
- added using more rpm macros,
- added --without-included-gettext to ./configure pararameters.

* Fri May  7 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.6-1]
- naw package is FHS 2.0 compliant.

* Fri Mar 19 1999 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.5-1]
- removed man group from man pages,
- added gzipping %doc,
- added pl locale.

* Mon Dec 21 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.0-1]
- added %{_datadir}/gnupg.

* Sat Dec 12 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.5-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- s/rfcs/OpenPGP/ in %doc,
- added pt* and ru .mo files.

* Mon Sep 21 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.0-1]
- first release in rpm package.
