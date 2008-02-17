%define		main_version		45
%define		daily_version		5854
%define		database_version	20080217
%define		rel	2
Summary:	Virus databases for clamav
Summary(pl.UTF-8):	Bazy wirusów dla clamava
Name:		clamav-database
Version:	%{main_version}.%{daily_version}
Release:	%{database_version}.%{rel}
License:	GPL
Group:		Applications/Databases
Source0:	http://db.local.clamav.net/daily.cvd
# Source0-md5:	a0999deace2c3bd8dc48a5e03523b7fa
Source1:	http://db.local.clamav.net/main.cvd
# Source1-md5:	5312db62b11f8faf48c669fb358488e0
URL:		http://www.clamav.net/
BuildRequires:	file
Requires:	clamav
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virus databases for clamav (updated %{database_version}).

%description -l pl.UTF-8
Bazy wirusów dla clamava (aktualizowane %{database_version}).

%prep
%setup -qcT
cp -a %{SOURCE0} %{SOURCE1} .

%build
main_version=$(file main.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
daily_version=$(file daily.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
if [ "$main_version" != %{main_version} ]; then
	: Update %%define main_version $main_version, and retry
	exit 1
fi
if [ "$daily_version" != %{daily_version} ]; then
	: Update %%define daily_version $daily_version, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/clamav
install *.cvd $RPM_BUILD_ROOT/var/lib/clamav

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_sbindir}/clamav-post-updatedb

%files
%defattr(644,root,root,755)
%attr(644,clamav,root) %verify(not md5 mtime size) /var/lib/clamav/*.cvd
