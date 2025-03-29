# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-typing-inspect
Epoch: 100
Version: 0.9.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Runtime inspection utilities for typing module
License:  MIT
URL: https://github.com/ilevkivskyi/typing_inspect/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typing-inspect
Summary: Runtime inspection utilities for typing module
Requires: python3
Requires: python3-mypy-extensions >= 0.3.0
Requires: python3-typing-extensions >= 3.7.4
Provides: python3-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typing-inspect) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-typing-inspect
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%files -n python%{python3_version_nodots}-typing-inspect
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-typing-inspect
Summary: Runtime inspection utilities for typing module
Requires: python3
Requires: python3-mypy-extensions >= 0.3.0
Requires: python3-typing-extensions >= 3.7.4
Provides: python3-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typing-inspect) = %{epoch}:%{version}-%{release}

%description -n python3-typing-inspect
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%files -n python3-typing-inspect
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-typing-inspect
Summary: Runtime inspection utilities for typing module
Requires: python3
Requires: python3-mypy-extensions >= 0.3.0
Requires: python3-typing-extensions >= 3.7.4
Provides: python3-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python3dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typing-inspect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typing-inspect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typing-inspect) = %{epoch}:%{version}-%{release}

%description -n python3-typing-inspect
The "typing_inspect" module defines experimental API for runtime
inspection of types defined in the standard "typing" module.

%files -n python3-typing-inspect
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
