%define module 	mpi4py
%define name 	python-%{module}
%define version 1.3

Summary: 	MPI for Python
Name: 		%{name}
Version: 	1.3.1
Release: 	5
Source0: 	http://mpi4py.googlecode.com/files/mpi4py-%{version}.tar.gz
License: 	BSD
Group: 		Development/Python
Url: 		http://mpi4py.googlecode.com
Requires:	openmpi
BuildRequires:	python-devel
BuildRequires:	python-cython, openmpi, openmpi-devel, zlib-devel

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

%package devel
Summary:	mpi4py headers
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

%description devel 
This package contains header files needed to develop modules in C or
Fortran that can interact with mpi4py.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="-Wno-error=format-security" 
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
%__rm -f %{buildroot}%{py_platsitedir}/mpi4py/mpi.cfg
%__sed -si 's/^.*mpi\.cfg$//' FILELIST

%files -f FILELIST
%doc test/ demo/ *.txt docs/usrman docs/apiref
%exclude %{py_platsitedir}/%{module}/include/

%files devel
%{py_platsitedir}/%{module}/include/
