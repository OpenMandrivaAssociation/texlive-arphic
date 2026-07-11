%global tl_name arphic
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Arphic (Chinese) font packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/arphic
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arphic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arphic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These are font bundles for the Chinese Arphic fonts which work with the
CJK package. TrueType versions of these fonts for use with XeLaTeX and
LuaLaTeX are provided by the arphic-ttf package. Arphic is actually the
name of the company which created these fonts (and put them under a GPL-
like licence).

