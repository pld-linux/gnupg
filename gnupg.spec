Summary:	GnuPG - GNU Privacy Guard - tool for secure communication and data storage
Summary(pl):	GnuPG - GNU Privacy Guard - narzЙdzie do bezpiecznej komunikacji i bezpiecznego przechowywania danych
Summary(es):	CriptografМa con llaves pЗblicas (asimИtricas). GPL
Summary(ja):	╔╩╔╜╔Е╔╒╓й╔Ё╔ъ╔Е╔к╔╠║╪╔╥╔Г╔С╓х╔г║╪╔©йщб╦╓н╓©╓А╓н GNU ╔Ф║╪╔ф╔ё╔Й╔ф╔ё║ё
Summary(pt_BR):	Criptografia com chaves pЗblicas (assimИtricas). GPL
Summary(ru):	GNU Privacy Guard - свободная замена PGP
Summary(uk):	GNU Privacy Guard - в╕льна зам╕на PGP
Name:		gnupg
Version:	1.0.7
Release:	2
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	libcap-devel
BuildRequires:	openldap-devel 
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG is GNU's tool for secure communication and data storage. It can
be used to encrypt data and to create digital signatures. It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440.

%description -l es
GnuPG es un sustituto completo y de libre distribuciСn para PGP. Como
no utiliza IDEA y RSA, su uso no estА restringido. EstА casi
completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l ja
GnuPG (GNU Privacy Guard)
╓о╔г║╪╔©╓н╟е╧Ф╡╫╓х╔г╔ё╔╦╔©╔К╫Пл╬╓н╨Ню╝╓н╓©╓А╓н GNU
╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓г╓╧║ёGnuPG ╓о╧Беы╓й╦╟╢имЩг╫но╓Р╩Щ╓а║╒ RFC2440
╓г╣╜╫р╓╣╓Л╓ф╓╓╓К OpenPGP ╔╓╔С╔©║╪╔м╔ц╔хи╦╫Ю╓ндС╟ф╓ке╛╧Г╓╥╓ф╓╓╓ч╓╧║ё
GnuPG ╓офц╣Ж╔╒╔К╔╢╔Й╔╨╔Ю╓о╩хмя╓╥╓ф╓╓╓й╓╓╓н╓г║╒PGP2
╓н╓╒╓И╓Ф╓К╔Т╔║║╪╔╦╔Г╔С ╓х╦ъ╢╧ю╜╓╛╓╒╓Й╓ч╓╩╓С║ё(PGP2.x ╓о
ю╓Ё╕е╙╓йфц╣Ж╓г╓╒╓К IDEA ╓х║╒ 2000г╞ 9╥Н20фЭ╓ч╓г USA ╓г╓нфц╣Ж╓г╓╒╓К RSA
╓н╓ъ╓Рмя╓╓╓ф╓╓╓ч╓╧)

%description -l pl
GnuPG jest narzЙdziem do bezpiecznej komunikacji i bezpiecznego
przechowywania danych. Mo©e byФ u©ywany do szyfrowania oraz
podpisywania danych. Umo©liwia zaawansowane zarz╠dzanie kluczami i
speЁnia normy zdefiniowane w standardzie OpenPGP, ktСry jest opisany w
RFC2440.

%description -l pt_BR
O GnuPG И um substituto completo e de livre distribuiГЦo para o PGP.
Como ele nЦo usa IDEA e RSA seu uso И irrestrito. EstА quase
completamente de acordo com o rascunho (draft) OpenPGP.

%description -l ru
GnuPG является полной и свободной заменой для PGP. Так как он не
использует ни IDEA, ни RSA, то на его использование не накладывается
никаких ограничений. GnuPG соответствует спецификации OpenPGP
(RFC2440).

%description -l uk
GnuPG ╓ повною та в╕льною зам╕ною PGP. В╕н не використову╓ н╕ IDEA,
ан╕ RSA, так що на його застосування не наклада╓ться н╕яких обмежень.
GnuPG в╕дпов╕да╓ специф╕кац╕╖ OpenPGP (RFC2440).

%prep
%setup -q

%build
%configure \
	--with-capabilities \
	--enable-ldap \
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/{DETAILS,FAQ,OpenPGP}

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*

%{_mandir}/man?/*
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/options.skel
