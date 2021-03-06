Summary:	Application Framework for Python 2 and PyQt
Summary(pl.UTF-8):	Szkielet dla aplikacji opartych na Pythonie 2 i PyQt
Name:		python-dip
Version:	0.4.4
Release:	1
License:	GPL v2 with exception or commercial
Group:		Development/Languages/Python
Source0:	http://www.riverbankcomputing.com/static/Downloads/dip/dip-py2-gpl-%{version}.tar.gz
# Source0-md5:	25951bcd0ce8245ce6a2d8b806e19e50
URL:		http://www.riverbankcomputing.com/static/Docs/dip/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
Requires:	python-PyQt4 >= 4.7.5
Requires:	QtGui >= 4.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dip is an application framework for Python and PyQt.

This version supports Python 2.x.

%description -l pl.UTF-8
dip to szkielet dla aplikacji opartych na Pythonie i PyQt.

Ta wersja jest przeznaczona dla Pythona 2.x.

%prep
%setup -q -n dip-py2-gpl-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog* GPL-Exception.txt LICENSE-Commercial.txt NEWS README doc/_build/html
%attr(755,root,root) %{_bindir}/dip-automate
%attr(755,root,root) %{_bindir}/dip-builder
%{py_sitescriptdir}/dip
%{py_sitescriptdir}/dip_py2_gpl-%{version}-py*.egg-info
