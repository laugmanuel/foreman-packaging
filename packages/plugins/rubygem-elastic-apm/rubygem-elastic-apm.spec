# template: default
%global gem_name elastic-apm

Name: rubygem-%{gem_name}
Version: 4.7.3
Release: 1%{?dist}
Summary: The official Elastic APM agent for Ruby
License: Apache-2.0
URL: https://github.com/elastic/apm-agent-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.3.0
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
The official Elastic APM agent for Ruby.


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

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.ci
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.pre-commit-config.yaml
%exclude %{gem_instdir}/.rubocop.yml
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%{gem_instdir}/Dockerfile
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/bench
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.asciidoc
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docker-compose.yml
%doc %{gem_instdir}/docs
%exclude %{gem_instdir}/elastic-apm.gemspec

%changelog
* Wed Aug 21 2024 Manuel Laug - 4.7.3-1
- Update elastic-apm to 4.7.3

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.9.1-3
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.9.1-2
- Update spec to remove the ror scl

* Fri Apr 12 2019 Timo Goebel <mail@timogoebel.name> 2.9.1-1
- Add rubygem-elastic-apm generated by gem2rpm using the scl template
