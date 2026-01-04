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
%define pkg_rel 3

%define tde_pkg k3b
%define tde_prefix /opt/trinity


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


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_MUSICBRAINZ=OFF
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_FFMPEG_ALL_CODECS=%{!?with_ffmpeg:OFF}%{?with_ffmpeg:ON}
BuildOption:    -DWITH_MUSEPACK=%{!?with_musepack:OFF}%{?with_musepack:ON}
BuildOption:    -DWITH_LAME=%{!?with_lame:OFF}%{?with_lame:ON}
BuildOption:    -DWITH_MAD=%{!?with_libmad:OFF}%{?with_libmad:ON}

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
%{tde_prefix}/bin/k3b
%{tde_prefix}/%{_lib}/trinity/tdefile_k3b.la
%{tde_prefix}/%{_lib}/trinity/tdefile_k3b.so
%{tde_prefix}/%{_lib}/trinity/tdeio_videodvd.la
%{tde_prefix}/%{_lib}/trinity/tdeio_videodvd.so
%{tde_prefix}/%{_lib}/trinity/libk3balsaoutputplugin.la
%{tde_prefix}/%{_lib}/trinity/libk3balsaoutputplugin.so
%{tde_prefix}/%{_lib}/trinity/libk3bartsoutputplugin.la
%{tde_prefix}/%{_lib}/trinity/libk3bartsoutputplugin.so
%{tde_prefix}/%{_lib}/trinity/libk3baudiometainforenamerplugin.la
%{tde_prefix}/%{_lib}/trinity/libk3baudiometainforenamerplugin.so
%{tde_prefix}/%{_lib}/trinity/libk3baudioprojectcddbplugin.la
%{tde_prefix}/%{_lib}/trinity/libk3baudioprojectcddbplugin.so
%{tde_prefix}/%{_lib}/trinity/libk3bexternalencoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bexternalencoder.so
%{tde_prefix}/%{_lib}/trinity/libk3bflacdecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bflacdecoder.so
%if %{with sndfile}
%{tde_prefix}/%{_lib}/trinity/libk3blibsndfiledecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3blibsndfiledecoder.so
%endif
%if %{with musepack}
%{tde_prefix}/%{_lib}/trinity/libk3bmpcdecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bmpcdecoder.so
%endif
%{tde_prefix}/%{_lib}/trinity/libk3boggvorbisdecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3boggvorbisdecoder.so
%{tde_prefix}/%{_lib}/trinity/libk3boggvorbisencoder.la
%{tde_prefix}/%{_lib}/trinity/libk3boggvorbisencoder.so
%{tde_prefix}/%{_lib}/trinity/libk3bsoxencoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bsoxencoder.so
%{tde_prefix}/%{_lib}/trinity/libk3bwavedecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bwavedecoder.so
%lang(en) %{tde_prefix}/share/doc/tde/HTML/en/k3b/
%{tde_prefix}/share/man/man1/k3b.1*

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
%{tde_prefix}/share/applications/tde/k3b.desktop
%{tde_prefix}/share/applnk/.hidden/k3b-cue.desktop
%{tde_prefix}/share/apps/k3b/
%{tde_prefix}/share/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_audiocd_rip.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_cd_copy.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_dvd_copy.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_handle_empty_cd.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_handle_empty_dvd.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/k3b_videodvd_rip.desktop
%{tde_prefix}/share/mimelnk/application/x-k3b.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/k3b.png
%{tde_prefix}/share/services/tdefile_k3b.desktop
%{tde_prefix}/share/services/videodvd.protocol
%{tde_prefix}/share/sounds/k3b_error1.wav
%{tde_prefix}/share/sounds/k3b_success1.wav
%{tde_prefix}/share/sounds/k3b_wait_media1.wav
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/videodvd/

##########

%package libs
Summary:		Runtime libraries for %{name}
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libk3b.so.3
%{tde_prefix}/%{_lib}/libk3b.so.3.0.0
%{tde_prefix}/%{_lib}/libk3bdevice.so.5
%{tde_prefix}/%{_lib}/libk3bdevice.so.5.0.0

##########

%package devel
Summary:		Files for the development of applications which will use %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/*.h
%{tde_prefix}/%{_lib}/libk3b.so
%{tde_prefix}/%{_lib}/libk3bdevice.so

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
%{tde_prefix}/%{_lib}/trinity/libk3bmaddecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bmaddecoder.so
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
%{tde_prefix}/%{_lib}/trinity/libk3blameencoder.la
%{tde_prefix}/%{_lib}/trinity/libk3blameencoder.so
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
%{tde_prefix}/%{_lib}/trinity/libk3bffmpegdecoder.la
%{tde_prefix}/%{_lib}/trinity/libk3bffmpegdecoder.so
%endif

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
# remove the .la files
%__rm -f %{buildroot}%{tde_prefix}/%{_lib}/libk3b*.la 

