Name:		goaccess
Version:	0.8.5
Release:	1%{?dist}
Summary:	Real-time web log analyzer and interactive viewer
License:	GPLv2+
URL:		http://goaccess.io/
Source0:	http://tar.goaccess.io/goaccess-%{version}.tar.gz
BuildRequires:	GeoIP-devel
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel

%description
Open source real-time web log analyzer and interactive viewer that runs
in a terminal in *nix systems. It provides fast and valuable HTTP statistics
for system administrators that require a visual server report on the fly.

Features:
GoAccess parses the specified web log file and outputs the data to the X 
terminal.

* General Statistics, bandwidth, etc.
* Time taken to serve the request (useful to track pages that are 
slowing down your site)
* Top Visitors
* Requested files & static files
* 404 or Not Found
* Hosts, Reverse DNS, IP Location
* Operating Systems
* Browsers and Spiders
* Referring Sites & URLs
* Keyphrases
* Geo Location - Continent/Country/City New
* HTTP Status Codes
* Ability to output JSON and CSV
* Different Color Schemes
* Support for large datasets and data persistence New
* Support for IPv6
* Output statistics to HTML. See report.
* Nearly all web log formats...

GoAccess allows any custom log format string. Predefined options include, 
but not limited to:

* Common Log Format (CLF) Apache
* Combined Format (XLF/ELF) Apache|Nginx
* W3C format (IIS)
* Amazon CloudFront (Download Distribution).
* Apache virtual hosts

%prep
%setup -q

%build
%configure --enable-debug --enable-geoip --enable-utf8
# --enable-tcb
# Note about Tokyo Cabinet hash table support. As you can see 0.8 onwards
# support hash table alternative from Tokyo Cabinet hash database, to replace
# GLib if needed. Basically, we can use GLib still as TC will introduce more
# dependencies.
# If upstream can prove that it's faster than GLib hash table on parsing, then
# we might switch to it.(From FAQ page I think glib is better)
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS ChangeLog COPYING README TODO
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Dec 5 2014 Eduardo Echeverria <echevemaster@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Christopher Meng <rpm@cicku.me> - 0.8.2-1
- Update to 0.8.2

* Wed Jun 18 2014 Christopher Meng <rpm@cicku.me> - 0.8.1-1
- Update to 0.8.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Christopher Meng <rpm@cicku.me> - 0.8-1
- Update to 0.8

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
