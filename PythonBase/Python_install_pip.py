Python2.7 安装以及安装pip

一、准备工作
1.下载Python源码包
$ wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2 --no-check-certificate

2.查看是否安装make工具
$ rpm -qa|grep make
automake-1.11.1-4.el6.noarch
make-3.81-20.el6.x86_64

### 如果没有安装make工具
yum -y install gcc automake autoconf libtool make

3.查看是否安装zlib库
$ rpm -qa|grep zlib
zlib-devel-1.2.3-29.el6.x86_64
zlib-1.2.3-29.el6.x86_64

### 如果没有安装安装zlib
yum install zlib-devel

4.检查是否安装ssl 库
$ rpm -qa|grep openssl
openssl-devel-1.0.1e-16.el6_5.x86_64
openssl-static-1.0.1e-16.el6_5.x86_64
openssl098e-0.9.8e-17.el6.centos.2.x86_64
openssl-1.0.1e-16.el6_5.x86_64
openssl-perl-1.0.1e-16.el6_5.x86_64

安装openssl
yum install openssl*

5.安装bzip2依赖库
yum install -y bzip2*

二、编译安装
$ cp Python-2.7.3.tar.bz2 /usr/src/
$ tar -jxvf Python-2.7.3.tar.bz2
$ vi Modules/Setup.dist
找到一下内容把注释去掉
#SSL=/usr/local/ssl
#_ssl _ssl.c \
#    -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
#    -L$(SSL)/lib -lssl -lcrypto
......
#zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz

python安装了2.7之后终端无法使用退格，上下左右
yum install readline-devel
然后重新编译安装python，终端控制符可用！

$ ./configure --prefix=/usr/local/python2.7
$ make all 
$ make install
$ make clean
$ make distclean
建立python2.7 软链
$ mv /usr/bin/python /usr/bin/python.bak
$ ln -s /usr/local/python2.7/bin/python2.7 /usr/bin/python2.7
$ ln -s /usr/bin/python2.7 /usr/bin/python

解决yum无法使用的问题
$ yum update

因为centos6.5 下yum默认使用的是python2.6
vim /usr/bin/yum
#!/usr/bin/python
修改为
#!/usr/bin/python2.6

三、安装python-pip工具
$ wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg --no-check-certificate
$ chmod +x setuptools-0.6c11-py2.7.egg
$ sh setuptools-0.6c11-py2.7.egg

安装pip
$ wget https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz --no-check-certificate
$ cp pip-1.3.1.tar.gz /usr/src/
$ tar zxvf pip-1.3.1.tar.gz
$ cd pip-1.3.1
$ python setup.py install
$ ln -s /usr/local/python2.7/bin/pip /usr/bin/pip






