Summary:	gpg - GNU Privacy Guard
Summary(pl):	gpg Stra�nik Prywatno�ci GNU
Name:		gnupg
Version:	1.0.5
Release:	1
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Patch0:		%{name}-locale.patch
Patch1:		%{name}-am.patch
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
BuildRequires:	gettext-devel
BuildRequires:	libcap-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
Provides:	pgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPG is the main program for the GNUPG system. gpgm is a maintenance
tool which has some commands gpgm does not have; it is there because
it does not handle sensitive data and therefore has no need to
allocate secure memory.

%description -l pl
GPG jest g��wnym programem nale��cym do systemu GNUPG (GNU Privacy
Guard, odpowiednik programu Pretty Good Privacy na licencji GNU).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm scripts/missing
gettextize --force --copy
aclocal
autoconf
automake -a -c --no-force
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%dir %{_libdir}/gnupg
%attr(755,root,root) %{_libdir}/gnupg/*
%{_datadir}/gnupg
