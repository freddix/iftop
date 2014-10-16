%define		pre	pre4
Summary:	Display bandwidth usage on an interface
Name:		iftop
Version:	1.0
Release:	0.%{pre}.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.ex-parrot.com/~pdw/iftop/download/%{name}-%{version}%{pre}.tar.gz
# Source0-md5:	7e6decb4958e8a4890cccac335239f24
URL:		http://www.ex-parrot.com/~pdw/iftop/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iftop does for network usage what top(1) does for CPU usage. It
listens to network traffic on a named interface and displays a table
of current bandwidth usage by pairs of hosts. Handy for answering the
question "why is our ADSL link so slow?".

%prep
%setup -q -n %{name}-%{version}%{pre}

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-resolver=getnameinfo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS TODO
%attr(755,root,root) %{_sbindir}/iftop
%{_mandir}/man8/iftop.8*

