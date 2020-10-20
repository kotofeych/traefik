# About role
This ansible role intended for setting on the host Traefik. 

# Using variables

### Defaults variables
| **Inventory**                              | **Description**             |
| ------------------------------------------ | --------------------------- |
| `traefik_distr_ver` | The version of Traefik used. (Default: `v2.3.2`) |
| `traefik_distr_os` | Operating system. (Default: `linux`) |
| `traefik_distr_arch` | OS architecture. (Default: `amd64`) |
| `traefik_url_release` | Traefik Archive URL. (Default: `https://github.com/containous/traefik/releases/download/v2.3.2/traefik_v2.3.2_linux_amd64.tar.gz`) |
| `traefik_path_bin` | Traefik bin location path. (Default: `/usr/bin`) |
| `traefik_binary` | Full path of Traefik on the system. (Default: `/usr/bin/traefik_v2.3.2`) |
| `molecule_test_run` | Designed to disable systemd tasks. For testing, the parameter must be set to `true` in the molecule. (Default: `false`) |
| `traefik_le_caserver` |  Determines which service issues the certificate. For test runs use - `https://acme-staging-v02.api.letsencrypt.org/directory.`. For production - `https://acme-v02.api.letsencrypt.org/directory`. (Default: `https://acme-v02.api.letsencrypt.org/directory`) |
| `traefik_le_challenge_type` | Different ACME Challenges. It is possible to use `httpChallenge` and `dnsChallenge`. (Default: `httpChallenge`) |
| `traefik_le_email` | Required parameter to get the certificate Let’s Encrypt. (Default: `NULL`) |

### Inventory variables
#### HTTP service
The `traefik_http_dynamic_config` variable describes the configuration of services operating over the `http protocol`.
Required variables: `name`, `services_url`, `domain`.
* `name` - The name of your configuration.
* `services_url` - Service address.
* `domain` - The domain on which the service will run.

TLS Certificates:
* You can connect your TLS Certificate to each service `tls_resolver` or `tls`.
* `tls` - Your generated self-signed certificate.
* `tls_resolver` - Certificate provided by Let’s Encrypt. 
Required parameters: `main` and `sans`.

```yaml
# Example:
traefik_http_dynamic_config:
  - name: 'name_config__HTTP__'
    services_url: 'http://172.16.1.10:9000'
    domain: 'test-http.vst.lan'
  - name: 'name_config__HTTPS__1'
    services_url: 'http://172.16.1.10:9000'
    domain: 'subdomain.example.com'
    tls_resolver:
      main: 'testdomain.example.com'
      sans: '*.testdomain.example.com'
  - name: 'name_config__HTTPS__2'
    services_url: 'http://172.16.1.10:9000'
    domain: 'test.vst.lan'
    tls: {}
```

#### TCP service
The `traefik_tcp_dynamic_config` variable describes the configuration of services operating over the `tcp protocol`.
Required variables: `name`, `services_address`, `port`.
* `name` - The name of your configuration.
* `services_address` - Service address.
* `port` - Listening port for traffic setup.

TLS Certificates:
Likewise with `traefik_http_dynamic_config` parameters.
```yaml
# Example:
traefik_tcp_dynamic_config:
  - name: 'test_config__TCP__'
    services_address: 'http://172.16.1.10:9000'
    port: 8085
    tls_resolver:
      main: 'testdomain.example.com'
      sans: '*.testdomain.example.com'
  - name: 'test_config__TCP__'
    services_address: 'git.example.com'
    port: 8086
    tls: {}
  - name: 'test_config__TCP2__'
    services_address: 'http://172.16.1.10:9000'
    port: 8087
```
#### TLS
##### TLS Let`s Encrypt
There are variables to use letsencrypt service:
* `traefik_le_caserver`, `traefik_le_challenge_type` and `traefik_le_email` - see above.
* `traefik_le_dns_challenge_provider` - required variable, if `traefik_le_challenge_type: "dnsChallenge"`
```yaml
# Example:
traefik_le_caserver: "https://acme-staging-v02.api.letsencrypt.org/directory"
traefik_le_challenge_type: "dnsChallenge"
traefik_le_email: "testemail@vst.ru"
traefik_le_dns_challenge_provider: "route53"
```
* `traefik_tls_provider_environments` - sets an additional environment variable for the provider.
```yaml
# Example:
traefik_tls_provider_environments:
  - name: "AWS_PROFILE"
    value: "default"
```

| **Provider**                              | **Environments**            |
| ----------------------------------------- | --------------------------- |
| `route53` |  `AWS_PROFILE`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. |


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

# An example of your inventory
```yaml
all:
  hosts:
    host
  vars:
    ansible_user: root
    ansible_ssh_private_key_file: '/path/to/.ssh/key'
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

# Supported OS
Any OS that has a `systemd` service.

Tested on distributions:
- Ubuntu 18.04
- Centos 7

Enjoy it!
