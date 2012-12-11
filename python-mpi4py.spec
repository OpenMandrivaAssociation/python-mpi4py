%define module 	mpi4py
%define name 	python-%{module}
%define version 1.3
%define rel		4
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define release %rel
%endif

Summary: 	MPI for Python
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://mpi4py.googlecode.com/files/%{module}-%{version}.tar.gz
License: 	BSD
Group: 		Development/Python
Url: 		http://mpi4py.googlecode.com
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST
%__rm -f %{buildroot}%{py_platsitedir}/mpi4py/mpi.cfg
%__sed -si 's/^.*mpi\.cfg$//' FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc test/ demo/ *.txt docs/usrman docs/apiref
%exclude %{py_platsitedir}/%{module}/include/

%files devel
%defattr(-,root,root)
%{py_platsitedir}/%{module}/include/


%changelog
* Tue Apr 24 2012 Lev Givon <lev@mandriva.org> 1.3-4
+ Revision: 793216
- Correct license.

* Tue Apr 24 2012 Lev Givon <lev@mandriva.org> 1.3-3
+ Revision: 793204
- Require zlib as build req.

* Wed Feb 22 2012 Lev Givon <lev@mandriva.org> 1.3-2
+ Revision: 779268
- Rebuild.

* Mon Feb 20 2012 Lev Givon <lev@mandriva.org> 1.3-1
+ Revision: 778252
- Update to 1.3.

* Sun Oct 31 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.2.2-2mdv2011.0
+ Revision: 590963
- rebuild for new python 2.7

* Tue Sep 14 2010 Lev Givon <lev@mandriva.org> 1.2.2-1mdv2011.0
+ Revision: 578335
- Update to 1.2.2.

* Tue Mar 23 2010 Lev Givon <lev@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 526949
- Update to 1.2.1.
- Update to 1.2.
  Put header files in a devel package.

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2010.0
+ Revision: 415363
- rebuild for new libtorque

* Mon Jul 13 2009 Lev Givon <lev@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 395522
- Update to 1.1.0.

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 371315
- Update to 1.0.0.

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 0.6.0-4mdv2009.1
+ Revision: 320930
- fix str fmt
- adjust BR

* Tue Sep 16 2008 Lev Givon <lev@mandriva.org> 0.6.0-4mdv2009.0
+ Revision: 285238
- Include openmpi as a build req so that the module is build with mpicc.

* Wed Sep 03 2008 Lev Givon <lev@mandriva.org> 0.6.0-3mdv2009.0
+ Revision: 279886
- Rebuild against latest version of openmpi.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 269034
- rebuild early 2009.0 package (before pixel changes)

  + Lev Givon <lev@mandriva.org>
    - Update to 0.6.0.

* Mon May 19 2008 Lev Givon <lev@mandriva.org> 0.5.0-2mdv2009.0
+ Revision: 208969
- Rebuild against latest release of openmpi.

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-1mdv2008.1
+ Revision: 166046
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 20 2007 Lev Givon <lev@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 67961
- Update to 0.5.0.

* Thu May 10 2007 Lev Givon <lev@mandriva.org> 0.4.0rc4-1mdv2008.0
+ Revision: 26039
- Build against openmpi instead of mpich2.


* Mon Nov 06 2006 Lev Givon <lev@mandriva.org> 0.4.0rc2-1mdv2007.0
+ Revision: 76967
- Fix build deps.
- Add files.

