%define pypi_name zope_hookable

Name:		python-zope-hookable
Version:	8.2
Release:	1
Summary:	Zope hookable
URL:		https://pypi.org/project/zope-hookable/
License:	None
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package supports the efficient creation of "hookable" objects,
which are callable objects that are meant to be optionally replaced.

The idea is that you create a function that does some default thing
and make it hookable.

Later, someone can modify what it does by calling its sethook method
and changing its implementation. All users of the function, including
those that imported it, will see the change.

Documentation is hosted at https://zopehookable.readthedocs.io

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf src/zope.component.egg-info

%files
%doc README.rst
%license LICENSE.txt COPYRIGHT.txt
%{python_sitearch}/zope
%{python_sitearch}/%{pypi_name}-%{version}.dist-info
