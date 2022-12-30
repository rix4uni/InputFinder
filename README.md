# InputFinder

InputFinder find all input fields

## Installation
```
git clone https://github.com/rix4uni/InputFinder.git
cd InputFinder
pip3 install -r requirements.txt
```

## Example usages

Single URL:
```
echo "http://testphp.vulnweb.com/login.php" | python3 inputfinder.py
```

Multiple URLs:
```
cat urls.txt | python3 inputfinder.py
```

urls.txt contains:
```
http://testphp.vulnweb.com/login.php
http://testphp.vulnweb.com/listproducts.php?cat=1
http://testphp.vulnweb.com/AJAX/index.php?id=xyz&cat=2
```

output:
```
http://testphp.vulnweb.com/login.php: [[('id=None', 'name=pass'), ('id=None', 'name=searchFor'), ('id=None', 'name=uname')]]
http://testphp.vulnweb.com/signup.php: [[('id=None', 'name=searchFor'), ('id=None', 'name=uaddress'), ('id=None', 'name=ucc'), ('id=None', 'name=uemail'), ('id=None', 'name=upass'), ('id=None', 'name=upass2'), ('id=None', 'name=uphone'), ('id=None', 'name=urname'), ('id=None', 'name=uuname')]]
```
