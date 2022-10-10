%global module	mpi4py
%global fname %(n=%{name}; echo ${n:0:1})

Summary:	MPI for Python
Name:		python-%{module}
Version:	3.1.3
Release:	1
Group:		Development/Python
License:	Public Domain
Url:		https://github.com/mpi4py/mpi4py
Source0:	https://pypi.io/packages/source/%{fname}/%{module}/%{module}-%{version}.tar.gz
#Source0:	%{url}/archive/refs/tags/%{version}/%{module}-%{version}.tar.gz
#Patch0:		mpi4py-1.3.1-linkage.patch
#Patch1:		mpi4py-1.3.1-openmpi1.7.patch

BuildRequires: openmpi
BuildRequires: pkgconfig(ompi)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(python3)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(cython)
BuildRequires: python3dist(setuptools)
# For testing
#BuildRequires: python3dist(dill)
BuildRequires: python3dist(numpy)
BuildRequires: python3dist(simplejson)
BuildRequires: python3dist(pyyaml)

Requires:	openmpi

%description
MPI for Python provides bindings of the Message Passing Interface
(MPI) standard for the Python programming language, allowing any
Python program to exploit multiple processors.

This package is constructed on top of the MPI-1/2 specifications and
provides an object oriented interface which closely follows MPI-2 C++
bindings. It supports point-to-point (sends, receives) and collective
(broadcasts, scatters, gathers) communications of any picklable Python
object, as well as optimized communications of Python object exposing
the single-segment buffer interface (NumPy arrays, builtin
bytes/string/array objects).

%files
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for mpi4py
Group:		Development/Python
BuildArch:	noarch

%description doc
This package contains documentation for MPI for Python.

%files doc
%doc demo/
%doc docs/*
%doc test/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}

# delete docs/source
# this is just needed to generate docs/*
rm -r docs/source

%build
export PATH=%{_libdir}/openmpi/bin/:$PATH
export CC=mpicc
export CXX=mpicxx
%py_build

%install
%py_install

#rm -f %{buildroot}%{python3_sitearch}/mpi4py/mpi.cfg

