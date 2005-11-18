#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	Ex-Simple-List
Summary:	A simple interface to Gtk2's complex MVC list widget
Summary(pl):	Prosty interfejs do z³o¿onego widgetu listy MVC w Gtk2
Name:		perl-%{pdir}-%{pnam}
Version:	0.50
Release:	1
License:	LGPL	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f66c71bbb794b699f0c3e8ca7cebc35b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Gtk2 >= 1.101-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple interface to Gtk2's complex MVC list widget.

%description -l pl
Prosty interfejs do z³o¿onego widgetu listy MVC w Gtk2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Gtk2/Ex/Simple
%{perl_vendorlib}/Gtk2/Ex/Simple/List.pm
%{perl_vendorlib}/Gtk2/Ex/Simple/TiedCommon.pm
%{perl_vendorlib}/Gtk2/Ex/Simple/TiedList.pm
%{_mandir}/man3/*
