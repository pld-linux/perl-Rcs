%include	/usr/lib/rpm/macros.perl
Summary:	Rcs perl module
Summary(pl):	Modu³ perla Rcs
Name:		perl-Rcs
Version:	0.09
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Rcs/Rcs-%{version}.tar.gz
Patch:		perl-Rcs-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rcs - provides an object oriented interface to access Revision Control System
(RCS) utilities.

%description -l pl
Rcs - umo¿liwia dostêp do narzêdzi Systemu Kontroli Rewizji (RCS).

%prep
%setup -q -n Rcs-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

cp -ar examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Rcs
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ANNOUNCE}.gz

%{perl_sitelib}/Rcs.pm
%{perl_sitearch}/auto/Rcs

%{_mandir}/man3/*

/usr/src/examples/%{name}-%{version}
