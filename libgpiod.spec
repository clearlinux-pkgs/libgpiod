#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : libgpiod
Version  : 2.1
Release  : 4
URL      : https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-2.1.tar.gz
Source0  : https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-2.1.tar.gz
Summary  : C library and tools for interacting with the linux GPIO character device
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 LGPL-2.1 LGPL-3.0
Requires: libgpiod-bin = %{version}-%{release}
Requires: libgpiod-lib = %{version}-%{release}
Requires: libgpiod-license = %{version}-%{release}
BuildRequires : autoconf-archive-dev
BuildRequires : pkgconfig(catch2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libedit)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(mount)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# SPDX-License-Identifier: CC-BY-SA-4.0
libgpiod
========
libgpiod - C library and tools for interacting with the linux GPIO
character device (gpiod stands for GPIO device)

%package bin
Summary: bin components for the libgpiod package.
Group: Binaries
Requires: libgpiod-license = %{version}-%{release}

%description bin
bin components for the libgpiod package.


%package dev
Summary: dev components for the libgpiod package.
Group: Development
Requires: libgpiod-lib = %{version}-%{release}
Requires: libgpiod-bin = %{version}-%{release}
Provides: libgpiod-devel = %{version}-%{release}
Requires: libgpiod = %{version}-%{release}

%description dev
dev components for the libgpiod package.


%package lib
Summary: lib components for the libgpiod package.
Group: Libraries
Requires: libgpiod-license = %{version}-%{release}

%description lib
lib components for the libgpiod package.


%package license
Summary: license components for the libgpiod package.
Group: Default

%description license
license components for the libgpiod package.


%prep
%setup -q -n libgpiod-2.1
cd %{_builddir}/libgpiod-2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699915264
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699915264
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgpiod
cp %{_builddir}/libgpiod-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/libgpiod/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libgpiod/cfa18f4cfd3c9a92cd5e109df5927ac08c6eaf3b || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/libgpiod/86d39c3677042ddb21c5eda2a447c5bd81f23446 || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libgpiod/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libgpiod/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgpiod/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/LGPL-%{version}-or-later.txt %{buildroot}/usr/share/package-licenses/libgpiod/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/libgpiod-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/libgpiod/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
%make_install
## install_append content
make -C tools
make -C tools install DESTDIR=%{buildroot}
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gpiodetect
/usr/bin/gpioget
/usr/bin/gpioinfo
/usr/bin/gpiomon
/usr/bin/gpionotify
/usr/bin/gpioset

%files dev
%defattr(-,root,root,-)
/usr/include/gpiod.h
/usr/lib64/libgpiod.so
/usr/lib64/pkgconfig/libgpiod.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgpiod.so.3
/usr/lib64/libgpiod.so.3.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgpiod/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/libgpiod/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libgpiod/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/libgpiod/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/libgpiod/86d39c3677042ddb21c5eda2a447c5bd81f23446
/usr/share/package-licenses/libgpiod/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
/usr/share/package-licenses/libgpiod/cfa18f4cfd3c9a92cd5e109df5927ac08c6eaf3b
