Summary:	AutoTrace - convert bitmap to vector graphics
Summary(pl):	AutoTrace - konwersja grafiki rastrowej do wektorowej
Name:		autotrace
Version:	0.27a
Release:	1
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/autotrace/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-magick.patch
URL:		http://autotrace.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libpng-devel >= 1.0.6
BuildRequires:	ming-devel
BuildRequires:	ImageMagick-devel >= 5.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoTrace is a utility that converts bitmap to vector graphics. It can
import p[nbgp]m, bmp, tga, png (and many more through ImageMagick)
files and write to emf, eps, ai, er, fig, svg, sk and swf files.

%description -l pl
AutoTrace jest narzÍdziem do konwersji grafiki rastrowej na wektorow±.
Moøe wczytywaÊ pliki p[nbgp]m, bmp, tga, png (i wiele innych przez
ImageMagick, a zapisywaÊ w formacie emf, eps, ai, er, fig, svg, sk
oraz swf.

%package devel
Summary:	AutoTrace library development files
Summary(pl):	Pliki dla programistÛw uøywaj±cych biblioteki AutoTrace
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
AutoTrace library header files.

%description devel -l pl
Pliki nag≥Ûwkowe do biblioteki AutoTrace.

%package static
Summary:	AutoTrace static library
Summary(pl):	Biblioteka statyczna AutoTrace
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
AutoTrace static library.

%description static -l pl
Biblioteka statyczna AutoTrace.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/autotrace
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_bindir}/autotrace-config
%{_includedir}/autotrace
%{_aclocaldir}/autotrace.m4

%files static
%defattr(644,root,root,755)
