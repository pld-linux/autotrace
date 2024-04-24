Summary:	AutoTrace - convert bitmap to vector graphics
Summary(pl.UTF-8):	AutoTrace - konwerter grafiki rastrowej do wektorowej
Name:		autotrace
Version:	0.31.10
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
#Source0Download: https://github.com/autotrace/autotrace/releases
Source0:	https://github.com/autotrace/autotrace/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3078d2530a65f28c31c89974671ef02a
Patch0:		%{name}-link.patch
URL:		https://autotrace.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:7.0.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.22.5
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libtool >= 2:2
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	ming-devel
BuildRequires:	pkgconfig
BuildRequires:	pstoedit-devel >= 3.33-4
BuildRequires:	sed >= 4.0
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
Requires:	ImageMagick-devel >= 1:7.0.1
Requires:	glib2-devel >= 2.0
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

%{__sed} -i -e 's,po/Makefile.in ,,' configure.ac

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libautotrace.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md THANKS TODO
%attr(755,root,root) %{_bindir}/autotrace
%attr(755,root,root) %{_libdir}/libautotrace.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libautotrace.so.3
%{_mandir}/man1/autotrace.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libautotrace.so
%{_includedir}/autotrace
%{_pkgconfigdir}/autotrace.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libautotrace.a
