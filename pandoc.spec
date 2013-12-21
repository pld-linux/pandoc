#
# Conditional build:
%bcond_without	prof	# profiling library
#
Summary:	Conversion between markup formats
Summary(pl.UTF-8):	Konwersja między różnymi formatami znaczników
Name:		pandoc
Version:	1.12.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
#Source0Download: http://code.google.com/p/pandoc/downloads/list
Source0:	http://pandoc.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	aaf8a1c343d05b122aecdbbae66800b4
Patch0:		%{name}-deps.patch
URL:		http://johnmacfarlane.net/pandoc/
BuildRequires:	alex
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-HTTP >= 4000.0.5
BuildRequires:	ghc-HTTP < 4000.3
BuildRequires:	ghc-aeson >= 0.6
BuildRequires:	ghc-aeson < 0.7
BuildRequires:	ghc-array >= 0.3
BuildRequires:	ghc-array < 0.5
BuildRequires:	ghc-attoparsec >= 0.10
BuildRequires:	ghc-attoparsec < 0.11
BuildRequires:	ghc-base >= 4.2
BuildRequires:	ghc-base < 5
BuildRequires:	ghc-base64-bytestring >= 0.1
BuildRequires:	ghc-base64-bytestring < 1.1
BuildRequires:	ghc-blaze-html >= 0.5
BuildRequires:	ghc-blaze-html < 0.7
BuildRequires:	ghc-blaze-markup >= 0.5.1
BuildRequires:	ghc-blaze-markup < 0.6
BuildRequires:	ghc-bytestring >= 0.9
BuildRequires:	ghc-bytestring < 0.11
BuildRequires:	ghc-containers >= 0.1
BuildRequires:	ghc-containers < 0.6
BuildRequires:	ghc-data-default >= 0.4
BuildRequires:	ghc-data-default < 0.6
BuildRequires:	ghc-directory >= 1
BuildRequires:	ghc-directory < 1.3
BuildRequires:	ghc-extensible-exceptions >= 0.1
BuildRequires:	ghc-extensible-exceptions < 0.2
BuildRequires:	ghc-filepath >= 1.1
BuildRequires:	ghc-filepath < 1.4
BuildRequires:	ghc-highlighting-kate >= 0.5.5
BuildRequires:	ghc-highlighting-kate < 0.6
BuildRequires:	ghc-hslua >= 0.3
BuildRequires:	ghc-hslua < 0.4
BuildRequires:	ghc-mtl >= 1.1
BuildRequires:	ghc-mtl < 2.2
BuildRequires:	ghc-network >= 2
BuildRequires:	ghc-network < 2.5
BuildRequires:	ghc-old-locale >= 1
BuildRequires:	ghc-old-locale < 1.1
BuildRequires:	ghc-old-time >= 1.0
BuildRequires:	ghc-old-time < 1.2
BuildRequires:	ghc-pandoc-types >= 1.12.3
BuildRequires:	ghc-pandoc-types < 1.13
BuildRequires:	ghc-parsec >= 3.1
BuildRequires:	ghc-parsec < 3.2
BuildRequires:	ghc-process >= 1
BuildRequires:	ghc-process < 1.2
BuildRequires:	ghc-random >= 1
BuildRequires:	ghc-random < 1.1
BuildRequires:	ghc-syb >= 0.1
BuildRequires:	ghc-syb < 0.5
BuildRequires:	ghc-tagsoup >= 0.12.5
BuildRequires:	ghc-tagsoup < 0.14
BuildRequires:	ghc-temporary >= 1.1
BuildRequires:	ghc-temporary < 1.2
BuildRequires:	ghc-texmath >= 0.6.5.2
BuildRequires:	ghc-texmath < 0.7
BuildRequires:	ghc-text >= 0.11
BuildRequires:	ghc-text < 1.1
BuildRequires:	ghc-time >= 1.2
BuildRequires:	ghc-time < 1.5
BuildRequires:	ghc-unordered-containers >= 0.2
BuildRequires:	ghc-unordered-containers < 0.3
BuildRequires:	ghc-vector >= 0.10
BuildRequires:	ghc-vector < 0.11
BuildRequires:	ghc-xml >= 1.3.12
BuildRequires:	ghc-xml < 1.4
BuildRequires:	ghc-yaml >= 0.8.3
BuildRequires:	ghc-yaml < 0.9
BuildRequires:	ghc-zip-archive >= 0.1.3.3
BuildRequires:	ghc-zip-archive < 0.3
BuildRequires:	ghc-zlib >= 0.5
BuildRequires:	ghc-zlib < 0.6
%if %{with prof}
BuildRequires:	ghc-prof >= 6.12.3
BuildRequires:	ghc-HTTP-prof >= 4000.0.5
BuildRequires:	ghc-HTTP-prof < 4000.3
BuildRequires:	ghc-aeson-prof >= 0.6
BuildRequires:	ghc-aeson-prof < 0.7
BuildRequires:	ghc-array-prof >= 0.3
BuildRequires:	ghc-array-prof < 0.5
BuildRequires:	ghc-attoparsec-prof >= 0.10
BuildRequires:	ghc-attoparsec-prof < 0.11
BuildRequires:	ghc-base-prof >= 4.2
BuildRequires:	ghc-base-prof < 5
BuildRequires:	ghc-base64-bytestring-prof >= 0.1
BuildRequires:	ghc-base64-bytestring-prof < 1.1
BuildRequires:	ghc-blaze-html-prof >= 0.5
BuildRequires:	ghc-blaze-html-prof < 0.7
BuildRequires:	ghc-blaze-markup-prof >= 0.5.1
BuildRequires:	ghc-blaze-markup-prof < 0.6
BuildRequires:	ghc-bytestring-prof >= 0.9
BuildRequires:	ghc-bytestring-prof < 0.11
BuildRequires:	ghc-containers-prof >= 0.1
BuildRequires:	ghc-containers-prof < 0.6
BuildRequires:	ghc-data-default-prof >= 0.4
BuildRequires:	ghc-data-default-prof < 0.6
BuildRequires:	ghc-directory-prof >= 1
BuildRequires:	ghc-directory-prof < 1.3
BuildRequires:	ghc-extensible-exceptions-prof >= 0.1
BuildRequires:	ghc-extensible-exceptions-prof < 0.2
BuildRequires:	ghc-filepath-prof >= 1.1
BuildRequires:	ghc-filepath-prof < 1.4
BuildRequires:	ghc-highlighting-kate-prof >= 0.5.5
BuildRequires:	ghc-highlighting-kate-prof < 0.6
BuildRequires:	ghc-hslua-prof >= 0.3
BuildRequires:	ghc-hslua-prof < 0.4
BuildRequires:	ghc-mtl-prof >= 1.1
BuildRequires:	ghc-mtl-prof < 2.2
BuildRequires:	ghc-network-prof >= 2
BuildRequires:	ghc-network-prof < 2.5
BuildRequires:	ghc-old-locale-prof >= 1
BuildRequires:	ghc-old-locale-prof < 1.1
BuildRequires:	ghc-old-time-prof >= 1.0
BuildRequires:	ghc-old-time-prof < 1.2
BuildRequires:	ghc-pandoc-types-prof >= 1.12.3
BuildRequires:	ghc-pandoc-types-prof < 1.13
BuildRequires:	ghc-parsec-prof >= 3.1
BuildRequires:	ghc-parsec-prof < 3.2
BuildRequires:	ghc-process-prof >= 1
BuildRequires:	ghc-process-prof < 1.2
BuildRequires:	ghc-random-prof >= 1
BuildRequires:	ghc-random-prof < 1.1
BuildRequires:	ghc-syb-prof >= 0.1
BuildRequires:	ghc-syb-prof < 0.5
BuildRequires:	ghc-tagsoup-prof >= 0.12.5
BuildRequires:	ghc-tagsoup-prof < 0.14
BuildRequires:	ghc-temporary-prof >= 1.1
BuildRequires:	ghc-temporary-prof < 1.2
BuildRequires:	ghc-texmath-prof >= 0.6.5.2
BuildRequires:	ghc-texmath-prof < 0.7
BuildRequires:	ghc-text-prof >= 0.11
BuildRequires:	ghc-text-prof < 1.1
BuildRequires:	ghc-time-prof >= 1.2
BuildRequires:	ghc-time-prof < 1.5
BuildRequires:	ghc-unordered-containers-prof >= 0.2
BuildRequires:	ghc-unordered-containers-prof < 0.3
BuildRequires:	ghc-vector-prof >= 0.10
BuildRequires:	ghc-vector-prof < 0.11
BuildRequires:	ghc-xml-prof >= 1.3.12
BuildRequires:	ghc-xml-prof < 1.4
BuildRequires:	ghc-yaml-prof >= 0.8.3
BuildRequires:	ghc-yaml-prof < 0.9
BuildRequires:	ghc-zip-archive-prof >= 0.1.3.3
BuildRequires:	ghc-zip-archive-prof < 0.3
BuildRequires:	ghc-zlib-prof >= 0.5
BuildRequires:	ghc-zlib-prof < 0.6
%endif
BuildRequires:	happy
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) Textile, reStructuredText, HTML, LaTeX,
MediaWiki markup, Haddock markup, OPML, and DocBook; and it can write
plain text, markdown, reStructuredText, XHTML, HTML 5, LaTeX
(including beamer slide shows), ConTeXt, RTF, OPML, DocBook,
OpenDocument, ODT, Word docx, GNU Texinfo, MediaWiki markup, EPUB (v2
or v3), FictionBook2, Textile, groff man pages, Emacs Org-Mode,
AsciiDoc, and Slidy, Slideous, DZSlides, reveal.js or S5 HTML slide
shows. It can also produce PDF output on systems where LaTeX is
installed.

%description -l pl.UTF-8
Pandoc to biblioteka Haskella do konwersji tekstów z jednego formatu
znaczników do innych oraz narzędzie linii poleceń wykorzystujące tę
bibliotekę. Potrafi czytać format markdown oraz (podzbiory) formatów
Textile, reStructuredText, HTML, LaTeX, znaczniki MediaWiki, znaczniki
Haddock, OPML oraz DocBook. Potrafi zapisywać zwykły tekst, markdown,
reStructuredText, XHTML, HTML 5, LaTeX (wraz z pokazami slajdów dla
pakietu beamer), ConTeXt, RTF, OPML, DocBook, OpenDocument, ODT, Word
docx, GNU Texinfo, znaczniki MediaWiki, EPUB (w wersji 2 lub 3),
FictionBook2, Textile, strony man w formacie groff, Emacs Org-Mode,
AsciiDoc oraz pokazy slajdów HTML Slidy, Slideous, DZSlides, reveal.js
lub S5. Potrafi także tworzyć wyjście PDF na systemach z
zainstalowanym LaTeXem.

%package -n ghc-pandoc
Summary:	Conversion between markup formats
Summary(pl.UTF-8):	Konwersja między różnymi formatami znaczników
Group:		Development/Languages
Requires(post,postun):	/usr/bin/ghc-pkg
%requires_eq	ghc
Requires:	ghc-HTTP >= 4000.0.5
Requires:	ghc-HTTP < 4000.3
Requires:	ghc-aeson >= 0.6
Requires:	ghc-aeson < 0.7
Requires:	ghc-array >= 0.3
Requires:	ghc-array < 0.5
Requires:	ghc-attoparsec >= 0.10
Requires:	ghc-attoparsec < 0.11
Requires:	ghc-base >= 4.2
Requires:	ghc-base < 5
Requires:	ghc-base64-bytestring >= 0.1
Requires:	ghc-base64-bytestring < 1.1
Requires:	ghc-blaze-html >= 0.5
Requires:	ghc-blaze-html < 0.7
Requires:	ghc-blaze-markup >= 0.5.1
Requires:	ghc-blaze-markup < 0.6
Requires:	ghc-bytestring >= 0.9
Requires:	ghc-bytestring < 0.11
Requires:	ghc-containers >= 0.1
Requires:	ghc-containers < 0.6
Requires:	ghc-data-default >= 0.4
Requires:	ghc-data-default < 0.6
Requires:	ghc-directory >= 1
Requires:	ghc-directory < 1.3
Requires:	ghc-extensible-exceptions >= 0.1
Requires:	ghc-extensible-exceptions < 0.2
Requires:	ghc-filepath >= 1.1
Requires:	ghc-filepath < 1.4
Requires:	ghc-highlighting-kate >= 0.5.5
Requires:	ghc-highlighting-kate < 0.6
Requires:	ghc-hslua >= 0.3
Requires:	ghc-hslua < 0.4
Requires:	ghc-mtl >= 1.1
Requires:	ghc-mtl < 2.2
Requires:	ghc-network >= 2
Requires:	ghc-network < 2.5
Requires:	ghc-old-locale >= 1
Requires:	ghc-old-locale < 1.1
Requires:	ghc-old-time >= 1.0
Requires:	ghc-old-time < 1.2
Requires:	ghc-pandoc-types >= 1.12.3
Requires:	ghc-pandoc-types < 1.13
Requires:	ghc-parsec >= 3.1
Requires:	ghc-parsec < 3.2
Requires:	ghc-process >= 1
Requires:	ghc-process < 1.2
Requires:	ghc-random >= 1
Requires:	ghc-random < 1.1
Requires:	ghc-syb >= 0.1
Requires:	ghc-syb < 0.5
Requires:	ghc-tagsoup >= 0.12.5
Requires:	ghc-tagsoup < 0.14
Requires:	ghc-temporary >= 1.1
Requires:	ghc-temporary < 1.2
Requires:	ghc-texmath >= 0.6.5.2
Requires:	ghc-texmath < 0.7
Requires:	ghc-text >= 0.11
Requires:	ghc-text < 1.1
Requires:	ghc-time >= 1.2
Requires:	ghc-time < 1.5
Requires:	ghc-unordered-containers >= 0.2
Requires:	ghc-unordered-containers < 0.3
Requires:	ghc-vector >= 0.10
Requires:	ghc-vector < 0.11
Requires:	ghc-xml >= 1.3.12
Requires:	ghc-xml < 1.4
Requires:	ghc-yaml >= 0.8.3
Requires:	ghc-yaml < 0.9
Requires:	ghc-zip-archive >= 0.1.3.3
Requires:	ghc-zip-archive < 0.3
Requires:	ghc-zlib >= 0.5
Requires:	ghc-zlib < 0.6

%description -n ghc-pandoc
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) Textile, reStructuredText, HTML, LaTeX,
MediaWiki markup, Haddock markup, OPML, and DocBook; and it can write
plain text, markdown, reStructuredText, XHTML, HTML 5, LaTeX
(including beamer slide shows), ConTeXt, RTF, OPML, DocBook,
OpenDocument, ODT, Word docx, GNU Texinfo, MediaWiki markup, EPUB (v2
or v3), FictionBook2, Textile, groff man pages, Emacs Org-Mode,
AsciiDoc, and Slidy, Slideous, DZSlides, reveal.js or S5 HTML slide
shows. It can also produce PDF output on systems where LaTeX is
installed.

%description -n ghc-pandoc -l pl.UTF-8
Pandoc to biblioteka Haskella do konwersji tekstów z jednego formatu
znaczników do innych oraz narzędzie linii poleceń wykorzystujące tę
bibliotekę. Potrafi czytać format markdown oraz (podzbiory) formatów
Textile, reStructuredText, HTML, LaTeX, znaczniki MediaWiki, znaczniki
Haddock, OPML oraz DocBook. Potrafi zapisywać zwykły tekst, markdown,
reStructuredText, XHTML, HTML 5, LaTeX (wraz z pokazami slajdów dla
pakietu beamer), ConTeXt, RTF, OPML, DocBook, OpenDocument, ODT, Word
docx, GNU Texinfo, znaczniki MediaWiki, EPUB (w wersji 2 lub 3),
FictionBook2, Textile, strony man w formacie groff, Emacs Org-Mode,
AsciiDoc oraz pokazy slajdów HTML Slidy, Slideous, DZSlides, reveal.js
lub S5. Potrafi także tworzyć wyjście PDF na systemach z
zainstalowanym LaTeXem.

%package -n ghc-pandoc-prof
Summary:	Profiling %{name} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{name} dla GHC
Group:		Development/Libraries
Requires:	ghc-pandoc = %{version}-%{release}
Requires:	ghc-HTTP-prof >= 4000.0.5
Requires:	ghc-HTTP-prof < 4000.3
Requires:	ghc-aeson-prof >= 0.6
Requires:	ghc-aeson-prof < 0.7
Requires:	ghc-array-prof >= 0.3
Requires:	ghc-array-prof < 0.5
Requires:	ghc-attoparsec-prof >= 0.10
Requires:	ghc-attoparsec-prof < 0.11
Requires:	ghc-base-prof >= 4.2
Requires:	ghc-base-prof < 5
Requires:	ghc-base64-bytestring-prof >= 0.1
Requires:	ghc-base64-bytestring-prof < 1.1
Requires:	ghc-blaze-html-prof >= 0.5
Requires:	ghc-blaze-html-prof < 0.7
Requires:	ghc-blaze-markup-prof >= 0.5.1
Requires:	ghc-blaze-markup-prof < 0.6
Requires:	ghc-bytestring-prof >= 0.9
Requires:	ghc-bytestring-prof < 0.11
Requires:	ghc-containers-prof >= 0.1
Requires:	ghc-containers-prof < 0.6
Requires:	ghc-data-default-prof >= 0.4
Requires:	ghc-data-default-prof < 0.6
Requires:	ghc-directory-prof >= 1
Requires:	ghc-directory-prof < 1.3
Requires:	ghc-extensible-exceptions-prof >= 0.1
Requires:	ghc-extensible-exceptions-prof < 0.2
Requires:	ghc-filepath-prof >= 1.1
Requires:	ghc-filepath-prof < 1.4
Requires:	ghc-highlighting-kate-prof >= 0.5.5
Requires:	ghc-highlighting-kate-prof < 0.6
Requires:	ghc-hslua-prof >= 0.3
Requires:	ghc-hslua-prof < 0.4
Requires:	ghc-mtl-prof >= 1.1
Requires:	ghc-mtl-prof < 2.2
Requires:	ghc-network-prof >= 2
Requires:	ghc-network-prof < 2.5
Requires:	ghc-old-locale-prof >= 1
Requires:	ghc-old-locale-prof < 1.1
Requires:	ghc-old-time-prof >= 1.0
Requires:	ghc-old-time-prof < 1.2
Requires:	ghc-pandoc-types-prof >= 1.12.3
Requires:	ghc-pandoc-types-prof < 1.13
Requires:	ghc-parsec-prof >= 3.1
Requires:	ghc-parsec-prof < 3.2
Requires:	ghc-process-prof >= 1
Requires:	ghc-process-prof < 1.2
Requires:	ghc-random-prof >= 1
Requires:	ghc-random-prof < 1.1
Requires:	ghc-syb-prof >= 0.1
Requires:	ghc-syb-prof < 0.5
Requires:	ghc-tagsoup-prof >= 0.12.5
Requires:	ghc-tagsoup-prof < 0.14
Requires:	ghc-temporary-prof >= 1.1
Requires:	ghc-temporary-prof < 1.2
Requires:	ghc-texmath-prof >= 0.6.5.2
Requires:	ghc-texmath-prof < 0.7
Requires:	ghc-text-prof >= 0.11
Requires:	ghc-text-prof < 1.1
Requires:	ghc-time-prof >= 1.2
Requires:	ghc-time-prof < 1.5
Requires:	ghc-unordered-containers-prof >= 0.2
Requires:	ghc-unordered-containers-prof < 0.3
Requires:	ghc-vector-prof >= 0.10
Requires:	ghc-vector-prof < 0.11
Requires:	ghc-xml-prof >= 1.3.12
Requires:	ghc-xml-prof < 1.4
Requires:	ghc-yaml-prof >= 0.8.3
Requires:	ghc-yaml-prof < 0.9
Requires:	ghc-zip-archive-prof >= 0.1.3.3
Requires:	ghc-zip-archive-prof < 0.3
Requires:	ghc-zlib-prof >= 0.5
Requires:	ghc-zlib-prof < 0.6

%description -n ghc-pandoc-prof
Profiling %{name} library for GHC. Should be installed when GHC's
profiling subsystem is needed.

%description -n ghc-pandoc-prof -l pl.UTF-8
Biblioteka profilująca %{name} dla GHC. Powinna być zainstalowana
kiedy potrzebujemy systemu profilującego z GHC.

%package -n ghc-pandoc-doc
Summary:	HTML documentation for ghc %{name} package
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla pakietu ghc %{name}
Group:		Documentation

%description -n ghc-pandoc-doc
HTML documentation for ghc %{name} package.

%description -n ghc-pandoc-doc -l pl.UTF-8
Dokumentacja w formacie HTML dla pakietu ghc %{name}.

%prep
%setup -q
%patch0 -p1

%build
runhaskell Setup.hs configure -v2 \
	%{?with_prof:--enable-library-profiling} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_docdir}/ghc-pandoc-%{version}

runhaskell Setup.hs build
runhaskell Setup.hs haddock

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

runhaskell Setup.hs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf ghc-pandoc-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/ghc-pandoc-%{version}/html ghc-pandoc-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ghc-pandoc-%{version}

runhaskell Setup.hs register \
	--gen-pkg-config=$RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d/%{name}.conf

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/{BUGS,CONTRIBUTING.md,COPYRIGHT,INSTALL,README,changelog}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n ghc-pandoc
%ghc_pkg_recache

%postun	-n ghc-pandoc
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc BUGS CONTRIBUTING.md COPYRIGHT README changelog
%attr(755,root,root) %{_bindir}/pandoc
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/pandoc.1*
%{_mandir}/man5/pandoc_markdown.5*

%files -n ghc-pandoc
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/package.conf.d/%{name}.conf
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}
%{_libdir}/%{ghcdir}/%{name}-%{version}/HSpandoc-%{version}.o
%{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}.a
%{_libdir}/%{ghcdir}/%{name}-%{version}/Paths_pandoc.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/*.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Compat
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Compat/*.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/*.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Haddock
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Haddock/*.hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/*.hi

%if %{with prof}
%files -n ghc-pandoc-prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}_p.a
%{_libdir}/%{ghcdir}/%{name}-%{version}/Paths_pandoc.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Compat/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Haddock/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/*.p_hi
%endif

%files -n ghc-pandoc-doc
%defattr(644,root,root,755)
%doc ghc-pandoc-%{version}-doc/*
