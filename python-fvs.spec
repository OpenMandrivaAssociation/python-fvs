Name:           python-fvs
Version:        0.3.4
Release:        1
Summary:        File Versioning System with hash comparison, deduplication and data storage to create unlinked states that can be deleted
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mirkobrombin/FVS
Source:         https://github.com/mirkobrombin/FVS/archive/refs/tags/%{version}/FVS-%{version}.tar.gz
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(orjson)

Requires:       python3dist(orjson)

BuildArch:      noarch

%description
File Versioning System with hash comparison and data storage to create unlinked states that can be deleted

Why FVS?
The main reason for this project is for the purpose of personal knowledge and understanding of the versioning system. 
The second reason is to make a simple and easy-to-implement versioning system for Bottles.
There are plenty of other versioning systems out there, but all of these provide features that I wouldn't need in my projects. 
The purpose of FVS is to always remain as clear and simple as possible, providing only the functionality of organizing file versions into states, 
ie recovery points that take advantage of deduplication to minimize space consumption.

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
