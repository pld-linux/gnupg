#
# Conditional builds:
%bcond_without	ldap	# without LDAP plugin
#
Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(cs):	GNU nástroj pro ¹ifrovanou komunikaci a bezpeèné ukládání dat
Summary(es):	Criptografía con llaves públicas (asimétricas). GPL
Summary(ja):	¥»¥­¥å¥¢¤Ê¥³¥ß¥å¥Ë¥±¡¼¥·¥ç¥ó¤È¥Ç¡¼¥¿ÊÝÂ¸¤Î¤¿¤á¤Î GNU ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡£
Summary(pl):	GnuPG - narzêdzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(pt_BR):	Criptografia com chaves públicas (assimétricas). GPL
Summary(ru):	GNU Privacy Guard - Ó×ÏÂÏÄÎÁÑ ÚÁÍÅÎÁ PGP
Summary(uk):	GNU Privacy Guard - ×¦ÌØÎÁ ÚÁÍ¦ÎÁ PGP
Summary(zh_CN):	GPLµÄPGP¼ÓÃÜ³ÌÐò
Name:		gnupg
Version:	1.2.4
Release:	4
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/GnuPG/gnupg/%{name}-%{version}.tar.bz2
# Source0-md5:	16d0b575812060328f8e677b7f0047cc
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-missing-nls.patch
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%description -l cs
GnuPG je GNU nástroj pro bezpeènou komunikaci a ukládání dat. Mù¾e být
pou¾it na ¹ifrování dat a vytváøení digitálních podpisù. Obsahuje
funkce pro pokroèilou správu klíèù a vyhovuje navrhovanému OpenPGP
Internet standardu podle RFC2440. Byl vytvoøen jako kompletní náhrada
za PGP. Proto¾e neobsahuje ¹ifrovací algoritmy IDEA nebo RSA, mù¾e být
pou¾íván bez omezení. Proto¾e GnuPG nepou¾ívá ¾ádný patentovaný
algoritmus, nemù¾e být úplnì kompatibilní s PGP verze 2. PGP 2.x
pou¾ívá algoritmy IDEA (patentováno celosvìtovì) a RSA (patentováno ve
Spojených státech do 20. záøí 2000). Tyto algoritmy lze zavést do
GnuPG pomocí externích modulù.

%description -l es
GnuPG es un sustituto completo y de libre distribución para PGP. Como
no utiliza IDEA y RSA, su uso no está restringido. Está casi
completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l fr
GnuPG est un utilitaire GNU destiné à chiffrer des données et à créer
des signatures électroniques. Il a des capacités avancées de gestion
de clés et il est conforme à la norme proposée OpenPGP décrite dans la
RFC2440. Comme GnuPG n'utilise pas d'algorithme breveté, il n'est
compatible avec aucune version de PGP2 (PGP2.x ne sait utiliser que
l'IDEA breveté dans le monde entier et RSA, breveté aux États-Unis
jusqu'au 20 septembre 2000).

%description -l it
GnuPG (GNU Privacy Guard) è una utility GNU per la cifratura di dati e
la creazione di firme digitali. Possiede una gestione avanzata delle
chiavi ed è conforme allo standard Internet OpenPGP, descritto nella
RFC 2440. Non utilizzando algoritmi brevettati, non è compatibile con
PGP2 (PGP2.x usa solo IDEA, coperto da brevetto mondiale, ed RSA,
brevettato negli USA con scadenza 20/09/2000). Questi algoritmi sono
utilizzabili da GnuPG tramite moduli esterni.

%description -l ja
GnuPG (GNU Privacy Guard)
¤Ï¥Ç¡¼¥¿¤Î°Å¹æ²½¤È¥Ç¥£¥¸¥¿¥ë½ðÌ¾¤ÎºîÀ®¤Î¤¿¤á¤Î GNU
¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ç¤¹¡£GnuPG ¤Ï¹âÅÙ¤Ê¸°´ÉÍýÇ½ÎÏ¤ò»ý¤Á¡¢ RFC2440
¤Çµ­½Ò¤µ¤ì¤Æ¤¤¤ë OpenPGP ¥¤¥ó¥¿¡¼¥Í¥Ã¥ÈÉ¸½à¤ÎÄó°Æ¤ËÅ¬¹ç¤·¤Æ¤¤¤Þ¤¹¡£
GnuPG ¤ÏÆÃµö¥¢¥ë¥´¥ê¥º¥à¤Ï»ÈÍÑ¤·¤Æ¤¤¤Ê¤¤¤Î¤Ç¡¢PGP2
¤Î¤¢¤é¤æ¤ë¥ô¥¡¡¼¥¸¥ç¥ó ¤È¸ß´¹À­¤¬¤¢¤ê¤Þ¤»¤ó¡£(PGP2.x ¤Ï
À¤³¦Åª¤ÊÆÃµö¤Ç¤¢¤ë IDEA ¤È¡¢ 2000Ç¯ 9·î20Æü¤Þ¤Ç USA ¤Ç¤ÎÆÃµö¤Ç¤¢¤ë RSA
¤Î¤ß¤òÍÑ¤¤¤Æ¤¤¤Þ¤¹)

%description -l pl
GnuPG (GNU Privacy Guard) jest narzêdziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Mo¿e byæ u¿ywany do szyfrowania
oraz podpisywania danych. Umo¿liwia zaawansowane zarz±dzanie kluczami
i spe³nia normy zdefiniowane w standardzie OpenPGP, który jest opisany
w RFC2440.

%description -l pt_BR
O GnuPG é um substituto completo e de livre distribuição para o PGP.
Como ele não usa IDEA e RSA seu uso é irrestrito. Está quase
completamente de acordo com o rascunho (draft) OpenPGP.

%description -l ru
GnuPG Ñ×ÌÑÅÔÓÑ ÐÏÌÎÏÊ É Ó×ÏÂÏÄÎÏÊ ÚÁÍÅÎÏÊ ÄÌÑ PGP. ôÁË ËÁË ÏÎ ÎÅ
ÉÓÐÏÌØÚÕÅÔ ÎÉ IDEA, ÎÉ RSA, ÔÏ ÎÁ ÅÇÏ ÉÓÐÏÌØÚÏ×ÁÎÉÅ ÎÅ ÎÁËÌÁÄÙ×ÁÅÔÓÑ
ÎÉËÁËÉÈ ÏÇÒÁÎÉÞÅÎÉÊ. GnuPG ÓÏÏÔ×ÅÔÓÔ×ÕÅÔ ÓÐÅÃÉÆÉËÁÃÉÉ OpenPGP
(RFC2440).

%description -l uk
GnuPG ¤ ÐÏ×ÎÏÀ ÔÁ ×¦ÌØÎÏÀ ÚÁÍ¦ÎÏÀ PGP. ÷¦Î ÎÅ ×ÉËÏÒÉÓÔÏ×Õ¤ Î¦ IDEA,
ÁÎ¦ RSA, ÔÁË ÝÏ ÎÁ ÊÏÇÏ ÚÁÓÔÏÓÕ×ÁÎÎÑ ÎÅ ÎÁËÌÁÄÁ¤ÔØÓÑ Î¦ÑËÉÈ ÏÂÍÅÖÅÎØ.
GnuPG ×¦ÄÐÏ×¦ÄÁ¤ ÓÐÅÃÉÆ¦ËÁÃ¦§ OpenPGP (RFC2440).

%package plugin-keys_ldap
Summary:	GnuPG plugin for allow talk to a LDAP keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj±ca komunikowaæ siê z serwerem kluczy LDAP
Group:		Applications/File
Requires:	%{name} = %{version}

%description plugin-keys_ldap
GnuPG plugin for allow talk to a LDAP keyserver.

%description plugin-keys_ldap -l pl
Wtyczka GnuPG pozwalaj±ca komunikowaæ siê z serwerem kluczy LDAP.

%package plugin-keys_mailto
Summary:	GnuPG plugin for allow talk to a email keyserver
Summary(pl):	Wtyczka GnuPG pozwalaj±ca komunikowaæ siê z e-mailowym serwerem kluczy
Group:		Applications/File
Requires:	%{name} = %{version}

%description plugin-keys_mailto
GnuPG plugin for allow talk to a email keyserver.

%description plugin-keys_mailto -l pl
Wtyczka GnuPG pozwalaj±ca komunikowaæ siê z e-mailowym serwerem
kluczy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp /usr/share/automake/config.sub scripts
%configure \
	--with-capabilities \
	%{?with_ldap:--enable-ldap} \
	%{!?with_ldap:--disable-ldap} \
%ifarch sparc sparc64
	--disable-m-guard \
%else
	--enable-m-guard \
%endif
	--without-included-gettext \
	--disable-m-debug \
	--with-mailprog=/usr/sbin/sendmail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/gnupg

%{_mandir}/man?/*
%{_infodir}/*info*
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel

%if %{with ldap}
%files plugin-keys_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnupg/gpgkeys_ldap
%endif

%files plugin-keys_mailto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnupg/gpgkeys_mailto
