Summary:     gpg - GNU Privacy Guard
Name:        gnupg
Version:     0.4.3
Release:     1
Source:      ftp://ftp.guug.de/pub/gcrypt/%{name}-%{version}.tar.gz
URL:         http://www.d.shuttle.de/isil/crypt/gnupg.html
Icon:        keyhole.gif
Copyright:   GPL
Provides:    pgp
Group:       Utilities/File
BuildRoot:   /tmp/%{name}-%{version}-root

%description
gpg is the main program for the GNUPG system. gpgm is a maintenance tool
which has some commands gpgm does not have; it is there because it does not
handle sensitive data ans therefore has no need to allocate secure memory.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--disable-m-debug \
	--disable-m-guard
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,rfcs}
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
%attr(755, root, root) /usr/lib/gnupg
%lang(en) /usr/share/locale/en/LC_MESSAGES/gnupg.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/gnupg.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/gnupg.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/gnupg.mo

%changelog
* Mon Sep 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4.0-1]
- first release in rpm package.
