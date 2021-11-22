# About role
This ansible role intended for setting on the host Traefik. 

# Using variables

### Defaults variables
| **Inventory**               | **Description**             |
| --------------------------- | --------------------------- |
| `traefik_distr_ver` | The version of Traefik used. (Default: `v2.5.4`) |
| `traefik_distr_os` | Operating system. (Default: `linux`) |
| `traefik_distr_arch` | OS architecture. (Default: `amd64`) |
| `traefik_url_release` | Traefik Archive URL. (Default: `https://github.com/containous/traefik/releases/download/v2.5.4/traefik_v2.5.4_linux_amd64.tar.gz`) |
| `traefik_path_bin` | Traefik bin location path. (Default: `/usr/bin`) |
| `traefik_binary` | Full path of Traefik on the system. (Default: `/usr/bin/traefik_v2.5.4`) |
| `traefik_le_caserver` |  Determines which service issues the certificate. For test runs use - `https://acme-staging-v02.api.letsencrypt.org/directory.`. For production - `https://acme-v02.api.letsencrypt.org/directory`. (Default: `https://acme-v02.api.letsencrypt.org/directory`) |
| `traefik_le_challenge_type` | Different ACME Challenges. It is possible to use `httpChallenge` and `dnsChallenge`. (Default: `httpChallenge`) |
| `traefik_le_email` | Required parameter to get the certificate Let’s Encrypt. (Default: `NULL`) |
| `traefik_log_level` | Default: `WARN` . Alternative logging levels are `DEBUG`, `PANIC`, `FATAL`, `ERROR`, `WARN` and `INFO`. |
| `traefik_enable_prometheus` | Default: `true` . Enables prometheus metrics endpoint. |
| `traefik_providers` | Default: `{}` . Setup other providers support. Key is provider name, value - provider settings. |
| `traefik_dashboard_port` | Default: `8080` . Insecure dashboard port. |
| `traefik_metrics_port` | Default: `8082` . Insecure metrics port for prometheus. |
| `traefik_entrypoints_extra_parameters` | Configure parameters Traefik entrypoints . Uses for `http` and `https` entrypoints. (Default: `[]`). |

### Inventory variables
#### HTTP service
The `traefik_http_dynamic_config` variable describes the configuration of services operating over the `http protocol`.
Required variables: `name`, `services_url`, `domain`.
* `name` - The name of your configuration.
* `services_url` - Service address.
* `domain` or `raw_domain` - The domain on which the service will run.

[Rule http. Resource link](https://doc.traefik.io/traefik/routing/routers/#rule)

TLS Certificates:
* You can connect your TLS Certificate to each service `tls_resolver` or `tls`.
* `tls` - Your generated self-signed certificate.
* `tls_resolver` - Certificate provided by Let’s Encrypt. 
Required parameters: `main` and `sans`.

```yaml
# Example:
traefik_http_dynamic_config:
  # http, no certificate
  - name: 'name_config__HTTP__'
    services_url: 'http://172.16.1.10:9000'
    domain: 'test-http.example.com'
  # https with Let`s Encrypt cert + traefik rule custom host
  - name: 'name_config__HTTPS__1'
    services_url: 'http://172.16.1.10:9000'
    domain: 'testdomain.example.com'
    tls_resolver:
      main: 'testdomain.example.com'
      sans: '*.testdomain.example.com'
  # https with Let`s Encrypt cert + traefik ruled Host
  - name: 'name_config__HTTPS__1'
    services_url: 'http://172.16.1.10:9000'
    raw_domain: >-
      'HostRegexp(`testdomain2.example.com`,
      `{subdomain:[a-zA-Z0-9-]+}.testdomain2.example.com`)'
    tls_resolver:
      main: 'testdomain.example.com'
      sans: '*.testdomain.example.com'
  # https with default cert
  - name: 'name_config__HTTPS__2'
    services_url: 'http://172.16.1.10:9000'
    domain: 'testdomain2.example.com'
    tls: {}
  # https with Let`s Encrypt auto domain cert + traefik ruled Host
  - name: 'name_config__HTTPS__3'
    services_url: 'http://172.16.1.10:9000'
    raw_domain: >-
      'Host(`testdomain3.example.com`, `testdomain4.example.com`)'
    tls_simple_acme: true
```

#### HTTP and HTTPS service
The `traefik_http_and_https_config` variable describes the configuration of services operating over the `http` and `https protocol`.

The parameter is used in cases when you need to have access to one service using different protocols: `http` and `https`.

The `traefik_http_and_https_config` works with similar parameters `traefik_http_dynamic_config`.

```yaml
# Example:
traefik_http_and_https_config:
  - name: 'test_1'
    services_url: 'http://127.0.0.1:8080/'
    domain: 'test1.local'
```

#### TCP service
The `traefik_tcp_dynamic_config` variable describes the configuration of services operating over the `tcp protocol`.
Required variables: `name`, `services_address`, `port`.
* `name` - The name of your configuration.
* `services_address` - Service address.
* `port` - Listening port for traffic setup.
* `entrypoints_extra_parameters` - Configure parameters Traefik entrypoints.

```yaml
# Example:
traefik_tcp_dynamic_config:
  - name: 'test_config__TCP__'
    services_address: 'git.example.com'
    port: 8086
    entrypoints_extra_parameters:
      forwardedHeaders:
        trustedIPs:
          - "127.0.0.1/32"
          - "172.16.0.0/16"
          - "172.20.100.0/24"
```
#### Transport Layer Security (TLS)
##### TLS Let`s Encrypt

There are variables to use letsencrypt service:
* `traefik_le_caserver`, `traefik_le_challenge_type` and `traefik_le_email` - see above.
* `traefik_le_dns_challenge_provider` - required variable, if `traefik_le_challenge_type: "dnsChallenge"`
```yaml
# Example:
traefik_le_caserver: "https://acme-staging-v02.api.letsencrypt.org/directory"
traefik_le_challenge_type: "dnsChallenge"
traefik_le_email: "testemail@example.com"
traefik_le_dns_challenge_provider: "route53"
```

[TLS. Resource link](https://doc.traefik.io/traefik/https/tls/)

* `traefik_tls_provider_environments` - sets an additional environment variable for the provider.
```yaml
# Example:
traefik_tls_provider_environments:
  - name: "AWS_PROFILE"
    value: "default"
```

| **Provider**        | **Environments**            |
| ------------------- | --------------------------- |
| `route53` | `AWS_PROFILE`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. |

[Provider. Resource link](https://doc.traefik.io/traefik/https/acme/#providers)

##### Default not-LE certs
To use your certificates, set - `traefik_tls_cert` and `traefik_tls_key`.
```yaml
# Example:
traefik_tls_cert: |
  -----BEGIN CERTIFICATE-----
  -----END CERTIFICATE-----
traefik_tls_key: |
  -----BEGIN RSA PRIVATE KEY-----
  -----END RSA PRIVATE KEY-----
```

[Default Certificate. Resource link](https://doc.traefik.io/traefik/https/tls/#default-certificate)

# Example file of inventory
```yaml
all:
  hosts:
    host
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: '/path/to/.ssh/key'
    traefik_log_level: 'DEBUG'
    traefik_api_debug: false
    traefik_http_dynamic_config:
      - name: 'name_config__HTTP__'
        services_url: 'http://172.16.1.10:9000'
        domain: 'testdomain.example.com'
        tls_resolver:
          main: 'testdomain.example.com'
          sans: '*.testdomain.example.com'
    traefik_tcp_dynamic_config:
      - name: 'name_config__TCP__'
        port: 8090
        services_address: 'git.example.com:22'
    traefik_tls_provider_environments:
      - name: "AWS_PROFILE"
        value: "default"
      - name: "AWS_ACCESS_KEY_ID"
        value: "token"
      - name: "AWS_SECRET_ACCESS_KEY"
        value: "token"
    traefik_le_caserver: "https://acme-staging-v02.api.letsencrypt.org/directory"
    traefik_le_challenge_type: "dnsChallenge"
    traefik_le_email: "main_email@example.com"
    traefik_le_dns_challenge_provider: "route53"
    traefik_tls_cert: |
      -----BEGIN CERTIFICATE-----
      -----END CERTIFICATE-----
    traefik_tls_key: |
      -----BEGIN RSA PRIVATE KEY-----
      -----END RSA PRIVATE KEY-----
```

# Info about configuration files
This is role worked with two type configuration files: `dynamic` and `custom`.

`Dynamic config files` - These files rewrite in process deployment project every time. 
Files located: `/etc/traefik/config/dynamic/`

`Custom config files` - Configuration files that are managed individually.
Files located: `/etc/traefik/config/custom/`

# Supported OS
Any OS that has a `systemd` service.

Tested on distributions:
- Ubuntu 18.04
- Centos 7

Enjoy it!


## License

BSD

## Author Information

[Sergey Klyuykov](https://github.com/onegreyonewhite)
[Konstantin Shumkin](https://github.com/kotofeych)
