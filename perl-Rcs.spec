%include	/usr/lib/rpm/macros.perl
Summary:	Rcs perl module
Summary(pl):	Modu³ perla Rcs
Name:		perl-Rcs
Version:	1.03
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Rcs/Rcs-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rcs - provides an object oriented interface to access Revision Control
System (RCS) utilities.

%description -l pl
Rcs - umo¿liwia dostêp do narzêdzi Systemu Kontroli Rewizji (RCS).

%prep
%setup -q -n Rcs-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Rcs.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
