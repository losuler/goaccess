Name:           goaccess
Version:        0.9.3
Release:        1%{?dist}
Summary:        Real-time web log analyzer and interactive viewer
License:        GPLv2+
URL:            http://goaccess.io/
Source0:        http://tar.goaccess.io/goaccess-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  GeoIP-devel
BuildRequires:  glib2-devel
BuildRequires:  ncurses-devel

%description
GoAccess is a real-time web log analyzer and interactive viewer that runs in a
terminal in *nix systems. It provides fast and valuable HTTP statistics for
system administrators that require a visual server report on the fly.

Features:
GoAccess parses the specified web log file and outputs the data to terminal.

* General statistics, bandwidth, etc.
* Time taken to serve the request (useful to track pages that are slowing down.
your site).
* Metrics for cumulative, average and slowest running requests.
* Top visitors.
* Requested files & static files.
* 404 or Not Found.
* Hosts, Reverse DNS, IP Location.
* Operating Systems.
* Browsers and Spiders.
* Referring Sites & URLs.
* Keyphrases.
* Geo Location - Continent/Country/City.
* Visitors Time Distribution.
* HTTP Status Codes.
* Ability to output JSON and CSV.
* Tailor GoAccess to suit your own color taste/schemes.
* Support for large datasets + data persistence.
* Support for IPv6.
* Output statistics to HTML. 
and more...

GoAccess allows any custom log format string. Predefined options include, but
not limited to:

* Amazon CloudFront (Download Distribution).
* AWS Elastic Load Balancing.
* Apache/Nginx Common/Combined + VHosts.
* Google Cloud Storage.
* W3C format (IIS).

%prep
%setup -q
# Prevent flags being overridden again and again.
#sed -i 's|-pthread|$CFLAGS \0|' configure.ac
sed -i '/-pthread/d' configure.ac
sed -i 's|storage:|LDFLAGS = $LIBS $LDFLAGS \n  \0|' configure.ac
# No math function found.
sed -i '/goaccess_LDADD/d' Makefile.am

%build
# --enable-tcb
# Note about Tokyo Cabinet hash table support: As you can see 0.8 onwards
# supports hash table alternative from Tokyo Cabinet hash database, to replace
# GLib if needed. Basically, we can use GLib still as TC will introduce more
# dependencies.
# If upstream can prove that it's faster than GLib hash table on parsing, then
# we might switch to it.(From FAQ page I think glib is better)
#
# --enable-debug
# Maintainers need this option to determine if a bug is caused by downstream,
# or by design flaw, this option won't affect efficiency and speed.
autoreconf -fiv
%configure --enable-debug --enable-geoip --enable-utf8
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Aug 27 2015 Christopher Meng <rpm@cicku.me> - 0.9.3-1
- Update to 0.9.3

* Fri Dec 5 2014 Eduardo Echeverria <echevemaster@gmail.com> - 0.8.5-1
- Update to 0.8.5

* Tue Jul 22 2014 Christopher Meng <rpm@cicku.me> - 0.8.2-1
- Update to 0.8.2

* Wed Jun 18 2014 Christopher Meng <rpm@cicku.me> - 0.8.1-1
- Update to 0.8.1

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

* Fri Jul 19 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.6-1
- Updated to the new upstream version

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-2
- Fix license field, GPLv2+ is correct
- Add NEWS and Changelog files to %%doc

* Sat May 25 2013 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5-1
- Initial packaging
