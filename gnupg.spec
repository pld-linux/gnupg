Summary:	gpg - GNU Privacy Guard
Summary(pl):	gpg Stra¿nik Prywatno¶ci GNU
Summary(ja):	¥»¥­¥å¥¢¤Ê¥³¥ß¥å¥Ë¥±¡¼¥·¥ç¥ó¤È¥Ç¡¼¥¿ÊÝÂ¸¤Î¤¿¤á¤Î GNU ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡£
Summary(pt_BR):	Criptografia com chaves públicas (assimétricas). GPL
Summary(es):	Criptografía con llaves públicas (asimétricas). GPL
Name:		gnupg
Version:	1.0.6
Release:	3
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Patch0:		%{name}-locale.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-1.0.5-es_ES-fix.patch
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
#BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
#BuildRequires:	libtool
#BuildRequires:	automake
#BuildRequires:	autoconf
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPG is the main program for the GNUPG system. gpgm is a maintenance
tool which has some commands gpgm does not have; it is there because
it does not handle sensitive data and therefore has no need to
allocate secure memory.

%description -l pl
GPG jest g³ównym programem nale¿±cym do systemu GNUPG (GNU Privacy
Guard, odpowiednik programu Pretty Good Privacy na licencji GNU).

%description -l ja
GnuPG (GNU Privacy Guard) ¤Ï¥Ç¡¼¥¿¤Î°Å¹æ²½¤È¥Ç¥£¥¸¥¿¥ë½ðÌ¾¤ÎºîÀ®¤Î¤¿¤á¤Î
GNU ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ç¤¹¡£GnuPG ¤Ï¹âÅÙ¤Ê¸°´ÉÍýÇ½ÎÏ¤ò»ý¤Á¡¢
RFC2440 ¤Çµ­½Ò¤µ¤ì¤Æ¤¤¤ë OpenPGP ¥¤¥ó¥¿¡¼¥Í¥Ã¥ÈÉ¸½à¤ÎÄó°Æ¤ËÅ¬¹ç¤·¤Æ¤¤¤Þ¤¹¡£
GnuPG ¤ÏÆÃµö¥¢¥ë¥´¥ê¥º¥à¤Ï»ÈÍÑ¤·¤Æ¤¤¤Ê¤¤¤Î¤Ç¡¢PGP2 ¤Î¤¢¤é¤æ¤ë¥ô¥¡¡¼¥¸¥ç¥ó
¤È¸ß´¹À­¤¬¤¢¤ê¤Þ¤»¤ó¡£(PGP2.x ¤Ï À¤³¦Åª¤ÊÆÃµö¤Ç¤¢¤ë IDEA ¤È¡¢
2000Ç¯ 9·î20Æü¤Þ¤Ç USA ¤Ç¤ÎÆÃµö¤Ç¤¢¤ë RSA ¤Î¤ß¤òÍÑ¤¤¤Æ¤¤¤Þ¤¹)

%description -l pt_BR
O GNUPG é um substituto completo e de livre distribuição para o PGP. Como ele
não usa IDEA e RSA seu uso é irrestrito. Está quase completamente de acordo com
o rascunho (draft) OpenPGP.

%description -l es
GNUPG es un sustituto completo y de libre distribución para PGP. Como no
utiliza IDEA y RSA, su uso no está restringido. Está casi completamente de
acuerdo con el borrador (draft) OpenPGP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
#rm scripts/missing
#gettextize --force --copy
#aclocal 
#autoconf
#automake -a -c --no-force
%configure2_13 \
	--with-capabilities \
%ifarch sparc sparc64
	--disable-m-guard \
%else
	--enable-m-guard \
%endif
	--without-included-gettext \
	--disable-m-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO \
	  doc/{DETAILS,FAQ,OpenPGP}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*
%{_datadir}/gnupg
