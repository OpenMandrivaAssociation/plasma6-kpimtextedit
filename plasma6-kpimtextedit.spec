#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KF6PimTextEdit
%define devname %mklibname KF6PimTextEdit -d

Name: plasma6-kpimtextedit
Version:	24.02.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kpimtextedit/-/archive/%{gitbranch}/kpimtextedit-%{gitbranchd}.tar.bz2#/kpimtextedit-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kpimtextedit-%{version}.tar.xz
%endif
Summary: Text editing library for KDE PIM
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6TextEmoticonsWidgets)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6TextAddonsWidgets)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6TextToSpeech)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
Text editing library for KDE PIM.

%package -n %{libname}
Summary: KDE PIM library for text editing
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE PIM library for text editing.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kpimtextedit-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkpimtextedit6

%files -f libkpimtextedit6.lang
%{_datadir}/qlogging-categories6/kpimtextedit.categories

%files -n %{libname}
%{_libdir}/*.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
