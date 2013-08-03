Name:		goaccess		
Version:	0.6
Release:	2%{?dist}
Summary:	Apache Log Analyzer

License:	GPLv2+	
URL:		http://goaccess.prosoftcorp.com/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ncurses-devel
BuildRequires:	glib2-devel
BuildRequires:	GeoIP-devel	

%description
Open source real-time web log analyzer and interactive viewer that runs
in a terminal in *nix systems. It provides fast and valuable HTTP statistics
for system administrators that require a visual server report on the fly.

%prep
%setup -q


%build
%configure --enable-geoip
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc COPYING README AUTHORS TODO NEWS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.6-1
- Updated to the new upstream version

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-2
- Fix license field, GPLv2+ is correct
- Add NEWS and Changelog files to %%doc

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-1
- Initial packaging

