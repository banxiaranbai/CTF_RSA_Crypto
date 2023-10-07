# CTF_RSA_Crypto
This program will briefly discuss CTF's RSA crypto. <br>
RSA作为一种非常经典的非对称公开密钥加密体制，属于是CTF中的常客。不管是在密码学中、逆向中还是PWN中，都有它的身影。<br>
本文章就简要介绍CTF中RSA常见题目与解题思路。
## RSA加密与解密
1. RSA概述:<br>
**密文 = 明文<sup>E</sup>modN**<br>
RSA加密是对明文的E次方后除以N后求余数的过程。<br>
从通式可知，只要知道E和N任何人都可以进行RSA加密了<br>
**公钥 = (E,N)** <br>
2. 下面简要介绍RSA加密中出现的各个字母含义<br>
明文M：待加密的文本，一般是题目中的flag，是我们需要求解的内容。<br>
密文C：加密完成后的密文，一般题目会给你，我们要做的就是根据密文解密出明文。<br>
公钥e（加密钥）：用来加密的密钥，是一个整数，是公开的。<br>
两个大素数p,q：RSA加密的关键部分。选取两个大素数并计算它们的乘积，得到n=p\*q。后面会用p,q,n来加密解密。由于p,q非常大，想要对n进行因式分解得到p，q非常困难，这也确保了RSA的安全性。*注:题目一般不会给出p、q，而是给出n,需要因式分解得到p、q*<br>
私钥 d（解密钥）：用来解密，一般需要求出。d满足e\*d mod (p-1)(q-1)=1，所以我们只要知道e、p和q就可以把d算出来。<br>
加密过程：<br>
**<center> C = M<sup>e</sup> mod N</center>**<br>
解密过程：<br>
**<center> M = C<sup>d</sup> mod N</center>**<br>
## 常见思路分析
### 1.1 知道C、N、e
- 需要因式分解N，得到p,q。可去往网站[factordb](http://www.factordb.com/)
- 得到p,q按照脚本解密就行(CNE1.py)。
### 1.2 知道C、N、e(但是N分解出多个因子)
- 需要因式分解N，得到p,q。可去往网站[factordb](http://www.factordb.com/)
- 但出现了多个因子，直接求φ(n)，即欧拉函数。
- 解密脚本(CNE2.py)
### 2. 低加密指数攻击
**使用情况：N很大但e很小**
- n很大时，无法进行因式分解，此时我们可以可以根据公式 C = M<sup>e</sup> + k\*n ,对k进行爆破，多次开根进行后得到M
- 解密脚本(Low_Attack.py)
### 3. 低指数加密广播攻击
**使用情况:出现多组不同的N、C,但是使用的是同一个e且e的数值小**
- 采用中国剩余定理求出 M<sup>e</sup> ,进行解密。
- 解密脚本(Low_radio.py)
