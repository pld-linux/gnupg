Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(pl):	GnuPG - GNU Privacy Guard - narzêdzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(ja):	¥»¥­¥å¥¢¤Ê¥³¥ß¥å¥Ë¥±¡¼¥·¥ç¥ó¤È¥Ç¡¼¥¿ÊÝÂ¸¤Î¤¿¤á¤Î GNU ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡£
Summary(pt_BR):	Criptografia com chaves públicas (assimétricas). GPL
Summary(es):	Criptografía con llaves públicas (asimétricas). GPL
Name:		gnupg
Version:	1.0.7
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	libcap-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage.
It can be used to encrypt data and to create digital signatures.
It includes an advanced key management facility and is compliant
with the proposed OpenPGP Internet standard as described in RFC2440.

%description -l pl
GnuPG jest narzêdziem do bezpiecznej komunikacji i bezpiecznego
przechowywania danych. Mo¿e byæ u¿ywany do szyfrowania oraz podpisywania
danych. Umo¿liwia zaawansowane zarz±dzanie kluczami i spe³nia normy
zdefiniowane w standardzie OpenPGP, który jest opisany w RFC2440.

%description -l ja
GnuPG (GNU Privacy Guard) ¤Ï¥Ç¡¼¥¿¤Î°Å¹æ²½¤È¥Ç¥£¥¸¥¿¥ë½ðÌ¾¤ÎºîÀ®¤Î¤¿¤á¤Î
GNU ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ç¤¹¡£GnuPG ¤Ï¹âÅÙ¤Ê¸°´ÉÍýÇ½ÎÏ¤ò»ý¤Á¡¢
RFC2440 ¤Çµ­½Ò¤µ¤ì¤Æ¤¤¤ë OpenPGP ¥¤¥ó¥¿¡¼¥Í¥Ã¥ÈÉ¸½à¤ÎÄó°Æ¤ËÅ¬¹ç¤·¤Æ¤¤¤Þ¤¹¡£
GnuPG ¤ÏÆÃµö¥¢¥ë¥´¥ê¥º¥à¤Ï»ÈÍÑ¤·¤Æ¤¤¤Ê¤¤¤Î¤Ç¡¢PGP2 ¤Î¤¢¤é¤æ¤ë¥ô¥¡¡¼¥¸¥ç¥ó
¤È¸ß´¹À­¤¬¤¢¤ê¤Þ¤»¤ó¡£(PGP2.x ¤Ï À¤³¦Åª¤ÊÆÃµö¤Ç¤¢¤ë IDEA ¤È¡¢
2000Ç¯ 9·î20Æü¤Þ¤Ç USA ¤Ç¤ÎÆÃµö¤Ç¤¢¤ë RSA ¤Î¤ß¤òÍÑ¤¤¤Æ¤¤¤Þ¤¹)

%description -l pt_BR
O GnuPG é um substituto completo e de livre distribuição para o PGP. Como ele
não usa IDEA e RSA seu uso é irrestrito. Está quase completamente de acordo com
o rascunho (draft) OpenPGP.

%description -l es
GnuPG es un sustituto completo y de libre distribución para PGP. Como no
utiliza IDEA y RSA, su uso no está restringido. Está casi completamente de
acuerdo con el borrador (draft) OpenPGP.

%prep
%setup -q

%build
%configure \
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*

%{_infodir}/*
%{_mandir}/man?/*
%{_datadir}/gnupg
