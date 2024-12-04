# TODO:
# - finish (optional) MPI support (1.8.14: fails on mpi_file_open check)
# - check missing file
#
# Conditional build:
%bcond_with	hdfs		# HDFS driver (requires libhdfs, hdfs.h)
%bcond_without	java		# Java wrappers
%bcond_without	s3		# R/O S3 driver
%bcond_without	szip		# SZIP compression support
%bcond_with	mpi		# parallel version of library using MPI
#
Summary:	Hierarchical Data Format 5 library
Summary(pl.UTF-8):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
Version:	1.14.5
Release:	1
License:	Nearly BSD, but changed sources must be marked
Group:		Libraries
Source0:	https://support.hdfgroup.org/releases/hdf5/v1_14/v1_14_5/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	600d29af6ccb7f1e3401560e1422ba5e
Patch0:		ix86-short-real.patch
Patch1:		%{name}-cmake.patch
URL:		https://www.hdfgroup.org/solutions/hdf5/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
%{?with_s3:BuildRequires:	curl-devel}
BuildRequires:	gcc-fortran >= 6:4.2
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
%{?with_mpi:BuildRequires:	mpi-devel}
%{?with_s3:BuildRequires:	openssl-devel}
%{?with_szip:BuildRequires:	szip-devel >= 2.0}
BuildRequires:	zlib-devel >= 1.1.3
Obsoletes:	hdf5_hl < 5180
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
%{?with_s3:Requires:	curl-devel}
%{?with_s3:Requires:	openssl-devel}
%{?with_szip:Requires:	szip-devel >= 2.0}
Requires:	zlib-devel
Obsoletes:	hdf5_hl-devel < 5180
Obsoletes:	hdf5_hl-tutor < 5180

%description devel
Header files for HDF5 library and HDF5 documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HDF5 oraz dokumentacja HDF5.

%package static
Summary:	HDF5 static library
Summary(pl.UTF-8):	Statyczna biblioteka HDF5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	hdf5_hl-static < 5180

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
Requires:	gcc-fortran >= 6:4.2

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

%package -n java-hdf5
Summary:	Java HDF5 Interface (JHI5)
Summary(pl.UTF-8):	Interfejs HDF5 do Javy (JHI5)
# to replace java-hdf5 [0:]2.11/3.3.1 from hdf-java.spec
Epoch:		1
Group:		Libraries/Java
URL:		http://portal.hdfgroup.org/display/HDFVIEW/JHI5+Design+Notes
Requires:	%{name} = %{version}-%{release}
Requires:	java-slf4j >= 1.7.25
Obsoletes:	java-hdf5-javadoc < 1.14.5

%description -n java-hdf5
The Java Native Interface to the standard HDF5 library.

%description -n java-hdf5 -l pl.UTF-8
Natywny interfejs Javy (JNI) do biblioteki standardowej HDF5.

%prep
%setup -q
%ifarch %{ix86}
%patch -P 0 -p1
%endif
%patch -P 1 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+bash(\s|$),#!/bin/bash\\1,' \
	utils/subfiling_vfd/h5fuse.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--docdir=%{_docdir} \
	--disable-silent-rules \
	--enable-cxx \
	--enable-direct-vfd \
	--enable-fortran \
	%{?with_java:--enable-java} \
	%{?with_mpi:--enable-parallel --enable-unsupported} \
	%{?with_s3:--enable-ros3-vfd} \
	--enable-shared \
	%{?with_hdfs:--with-libhdfs=%{_includedir},%{_libdir}} \
	--with-pthread \
	%{?with_szip:--with-szlib}

#	--enable-threadsafe is unspported with cxx/fortran/java/hl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install-recursive \
	DESTDIR=$RPM_BUILD_ROOT \
	hdf5_javadir=%{_javadir}

%if %{with java}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhdf5_java.la
ln -sf jarhdf5-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jarhdf5.jar
%endif

install -d $RPM_BUILD_ROOT%{_libdir}/cmake/hdf5
vmajor=$(sed -ne 's/^#define H5_VERS_MAJOR\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vminor=$(sed -ne 's/^#define H5_VERS_MINOR\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vrel=$(sed -ne 's/^#define H5_VERS_RELEASE\s*\([0-9]\+\).*/\1/p' src/H5public.h)
vsubr=$(sed -ne 's/^#define H5_VERS_SUBRELEASE\s*"\?\([^" \t]\+\)"\?.*/\1/p' src/H5public.h)
for f in hdf5-config-version.cmake hdf5-config.cmake hdf5-targets.cmake hdf5-targets-noconfig.cmake ; do
	sed -e 's,@HDF5_PACKAGE@,hdf5,g' \
	    -e 's,@HDF_PACKAGE_EXT@,,' \
	    -e "s,@HDF5_VERSION_STRING@,%{version}," \
	    -e "s,@HDF5_VERSION_MAJOR@,1.10," \
	    -e "s,@HDF5_VERSION_MINOR@,$vrel," \
	    -e "s,@H5_VERS_MAJOR@,$vmajor," \
	    -e "s,@H5_VERS_MINOR@,$vminor," \
	    -e "s,@H5_VERS_RELEASE@,$vrel," \
	    -e "s,@H5_VERS_SUBRELEASE@,$vsubr," \
	    -e 's,@HDF5_ENABLE_PARALLEL@,OFF,' \
	    -e 's,@HDF5_BUILD_FORTRAN@,ON,' \
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
	    -e 's,@PACKAGE_SHARE_INSTALL_DIR@,%{_libdir}/cmake/hdf5,' \
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

%post	-n java-hdf5 -p /sbin/ldconfig
%postun	-n java-hdf5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md release_docs/{HISTORY*.txt,RELEASE.txt}
%attr(755,root,root) %{_libdir}/libhdf5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5.so.310
%attr(755,root,root) %{_libdir}/libhdf5_hl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl.so.310
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
%{_includedir}/H5Dpublic.h
%{_includedir}/H5DSpublic.h
%{_includedir}/H5Epubgen.h
%{_includedir}/H5Epublic.h
%{_includedir}/H5ESdevelop.h
%{_includedir}/H5ESpublic.h
%{_includedir}/H5FDcore.h
%{_includedir}/H5FDdevelop.h
%{_includedir}/H5FDdirect.h
%{_includedir}/H5FDfamily.h
%{_includedir}/H5FDhdfs.h
%{_includedir}/H5FDioc.h
%{_includedir}/H5FDlog.h
%{_includedir}/H5FDmirror.h
%{_includedir}/H5FDmpi.h
%{_includedir}/H5FDmpio.h
%{_includedir}/H5FDmulti.h
%{_includedir}/H5FDonion.h
%{_includedir}/H5FDpublic.h
%{_includedir}/H5FDros3.h
%{_includedir}/H5FDsec2.h
%{_includedir}/H5FDsplitter.h
%{_includedir}/H5FDstdio.h
%{_includedir}/H5FDsubfiling.h
%{_includedir}/H5FDwindows.h
%{_includedir}/H5Fpublic.h
%{_includedir}/H5Gpublic.h
%{_includedir}/H5Idevelop.h
%{_includedir}/H5IMpublic.h
%{_includedir}/H5Include.h
%{_includedir}/H5Ipublic.h
%{_includedir}/H5Ldevelop.h
%{_includedir}/H5LDpublic.h
%{_includedir}/H5Lpublic.h
%{_includedir}/H5LTpublic.h
%{_includedir}/H5MMpublic.h
%{_includedir}/H5Mpublic.h
%{_includedir}/H5Opublic.h
%{_includedir}/H5PLextern.h
%{_includedir}/H5PLpublic.h
%{_includedir}/H5Ppublic.h
%{_includedir}/H5PTpublic.h
%{_includedir}/H5Rpublic.h
%{_includedir}/H5Spublic.h
%{_includedir}/H5TBpublic.h
%{_includedir}/H5Tdevelop.h
%{_includedir}/H5Tpublic.h
%{_includedir}/H5TSdevelop.h
%{_includedir}/H5VLconnector.h
%{_includedir}/H5VLconnector_passthru.h
%{_includedir}/H5VLnative.h
%{_includedir}/H5VLpassthru.h
%{_includedir}/H5VLpublic.h
%{_includedir}/H5Zdevelop.h
%{_includedir}/H5Zpublic.h
%{_includedir}/H5api_adpt.h
%{_includedir}/H5overflow.h
%{_includedir}/H5pubconf.h
%{_includedir}/H5public.h
%{_includedir}/H5version.h
%{_includedir}/hdf5.h
%{_includedir}/hdf5_hl.h

%{_libdir}/cmake/hdf5

%files static
%defattr(644,root,root,755)
%{_libdir}/libhdf5.a
%{_libdir}/libhdf5_hl.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_cpp.so.310
%attr(755,root,root) %{_libdir}/libhdf5_hl_cpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_hl_cpp.so.310

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

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libhdf5_cpp.a
%{_libdir}/libhdf5_hl_cpp.a

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_fortran.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5_fortran.so.310
%attr(755,root,root) %{_libdir}/libhdf5hl_fortran.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhdf5hl_fortran.so.310

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
%{_includedir}/H5config_f.inc
%{_includedir}/*.mod

%files fortran-static
%defattr(644,root,root,755)
%{_libdir}/libhdf5_fortran.a
%{_libdir}/libhdf5_hl_fortran.a
%{_libdir}/libhdf5hl_fortran.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h5clear
%attr(755,root,root) %{_bindir}/h5copy
%attr(755,root,root) %{_bindir}/h5debug
%attr(755,root,root) %{_bindir}/h5delete
%attr(755,root,root) %{_bindir}/h5diff
%attr(755,root,root) %{_bindir}/h5dump
%attr(755,root,root) %{_bindir}/h5format_convert
%attr(755,root,root) %{_bindir}/h5fuse
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

%if %{with java}
%files -n java-hdf5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhdf5_java.so
%{_javadir}/jarhdf5-%{version}.jar
%{_javadir}/jarhdf5.jar
%endif
