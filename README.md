# vhost-grabber
Retrieve the virtual hosts (vhosts) of a target using the Censys Search Engine API.\
**Introduction to Virtual Hosts By Censys** - https://support.censys.io/hc/en-us/articles/4411773845524

### Install
1. `pip install requests argparse`
2. Get your [Censys API credentials](https://search.censys.io/account/api) and set those with `CENSYS_API_ID` and `CENSYS_API_SECRET` envirnoment variables.

### Basic Usage 
Usage instructions:
```
▶ python vhost-grabber.py --help
usage: vhost-grabber.py [-h] --domain DOMAIN [--type {include,only}]

Grab all vhosts of a target from Censys Search Engine.

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN, -d DOMAIN
                        Please enter the target domain
  --type {include,only}, -t {include,only}
                        Type of scan
```
Note: `--type` flag is optional and default value is set to `only` 

Sample Test:
```
▶ python vhost-grabber.py -d 3.secproxy.sc-corp.net -t include
---------------------------------------------------------------
Target set to -> 3.secproxy.sc-corp.net
Scan type set to -> include
Found total vhosts -> 54
---------------------------------------------------------------
builds.sc-corp.net
drone-ci.sc-corp.net
barista-jupyterhub.sc-corp.net
sharing.snap-dev.net
star.secproxy.sc-corp.net
us-east-1.medialibrary.snap-dev.net
test.snap-dev.net
lens-central-admin.snap-dev.net
council-sfu.sc-corp.net
wiki-dev-api.sc-corp.net
log.lastline.sc-corp.net
staging--ftrack.mesh.sc-corp.net
link.snap-dev.net
key-master-prod.sc-corp.net
tb-chocolatey-cms-poc.snap-dev.net
.....
```

---
*Disclaimer: Please note that I have included the publicly available [snapchat, Inc. domain(scope item)](https://hackerone.com/snapchat?view_policy=true) for bug bounty testing purposes on HackerOne.*
