# template: default
%global gem_name sidekiq

Name: rubygem-%{gem_name}
Version: 6.5.12
Release: 1%{?dist}
Summary: Simple, efficient background processing for Ruby
License: LGPL-3.0
URL: https://sidekiq.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Simple, efficient background processing for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/sidekiq
%{_bindir}/sidekiqmon
%doc %{gem_instdir}/Changes.md
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/web
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/sidekiq.gemspec

%changelog
* Thu Oct 12 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.5.12-1
- Update to 6.5.12

* Tue Oct 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.5.11-1
- Update to 6.5.11

* Fri Sep 23 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.3.1-2
- Include web directory

* Tue Aug 23 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.3.1-1
- Update to 6.3.1

* Fri Mar 18 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.2.10-1
- Update to 5.2.10

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.2.7-4
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.7-3
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2.7-2
- Update spec to remove the ror scl

* Tue Oct 15 2019 Adam Ruzicka <aruzicka@redhat.com> 5.2.7-1
- Add rubygem-sidekiq generated by gem2rpm using the scl template
