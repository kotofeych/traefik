  #- name:
  #
  #- проверить, есть ли в директории `cert` или `dynamic` файлы
  #- если нет - создаем с нуля
  #- если есть -
  #  - создание временных директорий
  #    - записать шаблоны конфигурационных файлов и сертификатов во временные директории
  #    - просчитать общее количество файлов во временных директорий
  #    - просчитать контрольные суммы файлов
  #  - произвести определенную работу с конфигами
  #    - просчитать общее количество файлов в директории `cert` и `dynamic`
  #    - просчитать контрольные суммы файлов
  
 "Create dir: 
 {'results': 
 [{
 'path': '/etc/traefik/acme', 
 'changed': False, 
 'diff': 
    {'before': 
        {'path': '/etc/traefik/acme', 
        'state': 'absent', 
        'mode': '0755'},
    'after':
        {'path': '/etc/traefik/acme', 
        'state': 'directory', 
        'mode': '0644'}}, 
    'uid': 0, 
    'gid': 0, 
    'owner': 'root', 
    'group': 'root', 
    'mode': '0644', 
    'state': 'directory', 
    'size': 4096, 
    'invocation': 
        {'module_args': 
            {'path': '/etc/traefik/acme', 
            'state': 'directory', 
            'mode': 420, 
            'recurse': False, 
            'force': False, 
            'follow': True, 
            'modification_time_format': '%Y%m%d%H%M.%S', 
            'access_time_format': '%Y%m%d%H%M.%S', 
            '_original_basename': None, 
            '_diff_peek': None, 
            'src': None, 
            'modification_time': None,
            'access_time': None, 
            'owner': None, 
            'group': None, 
            'seuser': None, 
            'serole': None, 
            'selevel': None, 
            'setype': None, 
            'attributes': None,
            'content': None, 
            'backup': None, 
            'remote_src': None, 
            'regexp': None, 
            'delimiter': None, 
            'directory_mode': None, 
            'unsafe_writes': None}}, 
            'failed': False, 
            'item': {'name': 'acme'}, 
            'ansible_loop_var': 'item'},
            {'path': '/etc/traefik/cert', 'changed': False, 'diff': {'before': {'path': '/etc/traefik/cert', 'state': 'absent', 'mode': '0755'}, 'after': {'path': '/etc/traefik/cert', 'state': 'directory', 'mode': '0644'}}, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'directory', 'size': 4096, 'invocation': {'module_args': {'path': '/etc/traefik/cert', 'state': 'directory', 'mode': 420, 'recurse': False, 'force': False, 'follow': True, 'modification_time_format': '%Y%m%d%H%M.%S', 'access_time_format': '%Y%m%d%H%M.%S', '_original_basename': None, '_diff_peek': None, 'src': None, 'modification_time': None, 'access_time': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'content': None, 'backup': None, 'remote_src': None, 'regexp': None, 'delimiter': None, 'directory_mode': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'cert'}, 'ansible_loop_var': 'item'}, {'path': '/etc/traefik/config/dynamic', 'changed': False, 'diff': {'before': {'path': '/etc/traefik/config/dynamic', 'mode': '0755'}, 'after': {'path': '/etc/traefik/config/dynamic', 'mode': '0644'}}, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'directory', 'size': 4096, 'invocation': {'module_args': {'path': '/etc/traefik/config/dynamic', 'state': 'directory', 'mode': 420, 'recurse': False, 'force': False, 'follow': True, 'modification_time_format': '%Y%m%d%H%M.%S', 'access_time_format': '%Y%m%d%H%M.%S', '_original_basename': None, '_diff_peek': None, 'src': None, 'modification_time': None, 'access_time': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'content': None, 'backup': None, 'remote_src': None, 'regexp': None, 'delimiter': None, 'directory_mode': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'config/dynamic'}, 'ansible_loop_var': 'item'}, {'path': '/etc/traefik/config/custom', 'changed': False, 'diff': {'before': {'path': '/etc/traefik/config/custom', 'state': 'absent', 'mode': '0755'}, 'after': {'path': '/etc/traefik/config/custom', 'state': 'directory', 'mode': '0644'}}, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'directory', 'size': 4096, 'invocation': {'module_args': {'path': '/etc/traefik/config/custom', 'state': 'directory', 'mode': 420, 'recurse': False, 'force': False, 'follow': True, 'modification_time_format': '%Y%m%d%H%M.%S', 'access_time_format': '%Y%m%d%H%M.%S', '_original_basename': None, '_diff_peek': None, 'src': None, 'modification_time': None, 'access_time': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'content': None, 'backup': None, 'remote_src': None, 'regexp': None, 'delimiter': None, 'directory_mode': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'config/custom'}, 'ansible_loop_var': 'item'}], 'msg': 'All items completed', 'changed': False}",
 

"Create config: {'results': [{'diff': [], 'dest': '/etc/traefik/config/dynamic/test_1_http.yaml', 'src': '/root/.ansible/tmp/ansible-tmp-1621319808.9191399-284840-36310413957194/source', 'md5sum': '7f2599b3dfcdca0fe4dbd6332cb56a5a', 'checksum': '79a8974b3537f37e17b8025604560533ca1c85a1', 'changed': False, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'file', 'size': 627, 'invocation': {'module_args': {'src': '/root/.ansible/tmp/ansible-tmp-1621319808.9191399-284840-36310413957194/source', 'dest': '/etc/traefik/config/dynamic/test_1_http.yaml', 'mode': 420, 'follow': False, '_original_basename': 'traefik.http.dynamic.yaml.j2', 'checksum': '79a8974b3537f37e17b8025604560533ca1c85a1', 'backup': False, 'force': True, 'content': None, 'validate': None, 'directory_mode': None, 'remote_src': None, 'local_follow': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'regexp': None, 'delimiter': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'test_1', 'services_url': 'http://172.16.1.10:9000', 'domain': 'testdomain.example.com', 'tls_resolver': {'main': 'testdomain.example.com', 'sans': '*.testdomain.example.com'}}, 'ansible_loop_var': 'item'}, {'diff': [], 'dest': '/etc/traefik/config/dynamic/test_2_http.yaml', 'src': '/root/.ansible/tmp/ansible-tmp-1621319810.9288046-284840-201264119446392/source', 'md5sum': 'cc9a81ad7ab326babf7d87ab9f3a7c55', 'checksum': 'e7e871cd5c199fe930cd372babc7ab2eec7a06ed', 'changed': False, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'file', 'size': 466, 'invocation': {'module_args': {'src': '/root/.ansible/tmp/ansible-tmp-1621319810.9288046-284840-201264119446392/source', 'dest': '/etc/traefik/config/dynamic/test_2_http.yaml', 'mode': 420, 'follow': False, '_original_basename': 'traefik.http.dynamic.yaml.j2', 'checksum': 'e7e871cd5c199fe930cd372babc7ab2eec7a06ed', 'backup': False, 'force': True, 'content': None, 'validate': None, 'directory_mode': None, 'remote_src': None, 'local_follow': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'regexp': None, 'delimiter': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'test_2', 'services_url': 'http://172.16.1.10:9000', 'domain': 'dom1.example.com', 'tls': {}}, 'ansible_loop_var': 'item'}, {'diff': [], 'dest': '/etc/traefik/config/dynamic/test_3_http.yaml', 'src': '/root/.ansible/tmp/ansible-tmp-1621319813.020441-284840-147247713373189/source', 'md5sum': '45035709a4af9dc5be17bd84de8f6df0', 'checksum': '6dba5cfcabc0980387981054dc0b46917a20a0ff', 'changed': False, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'file', 'size': 234, 'invocation': {'module_args': {'src': '/root/.ansible/tmp/ansible-tmp-1621319813.020441-284840-147247713373189/source', 'dest': '/etc/traefik/config/dynamic/test_3_http.yaml', 'mode': 420, 'follow': False, '_original_basename': 'traefik.http.dynamic.yaml.j2', 'checksum': '6dba5cfcabc0980387981054dc0b46917a20a0ff', 'backup': False, 'force': True, 'content': None, 'validate': None, 'directory_mode': None, 'remote_src': None, 'local_follow': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'regexp': None, 'delimiter': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'test_3', 'services_url': 'http://172.16.1.10:9000', 'domain': 'dom2.example.com'}, 'ansible_loop_var': 'item'}, {'diff': [], 'dest': '/etc/traefik/config/dynamic/test_4_http.yaml', 'src': '/root/.ansible/tmp/ansible-tmp-1621319814.912267-284840-161560645633002/source', 'md5sum': 'ebeaadc4b63248381b774f38b4d5776a', 'checksum': 'd4c1b4cab1881470672df3ce3d548760b0858d0e', 'changed': False, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'file', 'size': 753, 'invocation': {'module_args': {'src': '/root/.ansible/tmp/ansible-tmp-1621319814.912267-284840-161560645633002/source', 'dest': '/etc/traefik/config/dynamic/test_4_http.yaml', 'mode': 420, 'follow': False, '_original_basename': 'traefik.http.dynamic.yaml.j2', 'checksum': 'd4c1b4cab1881470672df3ce3d548760b0858d0e', 'backup': False, 'force': True, 'content': None, 'validate': None, 'directory_mode': None, 'remote_src': None, 'local_follow': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'regexp': None, 'delimiter': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'test_4', 'services_url': 'http://172.16.1.10:9000', 'raw_domain': \"'HostRegexp(`testdomain2.example.com`, `{subdomain:[a-zA-Z0-9-]+}.testdomain2.example.com`)'\", 'tls_resolver': {'main': 'testdomain2.example.com', 'sans': '*.testdomain2.example.com'}}, 'ansible_loop_var': 'item'}, {'diff': [], 'dest': '/etc/traefik/config/dynamic/test_5_http.yaml', 'src': '/root/.ansible/tmp/ansible-tmp-1621319816.9660268-284840-105148949197147/source', 'md5sum': '32b152ce67814264d2491eb5be9585db', 'checksum': 'd21676ea513595f04f4469634e662c4d8178c3e4', 'changed': False, 'uid': 0, 'gid': 0, 'owner': 'root', 'group': 'root', 'mode': '0644', 'state': 'file', 'size': 525, 'invocation': {'module_args': {'src': '/root/.ansible/tmp/ansible-tmp-1621319816.9660268-284840-105148949197147/source', 'dest': '/etc/traefik/config/dynamic/test_5_http.yaml', 'mode': 420, 'follow': False, '_original_basename': 'traefik.http.dynamic.yaml.j2', 'checksum': 'd21676ea513595f04f4469634e662c4d8178c3e4', 'backup': False, 'force': True, 'content': None, 'validate': None, 'directory_mode': None, 'remote_src': None, 'local_follow': None, 'owner': None, 'group': None, 'seuser': None, 'serole': None, 'selevel': None, 'setype': None, 'attributes': None, 'regexp': None, 'delimiter': None, 'unsafe_writes': None}}, 'failed': False, 'item': {'name': 'test_5', 'services_url': 'http://172.16.1.10:9000', 'raw_domain': \"'HostRegexp(`testdomain3.example.com`)'\", 'tls_simple_acme': True}, 'ansible_loop_var': 'item'}], 'msg': 'All items completed', 'changed': False}"
