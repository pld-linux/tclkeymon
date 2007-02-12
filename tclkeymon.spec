Summary:	Tclkeymon - Monitor the Toshiba keys, and respond appropriately
Summary(pl.UTF-8):	Tclkeymon - monitorowanie i reagowanie na klawisze Toshiby
Name:		tclkeymon
Version:	0.51
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/tclmonkeys/%{name}-%{version}.tar.gz
# Source0-md5:	ce72637faa6084bdaf8a8aef5701b675
URL:		http://sourceforge.net/projects/tclkeymon/
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tclkeymon is a demon, writen in Tcl, for Toshiba laptops that use ACPI
and the Toshiba-ACPI extensions. It monitors function keys and Toshiba
specific buttons (including the CD-player buttons, and the state of
the laptop lid), and responds appropriately.

%description -l pl.UTF-8
Tclkeymon to napisany w Tcl-u demon dla laptopów Toshiby
wykorzystujący ACPI wraz z rozszerzeniami Toshiby. Monitoruje klawisze
funkcjne i specyficzne dla Toshiby (włącznie z przyciskami odtwarzacza
CD i stanem pokrywy laptopa) i odpowiednio na nie reaguje.

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

install etc/*  $RPM_BUILD_ROOT%{_sysconfdir}
install *tclkeymon*	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun 
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc HISTORY Changelog README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
