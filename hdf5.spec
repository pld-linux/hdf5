Summary:	Hierarchical Data Format 5 library
Summary(pl):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
%define	_ver	1.4.2
%define _patch	patch1
Version:	%{_ver}%{_patch}
Release:	2
Group:		Libraries
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/%{name}-%{_ver}-%{_patch}/src/%{name}-%{_ver}-%{_patch}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-hdf4link.patch
Patch2:		%{name}-acfix.patch
URL:		http://hdf.ncsa.uiuc.edu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	hdf-devel >= 4.0
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
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
Requires:	%{name} = %{version}

%description devel
Header files for HDF5 library and HDF5 documentation.

%description devel -l pl
Pliki nag³ówkowe biblioteki HDF5 oraz dokumentacja HDF5.

%package static
Summary:	HDF5 static library
Summary(pl):	Statyczna biblioteka HDF5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of HDF5 library.

%description static -l pl
Statyczna wersja biblioteki HDF5.

%package progs
Summary:	HDF5 utilities
Summary(pl):	Narzêdzia do plików HDF5
Group:		Applications/File
Requires:	%{name} = %{version}

%description progs
Utilities to convert from/to HDF5 format.

%description progs -l pl
Narzêdzia do konwersji z i to formatu HDF5.

%package hdf4
Summary:	HDF 4.x to/from HDF5 conversion tools
Summary(pl):	Narzêdzia do konwersji pomiêdzy HDF 4.x i HDF5
Group:		Applications/File
Requires:	%{name} = %{version}

%description hdf4
Utilities to convert files from HDF 4.x to HDF5 or from HDF5 to HDF
4.x format.

%description hdf4 -l pl
Narzêdzia do konwersji plików z formatu HDF 4.x do HDF5 oraz z HDF5 do
HDF 4.x.

%prep
%setup -q -n %{name}-%{_ver}-%{_patch}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
(cd c++ ; aclocal ; autoconf)
%configure \
	--enable-cxx \
	--with-hdf4=/usr/include/hdf

#	--enable-fortran  - requires Fortran90 compiler

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	bindir=$RPM_BUILD_ROOT%{_bindir}

find doc -name Dependencies -o -name Makefile\* | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.txt release_docs/{HISTORY.txt,RELEASE.txt}
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gif2h5
%attr(755,root,root) %{_bindir}/h52gif
%attr(755,root,root) %{_bindir}/h5debug
%attr(755,root,root) %{_bindir}/h5dump
%attr(755,root,root) %{_bindir}/h5import
%attr(755,root,root) %{_bindir}/h5ls
%attr(755,root,root) %{_bindir}/h5repart

%files hdf4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/h4toh5
%attr(755,root,root) %{_bindir}/h5toh4
