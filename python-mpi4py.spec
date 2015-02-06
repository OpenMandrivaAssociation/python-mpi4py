%define module mpi4py

Summary:	MPI for Python
Name:		python-%{module}
Version:	1.3.1
Release:	3
License:	BSD
Group:		Development/Python
Url:		http://mpi4py.googlecode.com
Source0:	http://mpi4py.googlecode.com/files/%{module}-%{version}.tar.gz
Patch0:		mpi4py-1.3.1-linkage.patch
Patch1:		mpi4py-1.3.1-openmpi1.7.patch
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
%package -n python2-%{module}
Summary: MPI (Message Passing Interface) for Python 2.x
Group: Development/Python

%description -n python2-%{module}
MPI (Message Passing Interface) for Python 2.x

%files -f FILELIST.py2
%doc test/ demo/ *.txt docs/usrman docs/apiref
%exclude %{py2_platsitedir}/%{module}/include/

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

%package -n python2-%{module}-devel
Summary:	mpi4py headers
Group:		Development/Python
Requires:	python2-%{module} = %{EVRD}

%description -n python2-%{module}-devel
This package contains header files needed to develop modules in C or
Fortran that can interact with mpi4py.

%files -n python2-%{module}-devel
%{py2_platsitedir}/%{module}/include/

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}
%apply_patches

mkdir py2
cp -a `ls |grep -v py2 py2/`

%build
export CFLAGS="-Wno-error=format-security"

cd py2
python2 setup.py build
cd ..

python setup.py build

%install
cd py2
PYTHONDONTWRITEBYTECODE=true python2 setup.py install --root=%{buildroot} --record=FILELIST.py2
rm -f %{buildroot}%{py2_platsitedir}/mpi4py/mpi.cfg
cd ..

PYTHONDONTWRITEBYTECODE=true python setup.py install --root=%{buildroot} --record=FILELIST
rm -f %{buildroot}%{py_platsitedir}/mpi4py/mpi.cfg
sed -si 's/^.*mpi\.cfg$//' FILELIST FILELIST.py2

