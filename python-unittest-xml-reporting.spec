
%define 	module	unittest-xml-reporting

Summary:	Unittest-based test runner with Ant/JUnit like XML reporting.
Name:		python-%{module}
Version:	1.2
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/u/unittest-xml-reporting/%{module}-%{version}.tar.gz
# Source0-md5:	cc1f1f576ed46c5f5cd127ce99ff1e4a
URL:		http://github.com/danielfm/unittest-xml-reporting/tree/master/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unittest-xml-reporting is a unittest test runner that can save test results to XML files that can be consumed by a wide range of tools, such as build systems, IDEs and continuous integration servers.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/unittest_xml_report*egg-info
%{py_sitescriptdir}/xmlrunner
