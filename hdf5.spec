# TODO:
# - build with MPICH
# - enable Stream VFD support
# - check missing file
Summary:	Hierarchical Data Format 5 library
Summary(pl):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
Version:	1.6.3
Release:	0.1
Group:		Libraries
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/%{name}-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	2bdca6886c6832013580af246c9bc4a0
Patch0:		%{name}-config.patch
URL:		http://hdf.ncsa.uiuc.edu/HDF5/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	zlib-devel >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%description -l pl
HDF5 jest ca³kowicie nowym produktem Hierarchiczego Formatu Danych,
sk³adaj±cym siê ze specyfikacji formatu danych oraz obs³uguj±cej go
biblioteki. HDF5 zosta³ zaprojektowany aby pozbyæ siê ograniczeñ
poprzedniego HDF oraz ¿eby zaspokoiæ bie¿±ce i przysz³e potrzeby
wspó³czesnych systemów i aplikacji.

%package devel
Summary:	HDF5 library development package
Summary(pl):	Pliki nag³ówkowe biblioteki HDF5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel
Requires:	zlib-devel

%description devel
Header files for HDF5 library and HDF5 documentation.

%description devel -l pl
Pliki nag³ówkowe biblioteki HDF5 oraz dokumentacja HDF5.

%package static
Summary:	HDF5 static library
Summary(pl):	Statyczna biblioteka HDF5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of HDF5 library.

%description static -l pl
Statyczna wersja biblioteki HDF5.

%package progs
Summary:	HDF5 utilities
Summary(pl):	Narzêdzia do plików HDF5
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description progs
Utilities to convert from/to HDF5 format.

%description progs -l pl
Narzêdzia do konwersji z i to formatu HDF5.

%prep
%setup -q
%patch0 -p1

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
	--with-ssl

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
#check this
#%{_libdir}/libhdf5.settings

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
