#
# Conditional builds:
%bcond_without	ldap	# without LDAP plugin
#
Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(cs.UTF-8):   GNU nástroj pro šifrovanou komunikaci a bezpečné ukládání dat
Summary(es.UTF-8):   Criptografía con llaves públicas (asimétricas). GPL
Summary(ja.UTF-8):   セキュアなコミュニケーションとデータ保存のための GNU ユーティリティ。
Summary(pl.UTF-8):   GnuPG - narzędzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(pt_BR.UTF-8):   Criptografia com chaves públicas (assimétricas). GPL
Summary(ru.UTF-8):   GNU Privacy Guard - свободная замена PGP
Summary(uk.UTF-8):   GNU Privacy Guard - вільна заміна PGP
Summary(zh_CN.UTF-8):   GPL的PGP加密程序
Name:		gnupg
Version:	1.4.6
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/GnuPG/gnupg/%{name}-%{version}.tar.bz2
# Source0-md5:	ec8dc6df1bd83c1d7e1a1ea10653f9f4
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-fix.patch
URL:		http://www.gnupg.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
BuildRequires:	libusb-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%description -l cs.UTF-8
GnuPG je GNU nástroj pro bezpečnou komunikaci a ukládání dat. Může být
použit na šifrování dat a vytváření digitálních podpisů. Obsahuje
funkce pro pokročilou správu klíčů a vyhovuje navrhovanému OpenPGP
Internet standardu podle RFC2440. Byl vytvořen jako kompletní náhrada
za PGP. Protože neobsahuje šifrovací algoritmy IDEA nebo RSA, může být
používán bez omezení. Protože GnuPG nepoužívá žádný patentovaný
algoritmus, nemůže být úplně kompatibilní s PGP verze 2. PGP 2.x
používá algoritmy IDEA (patentováno celosvětově) a RSA (patentováno ve
Spojených státech do 20. září 2000). Tyto algoritmy lze zavést do
GnuPG pomocí externích modulů.

%description -l es.UTF-8
GnuPG es un sustituto completo y de libre distribución para PGP. Como
no utiliza IDEA y RSA, su uso no está restringido. Está casi
completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l fr.UTF-8
GnuPG est un utilitaire GNU destiné à chiffrer des données et à créer
des signatures électroniques. Il a des capacités avancées de gestion
de clés et il est conforme à la norme proposée OpenPGP décrite dans la
RFC2440. Comme GnuPG n'utilise pas d'algorithme breveté, il n'est
compatible avec aucune version de PGP2 (PGP2.x ne sait utiliser que
l'IDEA breveté dans le monde entier et RSA, breveté aux États-Unis
jusqu'au 20 septembre 2000).

%description -l it.UTF-8
GnuPG (GNU Privacy Guard) è una utility GNU per la cifratura di dati e
la creazione di firme digitali. Possiede una gestione avanzata delle
chiavi ed è conforme allo standard Internet OpenPGP, descritto nella
RFC 2440. Non utilizzando algoritmi brevettati, non è compatibile con
PGP2 (PGP2.x usa solo IDEA, coperto da brevetto mondiale, ed RSA,
brevettato negli USA con scadenza 20/09/2000). Questi algoritmi sono
utilizzabili da GnuPG tramite moduli esterni.

%description -l ja.UTF-8
GnuPG (GNU Privacy Guard)
はデータの暗号化とディジタル署名の作成のための GNU
ユーティリティです。GnuPG は高度な鍵管理能力を持ち、 RFC2440
で記述されている OpenPGP インターネット標準の提案に適合しています。
GnuPG は特許アルゴリズムは使用していないので、PGP2
のあらゆるヴァージョン と互換性がありません。(PGP2.x は
世界的な特許である IDEA と、 2000年 9月20日まで USA での特許である RSA
のみを用いています)

%description -l pl.UTF-8
GnuPG (GNU Privacy Guard) jest narzędziem do bezpiecznej komunikacji i
bezpiecznego przechowywania danych. Może być używany do szyfrowania
oraz podpisywania danych. Umożliwia zaawansowane zarządzanie kluczami
i spełnia normy zdefiniowane w standardzie OpenPGP, który jest opisany
w RFC2440.

%description -l pt_BR.UTF-8
O GnuPG é um substituto completo e de livre distribuição para o PGP.
Como ele não usa IDEA e RSA seu uso é irrestrito. Está quase
completamente de acordo com o rascunho (draft) OpenPGP.

%description -l ru.UTF-8
GnuPG является полной и свободной заменой для PGP. Так как он не
использует ни IDEA, ни RSA, то на его использование не накладывается
никаких ограничений. GnuPG соответствует спецификации OpenPGP
(RFC2440).

%description -l uk.UTF-8
GnuPG є повною та вільною заміною PGP. Він не використовує ні IDEA,
ані RSA, так що на його застосування не накладається ніяких обмежень.
GnuPG відповідає специфікації OpenPGP (RFC2440).

%package plugin-keys_curl
Summary:	GnuPG plugin for allow talk to a HTTP/FTP keyserver
Summary(pl.UTF-8):   Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy HTTP/FTP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gnupg-plugin-keys_http

%description plugin-keys_curl
GnuPG plugin for allow talk to a HTTP(S)/FTP(S) keyserver.

%description plugin-keys_curl -l pl.UTF-8
Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy
HTTP(S)/FTP(S).

%package plugin-keys_finger
Summary:	GnuPG plugin for allow talk to a FINGER keyserver
Summary(pl.UTF-8):   Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy FINGER
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_finger
GnuPG plugin for allow talk to a FINGER keyserver.

%description plugin-keys_finger -l pl.UTF-8
Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy FINGER.

%package plugin-keys_hkp
Summary:	GnuPG plugin for allow talk to a HKP keyserver
Summary(pl.UTF-8):   Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy HKP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_hkp
GnuPG plugin for allow talk to a HKP keyserver.

%description plugin-keys_hkp -l pl.UTF-8
Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy HKP.

%package plugin-keys_ldap
Summary:	GnuPG plugin for allow talk to a LDAP keyserver
Summary(pl.UTF-8):   Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy LDAP
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_ldap
GnuPG plugin for allow talk to a LDAP keyserver.

%description plugin-keys_ldap -l pl.UTF-8
Wtyczka GnuPG pozwalająca komunikować się z serwerem kluczy LDAP.

%package plugin-keys_mailto
Summary:	GnuPG plugin for allow talk to a email keyserver
Summary(pl.UTF-8):   Wtyczka GnuPG pozwalająca komunikować się z e-mailowym serwerem kluczy
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description plugin-keys_mailto
GnuPG plugin for allow talk to a email keyserver.

%description plugin-keys_mailto -l pl.UTF-8
Wtyczka GnuPG pozwalająca komunikować się z e-mailowym serwerem
kluczy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.sub scripts
%configure \
	--with-capabilities \
	%{?with_ldap:--enable-ldap} \
	%{!?with_ldap:--disable-ldap} \
	--disable-m-debug \
	--disable-m-guard \
	--enable-mailto \
	--without-included-gettext \
	--with-mailprog=/usr/sbin/sendmail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT{%{_datadir}/gnupg/{FAQ,faq.html},%{_infodir}/dir}

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
%dir %{_libexecdir}/gnupg
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel
%{_mandir}/man?/*
%{_infodir}/*.info*

%files plugin-keys_finger
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_finger

%files plugin-keys_hkp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_hkp

%files plugin-keys_curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_curl

%if %{with ldap}
%files plugin-keys_ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_ldap
%endif

%files plugin-keys_mailto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnupg/gpgkeys_mailto
