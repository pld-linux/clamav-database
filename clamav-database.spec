%define		database_version	20061227
Summary:	Virus database for clamav
Summary(pl):	Bazy wirusów dla clamav
Name:		clamav-database
Version:	0.88.7.%{database_version}
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://db.local.clamav.net/daily.cvd
# Source0-md5:	03769468fc0f2b563bc3ec5de295a4ae
Source1:	http://db.local.clamav.net/main.cvd
# Source1-md5:	347c99544205184fbc1bd23fd7cfd782
URL:		http://www.clamav.net/
Requires:	clamav
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virus database for clamav (updated %{database_version}).

%description -l pl
Bazy wirusów dla clamav (aktualizowana %{database_version}).

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/clamav,%{_sbindir}}

install %{SOURCE0} $RPM_BUILD_ROOT/var/lib/clamav
install %{SOURCE1} $RPM_BUILD_ROOT/var/lib/clamav

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_sbindir}/clamav-post-updatedb

%files
%defattr(644,root,root,755)
%attr(644,clamav,root) %verify(not md5 mtime size) /var/lib/clamav/*.cvd
