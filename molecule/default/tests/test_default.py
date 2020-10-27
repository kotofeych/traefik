import testinfra

host = testinfra.get_hosts('all')
# Files to check
traefik_service_content = '''
# https://raw.githubusercontent.com/containous/traefik/master/contrib/systemd/traefik.service

[Unit]
Description=Traefik
Documentation=https://docs.traefik.io
AssertFileIsExecutable=/usr/bin/traefik_v2.3.2
AssertPathExists=/etc/traefik/traefik.yaml

[Service]
Environment="AWS_PROFILE=default"
Environment="AWS_ACCESS_KEY_ID=token_access"
Environment="AWS_SECRET_ACCESS_KEY=token_secret"
Type=notify
ExecStart=/usr/bin/traefik_v2.3.2
Restart=always
WatchdogSec=1s

[Install]
WantedBy=multi-user.target
'''
global_yaml_content = '''
---
http:
    middlewares:
        redirect-http-to-https:
            redirectScheme:
                scheme: https
        proxy-proto-headers:
            headers:
                customRequestHeaders:
                    X-Forwarded-Protocol: "https"
                    X-Forwarded-Proto: "https"

tls:
    stores:
        default:
            defaultCertificate:
                certFile: /etc/traefik/cert/default.crt
                keyFile: /etc/traefik/cert/default.pem
'''
traefik_yaml_content = '''
---
entryPoints:
  http:
    address: ":80"
  https:
    address: ":443"
  traefik:
    address: ":8083"
  metrics:
    address: ":8081"
  test_1:
    address: ":8090"

providers:
  file:
    directory: /etc/traefik/dynamic/
    watch: false
  docker:
    defaultRule: Host(`{{ .Name }}.example.com`)
    endpoint: tcp://1.1.1.1:2376
    exposedByDefault: false
    useBindPortIP: false

certificatesResolvers:
  default_le_resolver:
    acme:
      email: main_email@example.com
      storage: /etc/traefik/acme/acme.json
      caServer: https://acme-staging-v02.api.letsencrypt.org/directory
      dnsChallenge:
        provider: route53

metrics:
  prometheus:
    entryPoint: metrics
    addServicesLabels: true
    addEntryPointsLabels: true
    buckets:
      - 0.1
      - 0.3
      - 1.2
      - 5.0

api:
  dashboard: true
  insecure: true
  debug: true

log:
  level: DEBUG
'''
default_crt = '''
-----BEGIN CERTIFICATE-----
MIIEJzCCAw+gAwIBAgIBBDANBgkqhkiG9w0BAQsFADCBmjELMAkGA1UEBhMCUlUx
GDAWBgNVBAgTD1ByaW1vcnNraXkga3JheTEUMBIGA1UEBxMLVmxhZGl2b3N0b2sx
FzAVBgNVBAoTDlZTVCBjb25zdWx0aW5nMQ0wCwYDVQQLEwRJbmMuMQwwCgYDVQQD
EwNWU1QxJTAjBgkqhkiG9w0BCQEWFm1haWxAdnN0Y29uc3VsdGluZy5uZXQwHhcN
MjAwOTE1MDM1NDAwWhcNMjEwOTE1MDM1NDAwWjBtMQswCQYDVQQGEwJSVTELMAkG
A1UECBMCMjUxCzAJBgNVBAcTAlZMMQwwCgYDVQQKEwNWU1QxDDAKBgNVBAsTA1ZT
VDEMMAoGA1UEAxMDVlNUMRowGAYJKoZIhvcNAQkBFgt2c3RAbWFpbC5ydTCCASIw
DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALfx07fKv2Cjmu1xmv4yJTdLPurr
X1rDNGdT551QX4ZkQHhv1oMI/kezHaNLuPQXnTJIRqGXBHhyvinBdWEuuU3rKMJv
g5HpbUaMnu7pEHe9fxmtgYv8aFu8hCROefrdQdj/xu953G004E372SG8OuV3s+ca
+dvA4ma6ykFQhPRA8LFpfW5s9qzgVe6AbeFn3xE/k33a7Jhw5sSgS8ahUmjayFDU
GHiqTbCDTzHhPwNYpsbPhYl+mDPqJs/V9rKZ4tkp5KtB6Zi3rbsFe2HTfbmIBLb8
CxpJOda+IlUXyWff5X6ffRggwaHQ9MsMTY4EOR9cEEOQqNd87mhPwnt2irkCAwEA
AaOBozCBoDAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRZXpUlSMz7Xn7R238YlRlC
vn6+GTALBgNVHQ8EBAMCBeAwMQYDVR0RBCowKIITdHJhZWZpay5zYW5kYm94Lmxh
bocErBABeIELdnN0QG1haWwucnUwEQYJYIZIAYb4QgEBBAQDAgZAMB4GCWCGSAGG
+EIBDQQRFg94Y2EgY2VydGlmaWNhdGUwDQYJKoZIhvcNAQELBQADggEBAFMMXAmO
VceME/Ig6Jo7TTpaAB4gS7lEpGg8mU7iUUCRN/hfGmvdobRP0x9HIR+/Qy7Qoa4x
UIArJgbZcN4RbHLQBmM23fWNGicLQZxVXcJ0Vp4Qu98aeoSRK3+UbVRs65OX1Akm
a9/yxhkZfAFcuzK7d+8NxKdTB2LjgEi+P/bdCyGATs/avlTSLO2xrAq3N0gsdPFB
yYZV2iYMGz9KVJ7cS6/ySQ9DlVRoKMDVhvGtbFozbvD34OsEANRGLFU2SdBw2hIs
28Uq9OXxx7sQjjX9/cG75nEpstCldXgg0Va24Y7RXNhunbC2qTLnXNHdZn+4Fd9k
DEkKriv9yWu9fX4=
-----END CERTIFICATE-----
'''
default_pem = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAt/HTt8q/YKOa7XGa/jIlN0s+6utfWsM0Z1PnnVBfhmRAeG/W
gwj+R7Mdo0u49BedMkhGoZcEeHK+KcF1YS65Tesowm+DkeltRoye7ukQd71/Ga2B
i/xoW7yEJE55+t1B2P/G73ncbTTgTfvZIbw65Xez5xr528DiZrrKQVCE9EDwsWl9
bmz2rOBV7oBt4WffET+TfdrsmHDmxKBLxqFSaNrIUNQYeKpNsINPMeE/A1imxs+F
iX6YM+omz9X2spni2Snkq0HpmLetuwV7YdN9uYgEtvwLGkk51r4iVRfJZ9/lfp99
GCDBodD0ywxNjgQ5H1wQQ5Co13zuaE/Ce3aKuQIDAQABAoIBAGFxrHTq5SMuyH4M
9sy+h9SY+gW9FtCgJHywiDxgPZqWNUkYBg14kCwviP3euWYltFLU0wX7WJTuRCse
ny4ScHwEnZ0TMiH0BL2g9PkfYmfsbQ6PSdd8qVQfs+j/4cKxv5ZTOXHXnpwDrOfj
CQ3EB3dUSGufcMmnjshZH5gmLaiubxTYTV4X83XHICEEs7YNAgoxZLWU0iSssseo
VD4pEnxik0gZIzNh2HRpJuCCuk7T9PSxZwUqI8yUM8TcdPFaX1CVxcKTTuPOkLU1
FzvBm94ecpjoGHhI026dHymVXGTX1nHKeOQay4m+ANutKDeOTBVzqMh8uTDxffcY
+nZNLpkCgYEA8aGKKOcZZBXZcH0f1oNpEUhrNMArUunAjBmCEmKYSEALih7UIlML
px4ZTZYSSa6vtI/FvXAJFzeUF6FRhotuXl/xud7PbPSpKzNhO/vkYI9om4iuTe4V
6Bt+vCZKC/obvBZzKPYq5FuJ5p1H8t5UPU3s0INu6BmivY6Mi8YnEO8CgYEAwuIZ
3GxFH5tFFjJbBrCPiLp0fZmeBgF1tTM2rRSYnZQPO/40M7LglmRj74QcvqpXIRPR
nGYT8Vc9NRbj7c1dCMeyb24wUbuCUT7or+KSosNgEqmlUEZtMKwCb2FHtz+ESAKw
iLPusyMjTaOgyMj5tWLrZA65bqU0UfgL90FpztcCgYEA3eygGDEpAOOQceB5/Wt0
dIsu66QUJnLKheJntLsZYkJwVss5ysy7RyI92ySaZ1Ipzoy98N+Ved1yBsIDPq+R
DtzQBwa9PDT5qtPl2lHfz0/no/JFJQ4m0KdwHx6Lo7RzBK0Z1+VAP7xTS5vpGQda
F3QarOgKVOI2tiLWswmrl8ECgYBOoP8iKiTxjaogPIzxdAdVeTVK/9H8RlaBl3o1
9xtkaLqE0Bmryj5HL5YKq1kVrJCe7eoimiTtuO8fHm80ISmqQzhBMUoZj/gSY7lq
TZYwSXfXz869Rs0DWENbQPq4es4aZ8tmPILQkBrMVnqmyD/H6XNj2XUDqXAkqlnZ
lvDj3QKBgQDrbenRM+aZ/gGnmSFX/bEWEMfP9henvza9KZiq3TjzN2YSY+xL1NAx
DxDbIV+PFMVAX9OynGJuDtc7dwWtVH5YqlCxmb5gRfLiYH1qIj6ek/l1ASVPztLI
pEsGJQKqucl+D1lho20uWAoCeeXOSTLwpi7TdIwJEtciMMvQtk1LvQ==
-----END RSA PRIVATE KEY-----
'''
test_1_http = '''
---
http:
  routers:
    http_test_1:
      rule: Host(`testdomain.example.com`)
      entrypoints:
        - http
      service: test_1
      middlewares:
      - redirect-http-to-https
    https_test_1:
      rule: Host(`testdomain.example.com`)
      entrypoints:
        - https
      service: test_1
      middlewares:
      - proxy-proto-headers
      tls:
        certResolver: default_le_resolver
        domains:
          - main: testdomain.example.com
            sans:
              - '*.testdomain.example.com'

  services:
    test_1:
      loadBalancer:
        servers:
          - url: http://172.16.1.10:9000
'''
test_2_http = '''
---
http:
  routers:
    http_test_2:
      rule: Host(`dom1.example.com`)
      entrypoints:
        - http
      service: test_2
      middlewares:
      - redirect-http-to-https
    https_test_2:
      rule: Host(`dom1.example.com`)
      entrypoints:
        - https
      service: test_2
      middlewares:
      - proxy-proto-headers
      tls:
        {}


  services:
    test_2:
      loadBalancer:
        servers:
          - url: http://172.16.1.10:9000
'''
test_3_http = '''
---
http:
  routers:
    http_test_3:
      rule: Host(`dom2.example.com`)
      entrypoints:
        - http
      service: test_3

  services:
    test_3:
      loadBalancer:
        servers:
          - url: http://172.16.1.10:9000
'''
test_4_http = '''
---
http:
  routers:
    http_test_4:
      rule: 'HostRegexp(`testdomain2.example.com`, \
`{subdomain:[a-zA-Z0-9-]+}.testdomain2.example.com`)'
      entrypoints:
        - http
      service: test_4
      middlewares:
      - redirect-http-to-https
    https_test_4:
      rule: 'HostRegexp(`testdomain2.example.com`, \
`{subdomain:[a-zA-Z0-9-]+}.testdomain2.example.com`)'
      entrypoints:
        - https
      service: test_4
      middlewares:
      - proxy-proto-headers
      tls:
        certResolver: default_le_resolver
        domains:
          - main: testdomain2.example.com
            sans:
              - '*.testdomain2.example.com'

  services:
    test_4:
      loadBalancer:
        servers:
          - url: http://172.16.1.10:9000
'''
test_5_http = '''
---
http:
  routers:
    http_test_5:
      rule: 'HostRegexp(`testdomain3.example.com`)'
      entrypoints:
        - http
      service: test_5
      middlewares:
      - redirect-http-to-https
    https_test_5:
      rule: 'HostRegexp(`testdomain3.example.com`)'
      entrypoints:
        - https
      service: test_5
      middlewares:
      - proxy-proto-headers
      tls:
        certResolver: default_le_resolver
  services:
    test_5:
      loadBalancer:
        servers:
          - url: http://172.16.1.10:9000
'''
test_1_tcp = '''
---
tcp:
  routers:
    tcp_test_1:
      entryPoints:
        - "test_1"
      service: "test_1"
      rule: "HostSNI(`*`)"

  services:
    test_1:
      loadBalancer:
        servers:
          - address: git.example.com:22
'''

check_files = {
    '/etc/systemd/system/traefik.service': traefik_service_content,
    '/etc/traefik/cert/default.crt': default_crt,
    '/etc/traefik/cert/default.pem': default_pem,
    '/etc/traefik/traefik.yaml': traefik_yaml_content,
    '/etc/traefik/dynamic/_global.yaml': global_yaml_content,
    '/etc/traefik/dynamic/test_1_http.yaml': test_1_http,
    '/etc/traefik/dynamic/test_2_http.yaml': test_2_http,
    '/etc/traefik/dynamic/test_3_http.yaml': test_3_http,
    '/etc/traefik/dynamic/test_4_http.yaml': test_4_http,
    '/etc/traefik/dynamic/test_5_http.yaml': test_5_http,
    '/etc/traefik/dynamic/test_1_tcp.yaml': test_1_tcp
}


def test_check_distribution(host):
    assert host.system_info.distribution.lower() in [
        'ubuntu',
        'centos'
    ]


def test_check_file_traefik(host):
    assert host.file("/usr/bin/traefik_v2.3.2").exists

    for file_path, content in check_files.items():
        file_obj = host.file(file_path)
        assert file_obj.exists
        assert file_obj.content_string == content.lstrip()
