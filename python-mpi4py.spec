%define module 	mpi4py
%define name 	python-%{module}
%define version 1.1.0
%define release %mkrel 1

Summary: 	MPI for Python
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://mpi4py.googlecode.com/files/%{module}-%{version}.tar.gz
License: 	Public Domain
Group: 		Development/Python
Url: 		http://mpi4py.googlecode.com
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d
Requires:	openmpi
BuildRequires:	python-cython, openmpi, openmpi-devel
BuildRequires:	tetex-latex, python-docutils >= 0.4, python-sphinx

%description
This package provides MPI support for Python scripting in parallel
environments. It is constructed on top of the MPI-1/MPI-2
specification, but provides an object oriented interface which closely
follows the MPI-2 C++ bindings.

This module supports point-to-point (send, receive) and collective
(broadcast, scatter, gather, reduction) communications of any
picklable Python object.

For objects exporting single-segment buffer interface (strings, NumPy
arrays, etc.), blocking/nonblocking/persistent point-to-point,
collective and one-sided (put, get, accumulate) communications are
fully supported, as well as parallel I/O (blocking and nonblocking,
collective and noncollective read and write operations using explicit
file offsets, individual file pointers and shared file pointers).

There is also full support for group and communicator (inter, intra,
Cartesian and graph topologies) creation and management, as well as
creating user-defined datatypes. Additionally, there is almost
complete support for dynamic process creation and management (spawn,
name publishing).

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="-Wno-error=format-security" 
%__python setup.py build
pushd docs/source
make PAPER=letter latex
make -C build/latex all-pdf
popd 

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc test/ demo/ *.txt docs/source/build/latex/mpi4py.pdf
