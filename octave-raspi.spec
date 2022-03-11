%global octpkg raspi

Summary:	GNU Octave toolkit for controlling a Raspberry Pi 
Name:		octave-%{octpkg}
Version:	0.0.2
Release:	1
Url:		https://sourceforge.net/projects/octave-raspberrypi
Source0:	https://downloads.sourceforge.net/octave-raspberrypi/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0
BuildRequires:	octave-instrument-control >= 0.4.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-instrument-control >= 0.4.0

Requires(post): octave
Requires(postun): octave

%description
Basic Octave implementation of the matlab raspi extension, allowing
communication to a Raspberry Pi board to control its hardware.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

