%define		main_version		52
%define		daily_version		1197
%define		bytecode_version	50
%define		safebrowsing_version	2388
%define		database_version	20100920
%define		rel	1
Summary:	Virus databases for clamav
Summary(hu.UTF-8):	Vírus adatbázis clamav-hoz
Summary(pl.UTF-8):	Bazy wirusów dla clamava
Name:		clamav-database
Version:	%{main_version}.%{daily_version}.%{bytecode_version}.%{safebrowsing_version}
Release:	%{database_version}.%{rel}
License:	GPL
Group:		Applications/Databases
Source0:	http://db.local.clamav.net/main.cvd
# Source0-md5:	b1e43b47f292fe18f5fd6155925b756b
Source1:	http://db.local.clamav.net/daily.cvd
# Source1-md5:	1bedb4000f2039d9c6f9a08e61733418
Source2:	http://db.local.clamav.net/bytecode.cvd
# Source2-md5:	6607d0a07b3e6f13a60aba0e00d23036
Source3:	http://db.local.clamav.net/safebrowsing.cvd
# Source3-md5:	bd31f2e47fbcd046d4436330c404ed67
URL:		http://www.clamav.net/
BuildRequires:	file
Requires:	clamav
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virus databases for clamav (updated %{database_version}).

%description  -l hu.UTF-8
Vírus adatbázis clamavhoz (%{database_version}).

%description -l pl.UTF-8
Bazy wirusów dla clamava (aktualizowane %{database_version}).

%prep
%setup -qcT
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
main_version=$(file main.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
daily_version=$(file daily.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
bytecode_version=$(file bytecode.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
safebrowsing_version=$(file safebrowsing.cvd | awk -F, '/version/{print $2}' | awk '{print $NF}')
if [ "$main_version" != %{main_version} ]; then
	: Update %%define main_version $main_version, and retry
	exit 1
fi
if [ "$daily_version" != %{daily_version} ]; then
	: Update %%define daily_version $daily_version, and retry
	exit 1
fi
if [ "$bytecode_version" != %{bytecode_version} ]; then
	: Update %%define bytecode_version $bytecode_version, and retry
	exit 1
fi
if [ "$safebrowsing_version" != %{safebrowsing_version} ]; then
	: Update %%define safebrowsing_version $safebrowsing_version, and retry
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
