
[root@docker ~]# git clone git://github.com/ansible/ansible.git --recursive
[root@docker ~]# cd ansible/

#ImportError: No module named argparse
[root@node2 ansible]# yum install -y python-argparse

#ImportError: No module named packaging.version
