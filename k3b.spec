%bcond clang 1
%bcond gamin 1
%bcond hal 0
%bcond sndfile 1
%bcond samplerate 1
%bcond dvdread 1
%bcond libmad 1
%bcond lame 1
%bcond ffmpeg 1
%bcond musepack 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg k3b
%define tde_prefix /opt/trinity
%define tde_appdir %{tde_datadir}/applications
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Epoch:			%{tde_epoch}
Version:		1.0.5
Release:		%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		CD/DVD burning application
Group:			Applications/Archiving
URL:			http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:    -DCMAKE_PROGRAM_PATH="%{tde_bindir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DBIN_INSTALL_DIR=%{tde_bindir}
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}
BuildOption:    -DLIB_INSTALL_DIR=%{tde_libdir}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_datadir}
BuildOption:    -DWITH_ALL_OPTIONS="ON"
BuildOption:    -DWITH_MUSICBRAINZ="OFF"
%{?with_ffmpeg:BuildOption:    -DWITH_FFMPEG_ALL_CODECS="ON"}
%{!?with_musepack:BuildOption:    -DWITH_MUSEPACK=OFF}
%{?with_musepack:BuildOption:    -DWITH_MUSEPACK=ON}
%{!?with_lame:BuildOption:    -DWITH_LAME=OFF}
%{?with_lame:BuildOption:    -DWITH_LAME=ON}
%{!?with_libmad:BuildOption:    -DWITH_MAD=OFF}
%{?with_libmad:BuildOption:    -DWITH_MAD=ON}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# ALSA supportl
BuildRequires:  pkgconfig(alsa)

BuildRequires:	pkgconfig(audiofile)
BuildRequires:	gettext
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(zlib-ng)

# VORBIS support
BuildRequires: pkgconfig(vorbis)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# ATTR support
BuildRequires:  pkgconfig(libattr)

Requires(post): coreutils
Requires(postun): coreutils

Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:		cdrecord
Requires:		mkisofs
Requires:		dvd+rw-tools

# CDRDAO support
Requires:		cdrdao

# UDEV support
BuildRequires:  pkgconfig(udev)

# HAL support
%{?with_hal:BuildRequires:	hal-devel}

# DBUS support
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
Requires:		trinity-dbus-tqt >= 1:0.63

# SNDFILE support
%{?with_sndfile:BuildRequires:  pkgconfig(sndfile)}

# SAMPLERATE support
%{?with_samplerate:BuildRequires:  pkgconfig(samplerate)}

# DVDREAD support
%{?with_dvdread:BuildRequires:  pkgconfig(dvdread)}

# FLAC support
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)

# MAD support
%{?with_libmad:BuildRequires:  pkgconfig(mad)}

# LAME support
%{?with_lame:BuildRequires:  pkgconfig(lame)}

# FFMPEG support
%{?with_ffmpeg:BuildRequires:  pkgconfig(libavcodec)}

# MUSEPACK
%{?with_musepack:BuildRequires:	%{_lib}mpcdec-devel}


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.


%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING TODO ChangeLog
%{tde_bindir}/k3b
%{tde_tdelibdir}/tdefile_k3b.la
%{tde_tdelibdir}/tdefile_k3b.so
%{tde_tdelibdir}/tdeio_videodvd.la
%{tde_tdelibdir}/tdeio_videodvd.so
%{tde_tdelibdir}/libk3balsaoutputplugin.la
%{tde_tdelibdir}/libk3balsaoutputplugin.so
%{tde_tdelibdir}/libk3bartsoutputplugin.la
%{tde_tdelibdir}/libk3bartsoutputplugin.so
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.la
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.so
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.la
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.so
%{tde_tdelibdir}/libk3bexternalencoder.la
%{tde_tdelibdir}/libk3bexternalencoder.so
%{tde_tdelibdir}/libk3bflacdecoder.la
%{tde_tdelibdir}/libk3bflacdecoder.so
%if %{with sndfile}
%{tde_tdelibdir}/libk3blibsndfiledecoder.la
%{tde_tdelibdir}/libk3blibsndfiledecoder.so
%endif
%if %{with musepack}
%{tde_tdelibdir}/libk3bmpcdecoder.la
%{tde_tdelibdir}/libk3bmpcdecoder.so
%endif
%{tde_tdelibdir}/libk3boggvorbisdecoder.la
%{tde_tdelibdir}/libk3boggvorbisdecoder.so
%{tde_tdelibdir}/libk3boggvorbisencoder.la
%{tde_tdelibdir}/libk3boggvorbisencoder.so
%{tde_tdelibdir}/libk3bsoxencoder.la
%{tde_tdelibdir}/libk3bsoxencoder.so
%{tde_tdelibdir}/libk3bwavedecoder.la
%{tde_tdelibdir}/libk3bwavedecoder.so
%lang(en) %{tde_tdedocdir}/HTML/en/k3b/
%{tde_mandir}/man1/k3b.1*

##########

%package common
Summary:		Common files of %{name}
Group:			Applications/Archiving
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description common
%{summary}.

%files common
%defattr(-,root,root,-)
%{tde_tdeappdir}/k3b.desktop
%{tde_datadir}/applnk/.hidden/k3b-cue.desktop
%{tde_datadir}/apps/k3b/
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_audiocd_rip.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_cd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_dvd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_cd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_dvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_videodvd_rip.desktop
%{tde_datadir}/mimelnk/application/x-k3b.desktop
%{tde_datadir}/icons/hicolor/*/apps/k3b.png
%{tde_datadir}/services/tdefile_k3b.desktop
%{tde_datadir}/services/videodvd.protocol
%{tde_datadir}/sounds/k3b_error1.wav
%{tde_datadir}/sounds/k3b_success1.wav
%{tde_datadir}/sounds/k3b_wait_media1.wav
%{tde_tdedocdir}/HTML/en/tdeioslave/videodvd/

##########

%package libs
Summary:		Runtime libraries for %{name}
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/libk3b.so.3
%{tde_libdir}/libk3b.so.3.0.0
%{tde_libdir}/libk3bdevice.so.5
%{tde_libdir}/libk3bdevice.so.5.0.0

##########

%package devel
Summary:		Files for the development of applications which will use %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libk3b.so
%{tde_libdir}/libk3bdevice.so

##########

%if %{with libmad}
%package plugin-mad
Summary:		The MAD plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-mad
%{summary}.

MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2  extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%files plugin-mad
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bmaddecoder.la
%{tde_tdelibdir}/libk3bmaddecoder.so
%endif

##########

%if %{with lame}
%package plugin-lame
Summary:		The LAME plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-lame
%{summary}.

Personal and commercial use of compiled versions of LAME (or any other mp3
encoder) requires a patent license in some countries.

This package is in tainted, as MP3 encoding is covered by software patents.

%files plugin-lame
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3blameencoder.la
%{tde_tdelibdir}/libk3blameencoder.so
%endif

##########

%if %{with ffmpeg}
%package plugin-ffmpeg
Summary:		The FFMPEG plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-ffmpeg
%{summary}.

ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

%files plugin-ffmpeg
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bffmpegdecoder.la
%{tde_tdelibdir}/libk3bffmpegdecoder.so
%endif

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
# remove the .la files
%__rm -f %{buildroot}%{tde_libdir}/libk3b*.la 

