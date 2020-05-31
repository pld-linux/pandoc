#
# Conditional build:
%bcond_without	prof	# profiling library
#
Summary:	Conversion between markup formats
Summary(pl.UTF-8):	Konwersja między różnymi formatami znaczników
Name:		pandoc
Version:	2.9.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	https://github.com/jgm/pandoc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3a403a40c9e5f7179f36c7817b97e83d
Patch0:		%{name}-deps.patch
Patch1:		jira-wiki-markup-1.3.patch
URL:		http://johnmacfarlane.net/pandoc/
BuildRequires:	alex
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-Glob >= 0.7
BuildRequires:	ghc-HTTP >= 4000.0.5
BuildRequires:	ghc-HsYAML >= 0.2
BuildRequires:	ghc-JuicyPixels >= 3.1.6.1
BuildRequires:	ghc-SHA >= 1.6
BuildRequires:	ghc-aeson >= 0.7
BuildRequires:	ghc-aeson-pretty >= 0.8.5
BuildRequires:	ghc-attoparsec >= 0.12
BuildRequires:	ghc-base64-bytestring >= 0.1
BuildRequires:	ghc-base-compat >= 0.9,
BuildRequires:	ghc-base-noprelude >= 4.9
BuildRequires:	ghc-binary >= 0.5
BuildRequires:	ghc-blaze-html >= 0.9
BuildRequires:	ghc-blaze-markup >= 0.8
BuildRequires:	ghc-bytestring >= 0.9
BuildRequires:	ghc-case-insensitive >= 1.2
BuildRequires:	ghc-cmark-gfm >= 0.2
BuildRequires:	ghc-containers >= 0.4.2.1
BuildRequires:	ghc-data-default >= 0.4
BuildRequires:	ghc-deepseq >= 1.3
BuildRequires:	ghc-directory >= 1.2.3
BuildRequires:	ghc-doclayout >= 0.3
BuildRequires:	ghc-doctemplates >= 0.8
BuildRequires:	ghc-emojis >= 0.1
BuildRequires:	ghc-exceptions >= 0.8
BuildRequires:	ghc-file-embed >= 0.0
BuildRequires:	ghc-filepath >= 1.1
BuildRequires:	ghc-haddock-library >= 1.8
BuildRequires:	ghc-hslua >= 1.0.1
BuildRequires:	ghc-hslua-module-system >= 0.2
BuildRequires:	ghc-hslua-module-text >= 0.2
BuildRequires:	ghc-http-client >= 0.4.30
BuildRequires:	ghc-http-client-tls >= 0.2.4
BuildRequires:	ghc-http-types >= 0.8
BuildRequires:	ghc-ipynb >= 0.1
BuildRequires:	ghc-jira-wiki-markup >= 1.1.3
BuildRequires:	ghc-mtl >= 2.2
BuildRequires:	ghc-network >= 2.6,
BuildRequires:	ghc-network-uri >= 2.6
BuildRequires:	ghc-pandoc-types >= 1.20
BuildRequires:	ghc-parsec >= 3.1
BuildRequires:	ghc-process >= 1.2.3
BuildRequires:	ghc-random >= 1
BuildRequires:	ghc-safe >= 0.3
BuildRequires:	ghc-scientific >= 0.3
BuildRequires:	ghc-skylighting >= 0.8.3.2
BuildRequires:	ghc-skylighting-core >= 0.8.3.2
BuildRequires:	ghc-split >= 0.2
BuildRequires:	ghc-syb >= 0.1
BuildRequires:	ghc-tagsoup >= 0.14.6
BuildRequires:	ghc-temporary >= 1.1
BuildRequires:	ghc-texmath >= 0.12.0.1
BuildRequires:	ghc-text >= 1.1.1.0
BuildRequires:	ghc-text-conversions >= 0.3
BuildRequires:	ghc-time >= 1.5
BuildRequires:	ghc-unicode-transforms >= 0.3
BuildRequires:	ghc-unordered-containers >= 0.2
BuildRequires:	ghc-vector >= 0.10
BuildRequires:	ghc-xml >= 1.3.12
BuildRequires:	ghc-zip-archive >= 0.2.3.4
BuildRequires:	ghc-zlib >= 0.5
%if %{with prof}
BuildRequires:	ghc-Glob-prof >= 0.7
BuildRequires:	ghc-HTTP-prof >= 4000.0.5
BuildRequires:	ghc-HsYAML-prof >= 0.2
BuildRequires:	ghc-JuicyPixels-prof >= 3.1.6.1
BuildRequires:	ghc-SHA-prof >= 1.6
BuildRequires:	ghc-aeson-prof >= 0.7
BuildRequires:	ghc-aeson-pretty-prof >= 0.8.5
BuildRequires:	ghc-attoparsec-prof >= 0.12
BuildRequires:	ghc-base64-bytestring-prof >= 0.1
BuildRequires:	ghc-base-compat-prof >= 0.9,
BuildRequires:	ghc-binary-prof >= 0.5
BuildRequires:	ghc-blaze-html-prof >= 0.9
BuildRequires:	ghc-blaze-markup-prof >= 0.8
BuildRequires:	ghc-bytestring-prof >= 0.9
BuildRequires:	ghc-case-insensitive-prof >= 1.2
BuildRequires:	ghc-cmark-gfm-prof >= 0.2
BuildRequires:	ghc-containers-prof >= 0.4.2.1
BuildRequires:	ghc-data-default-prof >= 0.4
BuildRequires:	ghc-deepseq-prof >= 1.3
BuildRequires:	ghc-directory-prof >= 1.2.3
BuildRequires:	ghc-doclayout-prof >= 0.3
BuildRequires:	ghc-doctemplates-prof >= 0.8
BuildRequires:	ghc-emojis-prof >= 0.1
BuildRequires:	ghc-exceptions-prof >= 0.8
BuildRequires:	ghc-file-embed-prof >= 0.0
BuildRequires:	ghc-filepath-prof >= 1.1
BuildRequires:	ghc-haddock-library-prof >= 1.8
BuildRequires:	ghc-hslua-prof >= 1.0.1
BuildRequires:	ghc-hslua-module-system-prof >= 0.2
BuildRequires:	ghc-hslua-module-text-prof >= 0.2
BuildRequires:	ghc-http-client-prof >= 0.4.30
BuildRequires:	ghc-http-client-tls-prof >= 0.2.4
BuildRequires:	ghc-http-types-prof >= 0.8
BuildRequires:	ghc-ipynb-prof >= 0.1
BuildRequires:	ghc-jira-wiki-markup-prof >= 1.1.3
BuildRequires:	ghc-mtl-prof >= 2.2
BuildRequires:	ghc-network-prof >= 2.6,
BuildRequires:	ghc-network-uri-prof >= 2.6
BuildRequires:	ghc-pandoc-types-prof >= 1.20
BuildRequires:	ghc-parsec-prof >= 3.1
BuildRequires:	ghc-process-prof >= 1.2.3
BuildRequires:	ghc-random-prof >= 1
BuildRequires:	ghc-safe-prof >= 0.3
BuildRequires:	ghc-scientific-prof >= 0.3
BuildRequires:	ghc-skylighting-prof >= 0.8.3.2
BuildRequires:	ghc-skylighting-core-prof >= 0.8.3.2
BuildRequires:	ghc-split-prof >= 0.2
BuildRequires:	ghc-syb-prof >= 0.1
BuildRequires:	ghc-tagsoup-prof >= 0.14.6
BuildRequires:	ghc-temporary-prof >= 1.1
BuildRequires:	ghc-texmath-prof >= 0.12.0.1
BuildRequires:	ghc-text-prof >= 1.1.1.0
BuildRequires:	ghc-text-conversions-prof >= 0.3
BuildRequires:	ghc-time-prof >= 1.5
BuildRequires:	ghc-unicode-transforms-prof >= 0.3
BuildRequires:	ghc-unordered-containers-prof >= 0.2
BuildRequires:	ghc-vector-prof >= 0.10
BuildRequires:	ghc-xml-prof >= 1.3.12
BuildRequires:	ghc-zip-archive-prof >= 0.2.3.4
BuildRequires:	ghc-zlib-prof >= 0.5
%endif
BuildRequires:	happy
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
Requires:	ghc-Glob >= 0.7
Requires:	ghc-HTTP >= 4000.0.5
Requires:	ghc-HsYAML >= 0.2
Requires:	ghc-JuicyPixels >= 3.1.6.1
Requires:	ghc-SHA >= 1.6
Requires:	ghc-aeson >= 0.7
Requires:	ghc-aeson-pretty >= 0.8.5
Requires:	ghc-attoparsec >= 0.12
Requires:	ghc-base64-bytestring >= 0.1
Requires:	ghc-base-compat >= 0.9,
Requires:	ghc-base-noprelude >= 4.9
Requires:	ghc-binary >= 0.5
Requires:	ghc-blaze-html >= 0.9
Requires:	ghc-blaze-markup >= 0.8
Requires:	ghc-bytestring >= 0.9
Requires:	ghc-case-insensitive >= 1.2
Requires:	ghc-cmark-gfm >= 0.2
Requires:	ghc-containers >= 0.4.2.1
Requires:	ghc-data-default >= 0.4
Requires:	ghc-deepseq >= 1.3
Requires:	ghc-directory >= 1.2.3
Requires:	ghc-doclayout >= 0.3
Requires:	ghc-doctemplates >= 0.8
Requires:	ghc-emojis >= 0.1
Requires:	ghc-exceptions >= 0.8
Requires:	ghc-file-embed >= 0.0
Requires:	ghc-filepath >= 1.1
Requires:	ghc-haddock-library >= 1.8
Requires:	ghc-hslua >= 1.0.1
Requires:	ghc-hslua-module-system >= 0.2
Requires:	ghc-hslua-module-text >= 0.2
Requires:	ghc-http-client >= 0.4.30
Requires:	ghc-http-client-tls >= 0.2.4
Requires:	ghc-http-types >= 0.8
Requires:	ghc-ipynb >= 0.1
Requires:	ghc-jira-wiki-markup >= 1.1.3
Requires:	ghc-mtl >= 2.2
Requires:	ghc-network >= 2.6,
Requires:	ghc-network-uri >= 2.6
Requires:	ghc-pandoc-types >= 1.20
Requires:	ghc-parsec >= 3.1
Requires:	ghc-process >= 1.2.3
Requires:	ghc-random >= 1
Requires:	ghc-safe >= 0.3
Requires:	ghc-scientific >= 0.3
Requires:	ghc-skylighting >= 0.8.3.2
Requires:	ghc-skylighting-core >= 0.8.3.2
Requires:	ghc-split >= 0.2
Requires:	ghc-syb >= 0.1
Requires:	ghc-tagsoup >= 0.14.6
Requires:	ghc-temporary >= 1.1
Requires:	ghc-texmath >= 0.12.0.1
Requires:	ghc-text >= 1.1.1.0
Requires:	ghc-text-conversions >= 0.3
Requires:	ghc-time >= 1.5
Requires:	ghc-unicode-transforms >= 0.3
Requires:	ghc-unordered-containers >= 0.2
Requires:	ghc-vector >= 0.10
Requires:	ghc-xml >= 1.3.12
Requires:	ghc-zip-archive >= 0.2.3.4
Requires:	ghc-zlib >= 0.5

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
Requires:	ghc-Glob-prof >= 0.7
Requires:	ghc-HTTP-prof >= 4000.0.5
Requires:	ghc-HsYAML-prof >= 0.2
Requires:	ghc-JuicyPixels-prof >= 3.1.6.1
Requires:	ghc-SHA-prof >= 1.6
Requires:	ghc-aeson-prof >= 0.7
Requires:	ghc-aeson-pretty-prof >= 0.8.5
Requires:	ghc-attoparsec-prof >= 0.12
Requires:	ghc-base64-bytestring-prof >= 0.1
Requires:	ghc-base-compat-prof >= 0.9,
Requires:	ghc-binary-prof >= 0.5
Requires:	ghc-blaze-html-prof >= 0.9
Requires:	ghc-blaze-markup-prof >= 0.8
Requires:	ghc-bytestring-prof >= 0.9
Requires:	ghc-case-insensitive-prof >= 1.2
Requires:	ghc-cmark-gfm-prof >= 0.2
Requires:	ghc-containers-prof >= 0.4.2.1
Requires:	ghc-data-default-prof >= 0.4
Requires:	ghc-deepseq-prof >= 1.3
Requires:	ghc-directory-prof >= 1.2.3
Requires:	ghc-doclayout-prof >= 0.3
Requires:	ghc-doctemplates-prof >= 0.8
Requires:	ghc-emojis-prof >= 0.1
Requires:	ghc-exceptions-prof >= 0.8
Requires:	ghc-file-embed-prof >= 0.0
Requires:	ghc-filepath-prof >= 1.1
Requires:	ghc-haddock-library-prof >= 1.8
Requires:	ghc-hslua-prof >= 1.0.1
Requires:	ghc-hslua-module-system-prof >= 0.2
Requires:	ghc-hslua-module-text-prof >= 0.2
Requires:	ghc-http-client-prof >= 0.4.30
Requires:	ghc-http-client-tls-prof >= 0.2.4
Requires:	ghc-http-types-prof >= 0.8
Requires:	ghc-ipynb-prof >= 0.1
Requires:	ghc-jira-wiki-markup-prof >= 1.1.3
Requires:	ghc-mtl-prof >= 2.2
Requires:	ghc-network-prof >= 2.6,
Requires:	ghc-network-uri-prof >= 2.6
Requires:	ghc-pandoc-types-prof >= 1.20
Requires:	ghc-parsec-prof >= 3.1
Requires:	ghc-process-prof >= 1.2.3
Requires:	ghc-random-prof >= 1
Requires:	ghc-safe-prof >= 0.3
Requires:	ghc-scientific-prof >= 0.3
Requires:	ghc-skylighting-prof >= 0.8.3.2
Requires:	ghc-skylighting-core-prof >= 0.8.3.2
Requires:	ghc-split-prof >= 0.2
Requires:	ghc-syb-prof >= 0.1
Requires:	ghc-tagsoup-prof >= 0.14.6
Requires:	ghc-temporary-prof >= 1.1
Requires:	ghc-texmath-prof >= 0.12.0.1
Requires:	ghc-text-prof >= 1.1.1.0
Requires:	ghc-text-conversions-prof >= 0.3
Requires:	ghc-time-prof >= 1.5
Requires:	ghc-unicode-transforms-prof >= 0.3
Requires:	ghc-unordered-containers-prof >= 0.2
Requires:	ghc-vector-prof >= 0.10
Requires:	ghc-xml-prof >= 1.3.12
Requires:	ghc-zip-archive-prof >= 0.2.3.4
Requires:	ghc-zlib-prof >= 0.5

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
%patch1 -p1

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
install -d $RPM_BUILD_ROOT{%{_libdir}/%{ghcdir}/package.conf.d,%{_mandir}/man1}

runhaskell Setup.hs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf ghc-pandoc-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/ghc-pandoc-%{version}/html ghc-pandoc-%{version}-doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ghc-pandoc-%{version}

runhaskell Setup.hs register \
	--gen-pkg-config=$RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d/%{name}.conf


cp -p man/pandoc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n ghc-pandoc
%ghc_pkg_recache

%postun	-n ghc-pandoc
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc AUTHORS.md BUGS changelog.md CONTRIBUTING.md COPYING.md COPYRIGHT README.md
%attr(755,root,root) %{_bindir}/pandoc
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/pandoc.1*

%files -n ghc-pandoc
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/package.conf.d/%{name}.conf
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}
%{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}-*.so
%{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}-*.a
%exclude %{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}*_p.a
%{_libdir}/%{ghcdir}/%{name}-%{version}/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/App
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/App/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/App/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Class
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Class/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Class/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Filter
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Filter/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Filter/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Marshaling
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Marshaling/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Marshaling/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Module
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Module/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Module/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/Parse
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/Parse/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/Parse/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/LaTeX
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/LaTeX/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/LaTeX/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Arrows
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Arrows/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Arrows/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Generic
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Generic/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Generic/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Org
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Org/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Org/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Docx
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Docx/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Docx/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Powerpoint
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Powerpoint/*.hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Powerpoint/*.dyn_hi

%if %{with prof}
%files -n ghc-pandoc-prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{name}-%{version}/libHSpandoc-%{version}*_p.a
%{_libdir}/%{ghcdir}/%{name}-%{version}/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/App/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Class/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Filter/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Marshaling/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Lua/Module/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/LaTeX/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Arrows/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Odt/Generic/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Org/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Docx/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Readers/Docx/Parse/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/*.p_hi
%{_libdir}/%{ghcdir}/%{name}-%{version}/Text/Pandoc/Writers/Powerpoint/*.p_hi
%endif

%files -n ghc-pandoc-doc
%defattr(644,root,root,755)
%doc ghc-pandoc-%{version}-doc/*
