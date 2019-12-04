# frozen_string_literal: true

describe package('nfs-common') do
  it { should be_installed }
  its('version') { should eq '1:1.3.4-2.1' }
end

describe command('nfsstat --version') do
  its('stdout') { should eq "nfsstat: 1.3.3\n" }
  its('stderr') { should eq '' }
  its('exit_status') { should eq 0 }
end
