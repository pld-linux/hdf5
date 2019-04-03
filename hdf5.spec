# TODO:
# - finish (optional) MPI support (1.8.14: fails on mpi_file_open check)
# - check missing file
#
# Conditional build:
%bcond_without	fortran2003	# Fortran 2003 interface
%bcond_without	szip		# SZIP compression support
%bcond_with	mpi		# parallel version of library using MPI
#
Summary:	Hierarchical Data Format 5 library
Summary(pl.UTF-8):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
Version:	1.10.5
Release:	1
License:	Nearly BSD, but changed sources must be marked
Group:		Libraries
Source0:	https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	7c19d6b81ee2a3ba7d36f6922b2f90d3
Patch0:		%{name}-sig.patch
Patch1:		%{name}-cmake.patch
Patch2:		%{name}-sh.patch
URL:		https://support.hdfgroup.org/HDF5/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gcc-fortran >= %{?with_fortran2003:6:4.2}%{!?with_fortran2003:5:4.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
%{?with_mpi:BuildRequires:	mpi-devel}
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

%package fortran
Summary:	Fortran APIs for HDF5
Summary(pl.UTF-8):	API Fortran bibliotek HDF5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fortran
Fortran APIs for HDF5 (both base hdf5 and hdf5_hl).

%description fortran -l pl.UTF-8
API Fortran dla bibliotek HDF5 (zarówno podstawowej hdf5, jak i
hdf5_hl).

%package fortran-devel
Summary:	Header files for HDF5 Fortran APIs
Summary(pl.UTF-8):	Pliki nagłówkowe API Fortran bibliotek HDF5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-fortran = %{version}-%{release}
Requires:	gcc-fortran >= %{?with_fortran2003:6:4.2}%{!?with_fortran2003:5:4.0}

%description fortran-devel
Module and header files for HDF5 Fortran APIs (both base hdf5 and
hdf5_hl).

%description fortran-devel -l pl.UTF-8
Moduły i pliki nagłówkowe API C++ bibliotek HDF5 (zarówno podstawowej
hdf5, jak i hdf5_hl).

%package fortran-static
Summary:	Fortran APIs for HDF5 - static libraries
Summary(pl.UTF-8):	API Fortran bibliotek HDF5 - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-fortran-devel = %{version}-%{release}

%description fortran-static
Fortran APIs for HDF5 (both base hdf5 and hdf5_hl) - static libraries.

%description fortran-static -l pl.UTF-8
API Fortran dla bibliotek HDF5 (zarówno podstawowej hdf5, jak i
hdf5_hl) - biblioteki statyczne.

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
%setup -q
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
	--disable-silent-rules \
	--enable-build-node=production \
	--enable-cxx \
	--enable-fortran \
	%{?with_fortran2003:--enable-fortran2003} \
	%{?with_mpi:--enable-parallel --enable-unsupported} \
	--enable-shared \
	--with-optimization="" \
	--with-pthread \
	%{?with_szip:--with-szlib}

#	--enable-threadsafe is unspported with cxx/fortran/java/hl

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

install -d $RPM_BUILD_ROOT%{_libdir}/cmake/hdf5
vmajor=$(sed -ne 's/^#define H5_VERS_MAJOR\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vminor=$(sed -ne 's/^#define H5_VERS_MINOR\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vrel=$(sed -ne 's/^#define H5_VERS_RELEASE\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vsubr=$(sed -ne 's/^#define H5_VERS_SUBRELEASE\s*"\?\([^" \t]\+\)"\?.*/\1/p' src/H5public.h)
for f in hdf5-config-version.cmake hdf5-config.cmake hdf5-targets.cmake hdf5-targets-noconfig.cmake ; do
	sed -e 's,@HDF5_PACKAGE@,hdf5,g' \
	    -e 's,@HDF_PACKAGE_EXT@,,' \
	    -e "s,@HDF5_VERSION_STRING@,%{version}," \
	    -e "s,@HDF5_VERSION_MAJOR@,1.8," \
	    -e "s,@HDF5_VERSION_MINOR@,$vrel," \
	    -e "s,@H5_VERS_MAJOR@,$vmajor," \
	    -e "s,@H5_VERS_MINOR@,$vminor," \
	    -e "s,@H5_VERS_RELEASE@,$vrel," \
	    -e "s,@H5_VERS_SUBRELEASE@,$vsubr," \
	    -e 's,@HDF5_ENABLE_PARALLEL@,OFF,' \
	    -e 's,@HDF5_BUILD_FORTRAN@,ON,' \
	    -e 's,@HDF5_ENABLE_F2003@,%{?with_fortran2003:ON}%{!?with_fortran2003:OFF},' \
	    -e 's,@HDF5_BUILD_CPP_LIB@,ON,' \
	    -e 's,@HDF5_BUILD_TOOLS@,ON,' \
	    -e 's,@HDF5_BUILD_HL_LIB@,ON,' \
	    -e 's,@HDF5_ENABLE_Z_LIB_SUPPORT@,ON,' \
	    -e 's,@HDF5_ENABLE_SZIP_SUPPORT@,%{?with_szip:ON}%{!?with_szip:OFF},' \
	    -e 's,@HDF5_ENABLE_SZIP_ENCODING@,%{?with_szip:ON}%{!?with_szip:OFF},' \
%ifarch %{ix86} x32
	    -e 's,@CMAKE_SIZEOF_VOID_P@,4,' \
%else
%ifarch %{x8664}
	    -e 's,@CMAKE_SIZEOF_VOID_P@,8,' \
%endif
%endif
	    -e 's,@BUILD_SHARED_LIBS@,ON,' \
	    -e 's,@HDF5_PACKAGE_EXTLIBS@,OFF,' \
	    -e 's,@ZLIB_PACKAGE_NAME@,zlib,' \
	    -e 's,@SZIP_PACKAGE_NAME@,szip,' \
	    -e 's,@HDF5_LIBRARIES_TO_EXPORT@,hdf5,' \
	    -e 's,@CMAKE_GENERATOR_TOOLSET@,,' \
	    -e 's,@lib@,%{_lib},' \
	    %{?with_mpi:-e 's,@MPI_C_INCLUDE_PATH@,%{_includedir},'} \
	    %{?with_mpi:-e 's,@MPI_C_LIBRARIES@,%{_libdir},'} \
	    -e 's,@PACKAGE_INCLUDE_INSTALL_DIR@,%{_includedir},' \
	    -e 's,@PACKAGE_SHARE_INSTALL_DIR@,%{_libdir}/cmake,' \
	    -e 's,@PACKAGE_CURRENT_BUILD_DIR@,%{_prefix},' \
		config/cmake/${f}.in > $RPM_BUILD_ROOT%{_libdir}/cmake/hdf5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	fortran -p /sbin/ldconfig
%postun	fortran -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.txt release_docs/{HISTORY*.txt,RELEASE.txt}
%attr(755,root,root) %{_libdir}/libhdf5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5.so.103
%attr(755,root,root) %{_libdir}/libhdf5_hl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl.so.100
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
%{_includedir}/H5DOpublic.h
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
%{_includedir}/H5FDmulti.h
%{_includedir}/H5FDpublic.h
%{_includedir}/H5FDsec2.h
%{_includedir}/H5FDstdio.h
%{_includedir}/H5FDwindows.h
%{_includedir}/H5Fpublic.h
%{_includedir}/H5Gpublic.h
%{_includedir}/H5IMpublic.h
%{_includedir}/H5Include.h
%{_includedir}/H5Ipublic.h
%{_includedir}/H5LDpublic.h
%{_includedir}/H5LTpublic.h
%{_includedir}/H5Lpublic.h
%{_includedir}/H5MMpublic.h
%{_includedir}/H5Opublic.h
%{_includedir}/H5PTpublic.h
%{_includedir}/H5Ppublic.h
%{_includedir}/H5PLextern.h
%{_includedir}/H5PLpublic.h
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

%{_libdir}/cmake/hdf5
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/README
%{_examplesdir}/%{name}-%{version}/run-all-ex.sh
%{_examplesdir}/%{name}-%{version}/c
%dir %{_examplesdir}/%{name}-%{version}/hl
%{_examplesdir}/%{name}-%{version}/hl/run-hl-ex.sh
%{_examplesdir}/%{name}-%{version}/hl/c

%files static
%defattr(644,root,root,755)
%{_libdir}/libhdf5.a
%{_libdir}/libhdf5_hl.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_cpp.so.103
%attr(755,root,root) %{_libdir}/libhdf5_hl_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl_cpp.so.100

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
%{_includedir}/H5DaccProp.h
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
%{_includedir}/H5LaccProp.h
%{_includedir}/H5LcreatProp.h
%{_includedir}/H5Library.h
%{_includedir}/H5Location.h
%{_includedir}/H5Object.h
%{_includedir}/H5OcreatProp.h
%{_includedir}/H5PacketTable.h
%{_includedir}/H5PredType.h
%{_includedir}/H5PropList.h
%{_includedir}/H5StrType.h
%{_includedir}/H5VarLenType.h
%{_examplesdir}/%{name}-%{version}/c++
%{_examplesdir}/%{name}-%{version}/hl/c++

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libhdf5_cpp.a
%{_libdir}/libhdf5_hl_cpp.a

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_fortran.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_fortran.so.102
%attr(755,root,root) %{_libdir}/libhdf5hl_fortran.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5hl_fortran.so.100

%files fortran-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h5fc
%attr(755,root,root) %{_libdir}/libhdf5_fortran.so
%attr(755,root,root) %{_libdir}/libhdf5_hl_fortran.so
%attr(755,root,root) %{_libdir}/libhdf5hl_fortran.so
%{_libdir}/libhdf5_fortran.la
%{_libdir}/libhdf5hl_fortran.la
%{_includedir}/H5f90i.h
%{_includedir}/H5f90i_gen.h
%{_includedir}/h5_gen.mod
%{_includedir}/h5a.mod
%{_includedir}/h5d.mod
%{_includedir}/h5ds.mod
%{_includedir}/h5e.mod
%{_includedir}/h5f.mod
%{_includedir}/h5fortkit.mod
%{_includedir}/h5fortran_types.mod
%{_includedir}/h5g.mod
%{_includedir}/h5global.mod
%{_includedir}/h5i.mod
%{_includedir}/h5im.mod
%{_includedir}/h5l.mod
%{_includedir}/h5lib.mod
%{_includedir}/h5lt.mod
%{_includedir}/h5lt_const.mod
%{_includedir}/h5o.mod
%{_includedir}/h5p.mod
%{_includedir}/h5r.mod
%{_includedir}/h5s.mod
%{_includedir}/h5t.mod
%{_includedir}/h5tb.mod
%{_includedir}/h5tb_const.mod
%{_includedir}/h5z.mod
%{_includedir}/hdf5.mod

%files fortran-static
%defattr(644,root,root,755)
%{_libdir}/libhdf5_fortran.a
%{_libdir}/libhdf5_hl_fortran.a
%{_libdir}/libhdf5hl_fortran.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gif2h5
%attr(755,root,root) %{_bindir}/h52gif
%attr(755,root,root) %{_bindir}/h5clear
%attr(755,root,root) %{_bindir}/h5copy
%attr(755,root,root) %{_bindir}/h5debug
%attr(755,root,root) %{_bindir}/h5diff
%attr(755,root,root) %{_bindir}/h5dump
%attr(755,root,root) %{_bindir}/h5format_convert
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
%attr(755,root,root) %{_bindir}/h5watch
