Name:		texlive-fira
Version:	4.3
Release:	1
Summary:	Fira fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/fira
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fira.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fira.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Fira Sans family of fonts (version 2.001),
designed by Erik Spiekermann and Ralph du Carrois of Carrois
Type Design. Fira Sans is available in four weights with
corresponding italics: light, regular, medium, and bold.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/fira
%{_texmfdistdir}/fonts/map/dvips/fira
%{_texmfdistdir}/fonts/opentype/public/fira
%{_texmfdistdir}/fonts/tfm/public/fira
%{_texmfdistdir}/fonts/type1/public/fira
%{_texmfdistdir}/fonts/vf/public/fira
%{_texmfdistdir}/tex/latex/fira
%doc %{_texmfdistdir}/doc/fonts/fira

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
