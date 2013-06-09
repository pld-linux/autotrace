Summary:	AutoTrace - convert bitmap to vector graphics
Summary(pl.UTF-8):	AutoTrace - konwerter grafiki rastrowej do wektorowej
Name:		autotrace
Version:	0.31.1
Release:	10
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/autotrace/%{name}-%{version}.tar.gz
# Source0-md5:	54eabbb38d2076ded6d271e1ee4d0783
Patch0:		%{name}-link.patch
Patch1:		%{name}-aclocal.patch
Patch2:		%{name}-am18.patch
Patch3:		%{name}-magick6.patch
Patch4:		%{name}-am.patch
Patch5:		%{name}-libpng.patch
URL:		http://autotrace.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:6.2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	ming-devel
BuildRequires:	pstoedit-devel >= 3.33-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoTrace is a utility that converts bitmap to vector graphics. It can
import p[nbgp]m, bmp, tga, png (and many more through ImageMagick)
files and write to emf, eps, ai, er, fig, svg, sk and swf files.

%description -l pl.UTF-8
AutoTrace jest narzędziem do konwersji grafiki rastrowej na wektorową.
Może wczytywać pliki p[nbgp]m, bmp, tga, png (i wiele innych przez
ImageMagick, a zapisywać w formacie emf, eps, ai, er, fig, svg, sk
oraz swf.

%package devel
Summary:	AutoTrace library development files
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki AutoTrace
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick-devel >= 1:6.2.4.0
Requires:	libpng-devel >= 1.0.6
Requires:	ming-devel
Requires:	pstoedit-devel >= 3.33-4

%description devel
AutoTrace library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki AutoTrace.

%package static
Summary:	AutoTrace static library
Summary(pl.UTF-8):	Biblioteka statyczna AutoTrace
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
AutoTrace static library.

%description static -l pl.UTF-8
Biblioteka statyczna AutoTrace.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/autotrace
%attr(755,root,root) %{_libdir}/libautotrace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libautotrace.so.3
%{_mandir}/man1/autotrace.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/autotrace-config
%attr(755,root,root) %{_libdir}/libautotrace.so
%{_libdir}/libautotrace.la
%{_includedir}/autotrace
%{_aclocaldir}/autotrace.m4
%{_pkgconfigdir}/autotrace.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libautotrace.a
