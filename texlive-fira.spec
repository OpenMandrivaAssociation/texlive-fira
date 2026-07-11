%global tl_name fira
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3
Release:	%{tl_revision}.1
Summary:	Fira fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fira
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fira.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fira.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the Fira Sans and Fira Mono families of fonts designed by Erik
Spiekermann and Ralph du Carrois of Carrois Type Design. Fira Sans is
available in eleven weights with corresponding italics: light, regular,
medium, bold, ...

