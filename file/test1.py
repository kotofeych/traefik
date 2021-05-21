import os
import sys


def check_path(etc_path, tmp_path):
    etc_path_exists = os.path.exists(etc_path)
    tmp_path_exists = os.path.exists(tmp_path)
    if etc_path_exists and tmp_path_exists:
        return "True"
    elif not tmp_path_exists:
        return "No such file or directory: " + tmp_path
    elif not etc_path_exists:
        return "No such file or directory: " + etc_path


return_check_path = check_path("/etc/traefik/config/dynamic/", "/tmp/traefik_dynamic1/")
print(return_check_path)


print(str(sys.argv))

# list_differences = set(os.listdir('/etc/traefik/config/dynamic/')).difference(os.listdir('/tmp/traefik_dynamic/'))
# print(list(list_differences))