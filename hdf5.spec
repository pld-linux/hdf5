Summary:	Hierarchical Data Format 5 library
Summary(pl):	Biblioteka HDF5 (Hierarchical Data Format 5)
Name:		hdf5
%define	_ver	1.4.2
%define _patch	patch1
Version:	%{_ver}%{_patch}
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
License:	Nearly BSD, but changed sources must be marked
Source0:	ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/%{name}-%{version}/src/%{name}-%{_ver}-%{_patch}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://hdf.ncsa.uiuc.edu/
BuildRequires:	zlib-devel >= 1.1.3
BuildRequires:	openssl-devel
BuildRequires:	libstdc++-devel
#BuildRequires:	libjpeg-devel >= 6b
#BuildRequires:	hdf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%description -l pl
HDF5 jest ca≥kowicie nowym produktem Hierarchiczego Formatu Danych,
sk≥adaj±cym siÍ ze specyfikacji formatu danych oraz obs≥uguj±cej go
biblioteki. HDF5 zosta≥ zaprojektowany aby pozbyÊ siÍ ograniczeÒ
poprzedniego HDF oraz øeby zaspokoiÊ bieø±ce i przysz≥e potrzeby
wspÛ≥czesnych systemÛw i aplikacji.

%package devel
Summary:	HDF5 library development package
Summary(pl):	Pliki nag≥Ûwkowe biblioteki HDF5
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files for HDF5 library.

%description devel -l pl
Pliki nag≥Ûwkowe biblioteki HDF5.

%package static
Summary:	HDF5 static library
Summary(pl):	Statyczna biblioteka HDF5
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static version of HDF5 library.

%description static -l pl
Statyczna wersja biblioteki HDF5.

%package progs
Summary:	HDF5 utilities
Summary(pl):	NarzÍdzia do plikÛw HDF5
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Requires:	%{name} = %{version}

%description progs
Utilities to convert from/to HDF5 format.

%description progs -l pl
NarzÍdzia do konwersji z i to formatu HDF5.

%prep
%setup -q -n %{name}-%{_ver}-%{_patch}
%patch -p1

%build
%configure2_13 \
	--enable-cxx

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

gzip -9nf COPYING README.txt release_docs/{HISTORY.txt,RELEASE.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz release_notes/*.gz doc/html
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
