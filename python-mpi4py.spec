%define module mpi4py

Summary:	MPI for Python
Name:		python-%{module}
Version:	1.3.1
Release:	2
License:	BSD
Group:		Development/Python
Url:		http://mpi4py.googlecode.com
Source0:	http://mpi4py.googlecode.com/files/%{module}-%{version}.tar.gz
BuildRequires:	openmpi
BuildRequires:	python-cython
BuildRequires:	pkgconfig(ompi)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)
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

%files -f FILELIST
%doc test/ demo/ *.txt docs/usrman docs/apiref
%exclude %{py_platsitedir}/%{module}/include/

#----------------------------------------------------------------------------

%package devel
Summary:	mpi4py headers
Group:		Development/Python
Requires:	%{name} = %{EVRD}

%description devel
This package contains header files needed to develop modules in C or
Fortran that can interact with mpi4py.

%files devel
%{py_platsitedir}/%{module}/include/

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="-Wno-error=format-security"
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=FILELIST
rm -f %{buildroot}%{py_platsitedir}/mpi4py/mpi.cfg
sed -si 's/^.*mpi\.cfg$//' FILELIST

