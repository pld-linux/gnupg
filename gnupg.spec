Summary:	gpg - GNU Privacy Guard
Name:		gnupg
Version:	0.9.6
Release:	1
Copyright:	GPL
Group:		Utilities/File
Group(pl):	Narz璠zia/Pliki
Source:		ftp://ftp.guug.de/pub/gcrypt/%{name}-%{version}.tar.gz
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

%build
autoconf
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr \
	--disable-m-debug \
	--disable-m-guard
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/gpgm.1
echo ".so gpg.1" >$RPM_BUILD_ROOT%{_mandir}/man1/gpgm.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	{AUTHORS,ChangeLog,NEWS,README,THANKS,TODO,doc/{DETAILS,FAQ,OpenPGP}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS,TODO,doc/{DETAILS,FAQ,OpenPGP}}.gz
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*
%attr(755,root,root) %{_libdir}/gnupg
%{_datadir}/gnupg

%lang(de)    %{_datadir}/locale/de/LC_MESSAGES/gnupg.mo
%lang(es_ES) %{_datadir}/locale/es_ES/LC_MESSAGES/gnupg.mo
%lang(fr)    %{_datadir}/locale/fr/LC_MESSAGES/gnupg.mo
%lang(it)    %{_datadir}/locale/it/LC_MESSAGES/gnupg.mo
%lang(pl)    %{_datadir}/locale/pl/LC_MESSAGES/gnupg.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/gnupg.mo
%lang(ru)    %{_datadir}/locale/ru/LC_MESSAGES/gnupg.mo

%changelog
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
