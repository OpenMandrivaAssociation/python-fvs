Name:           python-fvs
Version:        0.3.4
Release:        4
Summary:        File versioning with hash comparison and deduplication
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mirkobrombin/FVS
Source:         https://github.com/mirkobrombin/FVS/archive/refs/tags/%{version}/FVS-%{version}.tar.gz
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(orjson)

Requires:       python%{pyver}dist(orjson)

BuildArch:      noarch

%description
File versioning with hash comparison and deduplication.

FVS stores recovery points that share unchanged data instead of
copying whole trees. It is a small system aimed at Bottles and
similar tools, not a general version-control system.

%prep
%autosetup -n FVS-%{version} -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/fvs
%{python_sitelib}/FVS-%{version}-py*.*.egg-info
%{python_sitelib}/fvs/
