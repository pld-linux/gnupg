Summary:	gpg - GNU Privacy Guard
Name:		gnupg
Version:	1.0.1
Release:	2
License:	GPL
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
Source0:	ftp://ftp.gnupg.org/pub/gcrypt/gnupg/%{name}-%{version}.tar.gz
Source1:	gpg.1
Icon:		gnupg.gif
URL:		http://www.gnupg.org/
BuildRequires:	gdbm-devel
BuildRequires:	zlib-devel
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


%prep
%setup -q

%build
gettextize --force --copy
LDFLAGS="-s"; export LDFLAGS
%configure \
	--without-included-gettext \
	--disable-m-debug \
	--disable-m-guard
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{_libdir}/gnupg/* || :

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

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
