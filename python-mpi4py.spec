%define module 	mpi4py
%define name 	python-%{module}
%define version 0.5.0
%define release %mkrel 1

Summary: 	MPI for Python
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.tar.bz2
License: 	Public Domain
Group: 		Development/Python
Url: 		http://mpi4py.scipy.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.3
Requires:	openmpi
BuildRequires:	openmpi-devel, python-devel >= 2.3

%description

MPI for Python provides an object oriented approach to message passing
in Python. Care was taken to translate the syntax and semantics of the
standard MPI-2 bindings for C++ to Python. Any user of the standard
C/C++ MPI bindings should be able to use this module without learning
how to use a new interface.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs/*.txt tests/ README.txt LICENSE.txt
