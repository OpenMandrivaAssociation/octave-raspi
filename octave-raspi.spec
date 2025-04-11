%global octpkg raspi

Summary:	GNU Octave toolkit for controlling a Raspberry Pi 
Name:		octave-raspi
Version:	0.0.3
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/raspi/
Url:		https://sourceforge.net/projects/octave-raspberrypi
Source0:	https://downloads.sourceforge.net/project/octave-raspberrypi/v%{version}/raspi-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:  octave-instrument-control >= 0.4.0

Requires:	octave(api) = %{octave_api}
Requires:  	octave-instrument-control >= 0.4.0

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

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

%build
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

