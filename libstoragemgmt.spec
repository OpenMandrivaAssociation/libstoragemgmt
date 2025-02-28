%define major 1
%define libname %mklibname storagemgmt
%define devname %mklibname storagemgmt -d

# For the python module
%define _disable_ld_no_undefined 1

Name:		libstoragemgmt
Version:	1.10.2
Release:	1
Source0:	https://github.com/libstorage/libstoragemgmt/archive/%{version}/%{name}-%{version}.tar.gz
Summary:	Library for storage management
URL:		https://github.com/libstorage/libstoragemgmt
License:	GPL
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(ledmon)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libconfig)
BuildRequires:	sg3_utils-devel
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	python%{pyver}dist(pywbem)
BuildRequires:	valgrind
BuildRequires:	procps-ng
BuildSystem:	autotools

%patchlist
libstoragemgmt-clang.patch

%description
Library for Storage Management

%package -n %{libname}
Summary:	Library for Storage Management
Group:		System/Libraries

%description -n %{libname}
Library for Storage Management

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n python-%{name}
Summary:	Python bindings to %{name}
Group:		Development/Python
Requires:	%{libname} = %{EVRD}

%description -n python-%{name}
Python bindings to %{name}

%prep
%autosetup -p1
./autogen.sh

%files
%{_bindir}/*
%dir %{_sysconfdir}/lsm
%config %{_sysconfdir}/lsm/lsmd.conf
%dir %{_sysconfdir}/lsm/pluginconf.d
%config %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%config %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%config %{_sysconfdir}/lsm/pluginconf.d/local.conf
%config %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%config %{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%config %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_unitdir}/libstoragemgmt.service
%{_tmpfilesdir}/libstoragemgmt.conf
%{_libexecdir}/lsm.d
%{_datadir}/bash-completion/completions/lsmcli
%{_mandir}/man1/*.1*
%{_mandir}/man5/lsmd.conf.5*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*.3*

%files -n python-%{name}
%{py_sitedir}/arcconf_plugin
%{py_sitedir}/hpsa_plugin
%{py_sitedir}/local_plugin
%{py_sitedir}/megaraid_plugin
%{py_sitedir}/smispy_plugin
%{py_sitedir}/targetd_plugin
%{py_platsitedir}/nfs_plugin
%{py_platsitedir}/sim_plugin
%{py_platsitedir}/lsm
