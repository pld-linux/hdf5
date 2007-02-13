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
Version:	1.6.5
Release:	2
Group:		Libraries
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/%{name}-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	67187b3253b89f1f41756b7fd4396ecf
Patch0:		%{name}-config.patch
Patch1:		%{name}-sig.patch
URL:		http://hdf.ncsa.uiuc.edu/HDF5/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openssl-devel >= 0.9.7d
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
Requires:	openssl-devel
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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd c++
%{__aclocal}
%{__autoconf}
cd ..
%configure \
	--enable-cxx \
	--enable-linux-lfs \
	--enable-threadsafe \
	--enable-production \
	--with-pthread \
	--with-ssl \
	%{?with_szip:--with-szlib}

#	--enable-fortran  - requires Fortran90 compiler

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	docdir=$RPM_BUILD_ROOT%{_docdir}

find doc -name Dependencies -o -name Makefile\* | xargs rm -f

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv -f $RPM_BUILD_ROOT%{_docdir}/hdf5/examples/{c,c++} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.txt release_docs/{HISTORY.txt,RELEASE.txt}
%attr(755,root,root) %{_libdir}/libhdf5.so.*.*.*
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so.*.*.*
%attr(755,root,root) %{_libdir}/libhdf5_hl.so.*.*.*
# used to show configuration at runtime
%{_libdir}/libhdf5.settings
%{_libdir}/libhdf5_cpp.settings

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/libhdf5.so
%attr(755,root,root) %{_libdir}/libhdf5_cpp.so
%attr(755,root,root) %{_libdir}/libhdf5_hl.so
%{_libdir}/libhdf5.la
%{_libdir}/libhdf5_cpp.la
%{_libdir}/libhdf5_hl.la
%{_includedir}/*.h
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libhdf5.a
%{_libdir}/libhdf5_cpp.a
%{_libdir}/libhdf5_hl.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
