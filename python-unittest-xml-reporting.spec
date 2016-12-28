#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	unittest-xml-reporting
Summary:	Unittest-based test runner with Ant/JUnit like XML reporting
Name:		python-%{module}
Version:	2.1.0
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/77/27/b4442a041de8fc5366e3d0c82fa2919cba76d6fc7888635540828c740633/%{module}-%{version}.tar.gz
# Source0-md5:	9284cbfccc56b4347493f134e780fa3c
URL:		http://github.com/danielfm/unittest-xml-reporting/tree/master/
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python2}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools,
such as build systems, IDEs and continuous integration servers.

%package -n python3-%{module}
Summary:	Unittest-based test runner with Ant/JUnit like XML reporting
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
unittest-xml-reporting is a unittest test runner that can save test
results to XML files that can be consumed by a wide range of tools,
such as build systems, IDEs and continuous integration servers.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/unittest_xml_report*egg-info
%{py_sitescriptdir}/xmlrunner

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO
%{py3_sitescriptdir}/unittest_xml_report*egg-info
%{py3_sitescriptdir}/xmlrunner
