Name:		goaccess
Version:	0.7.1
Release:	1%{?dist}
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
%configure --enable-debug --enable-geoip --enable-utf8
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Feb 20 2014 Christopher Meng <rpm@cicku.me> - 0.7.1-1
- Update to 0.7.1

* Sat Jan 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.7-2
- Build with $RPM_OPT_FLAGS, fix -debuginfo.

* Wed Jan 15 2014 Eduardo Echeverria <echevemaster@gmail.com> - 0.7-1
- Update to 0.7

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 19 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.6-1
- Updated to the new upstream version

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-2
- Fix license field, GPLv2+ is correct
- Add NEWS and Changelog files to %%doc

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-1
- Initial packaging
