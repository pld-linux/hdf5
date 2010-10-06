# TODO:
# - build with MPICH
# - check missing file
#
# Conditional build:
%bcond_without	szip	# build without SZIP support
#
Summary:	Hierarchical Data Format 5 library
Summary(pl.UTF-8):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
Version:	1.8.5.patch1
Release:	1
License:	Nearly BSD, but changed sources must be marked
Group:		Libraries
Source0:	ftp://ftp.hdfgroup.org/HDF5/current/src/%{name}-1.8.5-patch1.tar.gz
# Source0-md5:	d22a35a17877e369055ed50da5ba91fa
Patch0:		%{name}-config.patch
Patch1:		%{name}-sig.patch
Patch2:		%{name}-link.patch
URL:		http://www.hdfgroup.org/HDF5/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{?with_szip:BuildRequires:	szip-devel >= 2.0}
BuildRequires:	zlib-devel >= 1.1.3
Obsoletes:	hdf5_hl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%description -l pl.UTF-8
HDF5 jest całkowicie nowym produktem Hierarchiczego Formatu Danych,
składającym się ze specyfikacji formatu danych oraz obsługującej go
biblioteki. HDF5 został zaprojektowany aby pozbyć się ograniczeń
poprzedniego HDF oraz żeby zaspokoić bieżące i przyszłe potrzeby
współczesnych systemów i aplikacji.

%package devel
Summary:	HDF5 library development package
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki HDF5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_szip:Requires:	szip-devel >= 2.0}
Requires:	zlib-devel
Obsoletes:	hdf5_hl-devel
Obsoletes:	hdf5_hl-tutor

%description devel
Header files for HDF5 library and HDF5 documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HDF5 oraz dokumentacja HDF5.

%package static
Summary:	HDF5 static library
Summary(pl.UTF-8):	Statyczna biblioteka HDF5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	hdf5_hl-static

%description static
Static version of HDF5 library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki HDF5.

%package c++
Summary:	C++ APIs for HDF5
Summary(pl.UTF-8):	API C++ bibliotek HDF5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ APIs for HDF5 (both base hdf5 and hdf5_hl).

%description c++ -l pl.UTF-8
API C++ dla bibliotek HDF5 (zarówno podstawowej hdf5, jak i hdf5_hl).

%package c++-devel
Summary:	Header files for HDF5 C++ APIs
Summary(pl.UTF-8):	Pliki nagłówkowe API C++ bibliotek HDF5
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for HDF5 C++ APIs (both base hdf5 and hdf5_hl).

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe API C++ bibliotek HDF5 (zarówno podstawowej hdf5, jak
i hdf5_hl).

%package c++-static
Summary:	C++ APIs for HDF5 - static libraries
Summary(pl.UTF-8):	API C++ bibliotek HDF5 - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
C++ APIs for HDF5 (both base hdf5 and hdf5_hl) - static libraries.

%description c++-static -l pl.UTF-8
API C++ dla bibliotek HDF5 (zarówno podstawowej hdf5, jak i hdf5_hl) -
biblioteki statyczne.

%package progs
Summary:	HDF5 utilities
Summary(pl.UTF-8):	Narzędzia do plików HDF5
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description progs
Utilities to convert from/to HDF5 format.

%description progs -l pl.UTF-8
Narzędzia do konwersji z i to formatu HDF5.

%prep
%setup -q -n %{name}-1.8.5-patch1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--docdir=%{_docdir} \
	--enable-cxx \
	--enable-linux-lfs \
	--enable-production \
	--with-pthread \
	%{?with_szip:--with-szlib}

#	--enable-threadsafe is incompatible with cxx/fortran
#	--enable-fortran  - requires Fortran90 compiler

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install-recursive \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/hl
%{__make} -C examples install-examples \
	EXAMPLEDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/c \
	EXAMPLETOPDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__make} -C c++/examples install-examples \
	EXAMPLEDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/c++
%{__make} -C hl/examples install-examples \
	EXAMPLEDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/hl/c \
	EXAMPLETOPDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/hl
%{__make} -C hl/c++/examples install-examples \
	EXAMPLEDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/hl/c++

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.txt release_docs/{HISTORY*.txt,RELEASE.txt}
%attr(755,root,root) %{_libdir}/libhdf5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5.so.6
%attr(755,root,root) %{_libdir}/libhdf5_hl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl.so.6
# used to show configuration at runtime
%{_libdir}/libhdf5.settings

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h5cc
%attr(755,root,root) %{_libdir}/libhdf5.so
%attr(755,root,root) %{_libdir}/libhdf5_hl.so
%{_libdir}/libhdf5.la
%{_libdir}/libhdf5_hl.la
%{_includedir}/H5ACpublic.h
%{_includedir}/H5Apublic.h
%{_includedir}/H5Cpublic.h
%{_includedir}/H5DSpublic.h
%{_includedir}/H5Dpublic.h
%{_includedir}/H5Epubgen.h
%{_includedir}/H5Epublic.h
%{_includedir}/H5FDcore.h
%{_includedir}/H5FDdirect.h
%{_includedir}/H5FDfamily.h
%{_includedir}/H5FDlog.h
%{_includedir}/H5FDmpi.h
%{_includedir}/H5FDmpio.h
%{_includedir}/H5FDmpiposix.h
%{_includedir}/H5FDmulti.h
%{_includedir}/H5FDpublic.h
%{_includedir}/H5FDsec2.h
%{_includedir}/H5FDstdio.h
%{_includedir}/H5Fpublic.h
%{_includedir}/H5Gpublic.h
%{_includedir}/H5IMpublic.h
%{_includedir}/H5Include.h
%{_includedir}/H5Ipublic.h
%{_includedir}/H5LTpublic.h
%{_includedir}/H5Lpublic.h
%{_includedir}/H5MMpublic.h
%{_includedir}/H5Opublic.h
%{_includedir}/H5PTpublic.h
%{_includedir}/H5Ppublic.h
%{_includedir}/H5Rpublic.h
%{_includedir}/H5Spublic.h
%{_includedir}/H5TBpublic.h
%{_includedir}/H5Tpublic.h
%{_includedir}/H5Zpublic.h
%{_includedir}/H5api_adpt.h
%{_includedir}/H5overflow.h
%{_includedir}/H5pubconf.h
%{_includedir}/H5public.h
%{_includedir}/H5version.h
%{_includedir}/hdf5.h
%{_includedir}/hdf5_hl.h
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/run-all-ex.sh
%{_examplesdir}/%{name}-%{version}/c
%dir %{_examplesdir}/%{name}-%{version}/hl
%{_examplesdir}/%{name}-%{version}/hl/run-hl-ex.sh
%{_examplesdir}/%{name}-%{version}/hl/c

%files static
%defattr(644,root,root,755)
%{_libdir}/libhdf5.a
%{_libdir}/libhdf5_cpp.a
%{_libdir}/libhdf5_hl.a
%{_libdir}/libhdf5_hl_cpp.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_cpp.so.6
%attr(755,root,root) %{_libdir}/libhdf5_hl_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl_cpp.so.6

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h5c++
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so
%attr(755,root,root) %{_libdir}/libhdf5_hl_cpp.so
%{_libdir}/libhdf5_cpp.la
%{_libdir}/libhdf5_hl_cpp.la
%{_includedir}/H5AbstractDs.h
%{_includedir}/H5ArrayType.h
%{_includedir}/H5AtomType.h
%{_includedir}/H5Attribute.h
%{_includedir}/H5Classes.h
%{_includedir}/H5CommonFG.h
%{_includedir}/H5CompType.h
%{_includedir}/H5Cpp.h
%{_includedir}/H5CppDoc.h
%{_includedir}/H5DataSet.h
%{_includedir}/H5DataSpace.h
%{_includedir}/H5DataType.h
%{_includedir}/H5DcreatProp.h
%{_includedir}/H5DxferProp.h
%{_includedir}/H5EnumType.h
%{_includedir}/H5Exception.h
%{_includedir}/H5FaccProp.h
%{_includedir}/H5FcreatProp.h
%{_includedir}/H5File.h
%{_includedir}/H5FloatType.h
%{_includedir}/H5Group.h
%{_includedir}/H5IdComponent.h
%{_includedir}/H5IntType.h
%{_includedir}/H5Library.h
%{_includedir}/H5Object.h
%{_includedir}/H5PacketTable.h
%{_includedir}/H5PredType.h
%{_includedir}/H5PropList.h
%{_includedir}/H5StrType.h
%{_includedir}/H5VarLenType.h
%{_examplesdir}/%{name}-%{version}/c++
%{_examplesdir}/%{name}-%{version}/hl/c++

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gif2h5
%attr(755,root,root) %{_bindir}/h52gif
%attr(755,root,root) %{_bindir}/h5copy
%attr(755,root,root) %{_bindir}/h5debug
%attr(755,root,root) %{_bindir}/h5diff
%attr(755,root,root) %{_bindir}/h5dump
%attr(755,root,root) %{_bindir}/h5import
%attr(755,root,root) %{_bindir}/h5jam
%attr(755,root,root) %{_bindir}/h5ls
%attr(755,root,root) %{_bindir}/h5mkgrp
%attr(755,root,root) %{_bindir}/h5perf_serial
%attr(755,root,root) %{_bindir}/h5redeploy
%attr(755,root,root) %{_bindir}/h5repack
%attr(755,root,root) %{_bindir}/h5repart
%attr(755,root,root) %{_bindir}/h5stat
%attr(755,root,root) %{_bindir}/h5unjam
