# Install PostgreSQL 9.3 server from the PGDG repository
class {'postgresql::globals':
  manage_package_repo => true,
  version => '9.3',
}

class { 'postgresql::server':
  listen_addresses => '*',
  pg_hba_conf_defaults => false,
}

postgresql::server::pg_hba_rule { 'trust local access to all':
  type        => 'local',
  user        => 'all',
  auth_method => 'trust',
  order       => '001',
  database    => 'all',
}

postgresql::server::pg_hba_rule { 'trust host access to all':
  type        => 'host',
  user        => 'all',
  auth_method => 'trust',
  order       => '002',
  database    => 'all',
  address     => '0.0.0.0/0'
}

postgresql::server::pg_hba_rule { 'trust host access to 1/128':
  type        => 'host',
  user        => 'all',
  auth_method => 'trust',
  order       => '003',
  database    => 'all',
  address     => '::1/128'
}

# Install contrib modules
class { 'postgresql::server::contrib':
  package_ensure => 'present',
}

postgresql::server::db { 'trill':
  user     => 'trill',
  password => 'md584c2fc5a625dcf5c61be05f8584f6236',
}

postgresql::server::role { 'vagrant':
  password_hash => postgresql_password('vagrant', 'vagrant'),
  superuser => true,
}

postgresql::server::role { 'root':
  password_hash => postgresql_password('root', 'root'),
  superuser => true,
}

postgresql::server::database_grant { 'grant vagrant access to system of record':
  privilege => 'ALL',
  db        => 'trill',
  role      => 'vagrant',
}

postgresql::server::database_grant { 'grant root access to system of record':
  privilege => 'ALL',
  db        => 'trill',
  role      => 'root',
}