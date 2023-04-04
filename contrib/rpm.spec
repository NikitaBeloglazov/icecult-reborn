#
# spec file for package icecult-reborn
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           icecult-reborn
Version:        0.1.0
Release:        0
Summary:        icecult-reborn - web interface for eiskaltdcpp-daemon
License:        MIT
URL:            https://github.com/NikitaBeloglazov/icecult-reborn
Source:         %{name}-%{version}.tar.gz
Requires:       python3
Requires:       %{python_module Flask}

%description
icecult-reborn - web interface for eiskaltdcpp-daemon

%prep
%setup

%build

%install
install -Dm 644  contrib/systemd/icecult.service %{buildroot}%{_unitdir}/icecult.service
install -Dm 644  contrib/systemd/icecult.sysusers %{buildroot}%{_sysusersdir}/system-user-icecult.conf
install -Dm 644  contrib/systemd/valheim.env %{buildroot}%{_sysconfdir}/icecult.conf
install -Dm 755  redirect.py %{buildroot}%{_bindir}/icecult
install -Dm 644 ./contrib/icecult_nginx_conf %{buildroot}%{_sysconfdir}/nginx/conf.d/icecult.conf
cp  app/* %{buildroot}%{_datadir}/icecult

%files
%{_unitdir}/icecult.service
%{_sysusersdir}/system-user-icecult.conf
%config(noreplace) %{_sysconfdir}/icecult.conf
%{_datadir}/icecult
%config(noreplace) /usr/share/icecult/templates/nginx/conf.d/icecult.conf

%pre
%service_add_pre icecult.service

%post
%service_add_post icecult.service

%preun
%service_del_preun icecult.service

%postun
%service_del_postun icecult.service

%changelog
