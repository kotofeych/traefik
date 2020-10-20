import testinfra

host = testinfra.get_hosts('all')
traefik_service_content = '''
# https://raw.githubusercontent.com/containous/traefik/master/contrib/systemd/traefik.service

[Unit]
Description=Traefik
Documentation=https://docs.traefik.io
AssertFileIsExecutable=/usr/bin/traefik_v2.3.2
AssertPathExists=/etc/traefik/traefik.yaml

[Service]
Environment="AWS_PROFILE=default"
Environment="AWS_ACCESS_KEY_ID="
Environment="AWS_SECRET_ACCESS_KEY="
Type=notify
ExecStart=/usr/bin/traefik_v2.3.2
Restart=always
WatchdogSec=1s

[Install]
WantedBy=multi-user.target
'''
global_yaml_content = '''
http:
    middlewares:
        redirect-http-to-https:
            redirectScheme:
                scheme: https
tls:
    stores:
        default:
            defaultCertificate:
                certFile: /etc/traefik/cert/default.crt
                keyFile: /etc/traefik/cert/default.pem
'''
traefik_yaml_content = '''
entryPoints:
  http:
    address: ":80"
  https:
    address: ":443"
  traefik:
    address: ":8080"
  test_config__TCP__:
    address: ":8090"

providers:
  file:
    directory: /etc/traefik/dynamic/
    watch: false

certificatesResolvers:
  default_le_resolver:
    acme:
      email: main_email@example.com
      storage: /etc/traefik/acme/acme.json
      caServer: https://acme-staging-v02.api.letsencrypt.org/directory
      dnsChallenge:
        provider: route53

api:
  dashboard: true
  insecure: true
  debug: true

log:
  level: DEBUG
'''

check_files = {
    '/etc/systemd/system/traefik.service': traefik_service_content,
    '/etc/traefik/dynamic/_global.yaml': global_yaml_content,
    '/etc/traefik/traefik.yaml': traefik_yaml_content
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
