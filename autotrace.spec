Summary:	AutoTrace - convert bitmap to vector graphics
Summary(pl):	AutoTrace - konwerter grafiki rastrowej do wektorowej
Name:		autotrace
Version:	0.31.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/autotrace/%{name}-%{version}.tar.gz
# Source0-md5:	54eabbb38d2076ded6d271e1ee4d0783
Patch0:		%{name}-link.patch
Patch1:		%{name}-aclocal.patch
URL:		http://autotrace.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 5.2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	ming-devel
BuildRequires:	pstoedit >= 3.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoTrace is a utility that converts bitmap to vector graphics. It can
import p[nbgp]m, bmp, tga, png (and many more through ImageMagick)
files and write to emf, eps, ai, er, fig, svg, sk and swf files.

%description -l pl
AutoTrace jest narzêdziem do konwersji grafiki rastrowej na wektorow±.
Mo¿e wczytywaæ pliki p[nbgp]m, bmp, tga, png (i wiele innych przez
ImageMagick, a zapisywaæ w formacie emf, eps, ai, er, fig, svg, sk
oraz swf.

%package devel
Summary:	AutoTrace library development files
Summary(pl):	Pliki dla programistów u¿ywaj±cych biblioteki AutoTrace
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
AutoTrace library header files.

%description devel -l pl
Pliki nag³ówkowe do biblioteki AutoTrace.

%package static
Summary:	AutoTrace static library
Summary(pl):	Biblioteka statyczna AutoTrace
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
AutoTrace static library.

%description static -l pl
Biblioteka statyczna AutoTrace.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/autotrace
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%attr(755,root,root) %{_bindir}/autotrace-config
%{_includedir}/autotrace
%{_aclocaldir}/autotrace.m4
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
