#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Rcs perl module
Summary(pl):	Modu³ Perla Rcs
Name:		perl-Rcs
Version:	1.05
Release:	1
# same as perl
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Rcs/Rcs-%{version}.tar.gz
# Source0-md5:	f3466fe6cef54f8780d753fa0995b0ac
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rcs - provides an object oriented interface to access Revision Control
System (RCS) utilities.

%description -l pl
Rcs - umo¿liwia dostêp do narzêdzi Systemu Kontroli Rewizji (RCS).

%prep
%setup -q -n Rcs-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ANNOUNCE
%{perl_vendorlib}/Rcs.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
