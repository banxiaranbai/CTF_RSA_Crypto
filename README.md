# CTF_RSA_Crypto
This program will briefly discuss CTF's RSA crypto. <br>
RSA作为一种非常经典的非对称公开密钥加密体制，属于是CTF中的常客。不管是在密码学中、逆向中还是PWN中，都有它的身影。<br>
本文章就简要介绍CTF中RSA常见题目与解题思路。<br>

## RSA加密与解密
1. RSA原理:<br>
**密文 = 明文<sup>E</sup>modN**<br>
RSA加密是对明文的E次方后除以N后求余数的过程。<br>
从通式可知，只要知道E和N任何人都可以进行RSA加密了<br>
**公钥 = (E,N)** <br>
